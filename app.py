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
    c.execute('SELECT word,mean from hougen join category on hougen.category_id=category.id where hougen.category_id=1')
    # hougen_1 = c.fetchone()

    hougen_list_1 = []
    for row in c.fetchall():
        hougen_list_1.append({"word":row[0],"mean":row[1]})

 
    # print(hougen_list_1[0]
    # print(hougen_list_1[1]
    # print(hougen_list_1[2]
    # print(hougen_list_1[3]
    # print(hougen_list_1[4]


    c.execute('SELECT word,mean from hougen join category on hougen.category_id=category.id where hougen.category_id=2')
    # hougen_2 = c.fetchone()

    hougen_list_2 = []
    for row in c.fetchall():
        hougen_list_2.append({"word":row[0],"mean":row[1]})

    # print(hougen_list_2[0]
    # print(hougen_list_2[1]
    # print(hougen_list_2[2]
    # print(hougen_list_2[3]
    # print(hougen_list_2[4]

    c.execute('SELECT word,mean from hougen join category on hougen.category_id=category.id where hougen.category_id=3')
    # hougen_3 = c.fetchone()

    hougen_list_3 = []
    for row in c.fetchall():
        hougen_list_3.append({"word":row[0],"mean":row[1]})

    c.execute('SELECT word,mean from hougen join category on hougen.category_id=category.id where hougen.category_id=4')
    # hougen_4 = c.fetchone()

    hougen_list_4 = []
    for row in c.fetchall():
        hougen_list_4.append({"word":row[0],"mean":row[1]})

    c.close()
    # print(hougen_1)
    # print(hougen_2)
    # print(hougen_3)
    # print(hougen_4)


    #課題２ スタッフの誰か一名（誰でも可）情報を表示するHTMLを作成し表示
    return render_template("index.html",hougen_list_1=hougen_list_1[0])

    # return render_template("index.html",word_1=hougen_1[0],
    #                                     mean_1=hougen_1[1],
    #                                     word_2=hougen_2[0],
    #                                     mean_2=hougen_2[1],
    #                                     word_3=hougen_3[0],
    #                                     mean_3=hougen_3[1],
    #                                     word_4=hougen_4[0],
    #                                     mean_4=hougen_4[1])
                        











if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)
