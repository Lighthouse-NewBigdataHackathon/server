import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/articles', methods=['GET'])
def today():
    if request.method == 'GET':   #데이터를 받아야 아래 코드를 더 짤수 있을듯 하네용.. 우선은 articles로 넘어가짐
        return render_template("articles.html")


    
if __name__ == '__main__':
    app.run()