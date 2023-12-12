import psycopg2
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

conn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port=5432)
cur = conn.cursor()
cur.execute('SELECT num FROM table1')
database = [row[0] for row in cur.fetchall()]

@app.route("/", methods=["POST"])
def function():
    try:
        data = request.get_json()
        a = int(data.get('number'))
    except (ValueError, TypeError):
        return jsonify({"error": "Incorrect data"})
    if a in database:
        msg="Error 1. Match in DB"
        logging.error(msg)
    else:
        if (a + 1) in database:
            msg="Error 2. Number is less by 1 than the processed one"
            logging.error(msg)
        else:
            database.append(a)
            msg = str(a + 1)
            insert_q = """INSERT INTO table1 (num) VALUES (%s)"""
            rec = (a, )
            cur.execute(insert_q, rec)
            conn.commit()
    return jsonify({"result": msg})
     
if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.ERROR)
    app.run(host='127.0.0.1', port=5000)
