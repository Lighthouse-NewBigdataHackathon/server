import re
import pymysql
import db
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

with open("../db_data.pickle", 'rb') as f:
    db_data = pickle.load(f)
conn, cursor = db.connect_RDS(db_data["host"], db_data["port"], db_data["username"], db_data["password"], db_data["database"])

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/articles', methods=['GET'])
def today():
    if request.method == 'GET':   #데이터를 받아야 아래 코드를 더 짤수 있을듯 하네용.. 우선은 articles로 넘어가짐
        date='2022-09-30'
        q = db.select_with_date(date)
        cursor.execute(q)
        result = list(cursor.fetchall())
        for r in range(len(result)):
            result[r] = list(result[r])
            result[r][4]="https://www.bigkinds.or.kr/resources/images"+result[r][4]
        # print(result)
        return render_template("articles.html", articles=result)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
