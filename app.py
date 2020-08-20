#Flaskからimportしてflaskを使えるようにする
from flask import Flask,render_template,request,session,redirect
import sqlite3
 
#appっていう名前でFlaskアプリをつくっていくよ～みみたいな
app  = Flask(__name__)

# session利用時にはシークレットキーが必要
app.secret_key = 'kamaki0721'

@app.route("/index")
def index():
    conn = sqlite3.connect("hougen.db")
    c = conn.cursor()
    #課題１ スタッフの誰か一名 （誰でも可）情報を取得するSQL
    c.execute('SELECT word,mean from hougen')
    hougen = c.fetchone()
    c.close()
    print(hougen)

    #課題２ スタッフの誰か一名（誰でも可）情報を表示するHTMLを作成し表示
    return render_template("index.html",kotoba=hougen[0],imi=hougen[1])











if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)
