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
    c.execute('SELECT word from hougen join category on hougen.category_id=category.id where hougen.category_id=1')
    hougen_list_1 =[]
    for row in c.fetchall():
        hougen_list_1.append(row[0])
    print(hougen_list_1)
    # hougen_1 = c.fetchone()
    # hougen_list_1 = c.fetchall()
    # for row in c.fetchone():
    #     hougen_list_1.append({row[0],row[1]})

    c.execute('SELECT mean from hougen join category on hougen.category_id=category.id where hougen.category_id=1')
    mean_1 =[]
    for row in c.fetchall():
        mean_1.append(row[0])
    print(mean_1)
    # mean_1 = c.fetchall()

    c.execute('SELECT word from hougen join category on hougen.category_id=category.id where hougen.category_id=2')
    hougen_list_2 =[]
    for row in c.fetchall():
        hougen_list_2.append(row[0])
    print(hougen_list_2)
    # hougen_2 = c.fetchone()
    c.execute('SELECT mean from hougen join category on hougen.category_id=category.id where hougen.category_id=2')
    mean_2 =[]
    for row in c.fetchall():
        mean_2.append(row[0])

    # hougen_list_2 = c.fetchone()
    # for row in c.fetchall():
    #     hougen_list_2.append({row[0],row[1]})

    c.execute('SELECT word from hougen join category on hougen.category_id=category.id where hougen.category_id=3')
    hougen_list_3 =[]
    for row in c.fetchall():
        hougen_list_3.append(row[0])
    print(hougen_list_3)
    # hougen_3 = c.fetchone()
    c.execute('SELECT mean from hougen join category on hougen.category_id=category.id where hougen.category_id=3')
    mean_3 =[]
    for row in c.fetchall():
        mean_3.append(row[0])


    # hougen_list_3 = c.fetchone()
    # for row in c.fetchall():
    #     hougen_list_3.append({row[0],row[1]})

    c.execute('SELECT word from hougen join category on hougen.category_id=category.id where hougen.category_id=4')
    hougen_list_4 =[]
    for row in c.fetchall():
        hougen_list_4.append(row[0])
    print(hougen_list_4)
    # hougen_4 = c.fetchone()
    c.execute('SELECT mean from hougen join category on hougen.category_id=category.id where hougen.category_id=4')
    mean_4 =[]
    for row in c.fetchall():
        mean_4.append(row[0])

    # hougen_list_4 = c.fetchone()
    # for row in c.fetchall():
    #     hougen_list_4.append({row[0],row[1]})
    c.close()
    
    return render_template("index.html",
    hougen_list_1=hougen_list_1,mean_1=mean_1,
    # hougen_list_1=hougen_list_1[1],mean_1=mean_1[1],

    
    hougen_list_2=hougen_list_2,mean_2=mean_2,
    hougen_list_3=hougen_list_3,mean_3=mean_3,
    hougen_list_4=hougen_list_4,mean_4=mean_4)
                                        
    
    # return render_template("index.html",word_1=hougen_1[0],
    #                                     mean_1=hougen_1[1],
    #                                     word_2=hougen_2[0],
    #                                     mean_2=hougen_2[1],
    #                                     word_3=hougen_3[0],
    #                                     mean_3=hougen_3[1],
    #                                     word_4=hougen_4[0],
    #                                     mean_4=hougen_4[1])
                        
@app.route("/edit")
def edit():
    conn = sqlite3.connect('hougen.db')
    c = conn.cursor()

    c.execute('SELECT category_id,word,mean from hougen')
    edit = []

    for row in c.fetchall():
        edit.append({"category_id":row[0],"word":row[1],"mean":row[2]})
    c.close()
    print(edit) 


    return render_template("edit.html",edit=edit) 


@app.route("/add",methods=["GET"])
def add_get():
    return render_template("edit.html")

@app.route("/add",methods=["POST"])
def add_post():
    category_id=request.form.get("category_id")
    word=request.form.get("hougen")
    mean=request.form.get("mean")
    conn = sqlite3.connect('hougen.db')
    c = conn.cursor()

    c.execute('insert into hougen values(null,?,?,?)',(category_id,word,mean))
    conn.commit()
    conn.close()
    print(edit)


    return redirect("/index") 

    # 削除機能追加
@app.route("/delete/<int:id>")
def delete_(id):
    conn = sqlite3.connect("hougen.db")  #データベースに接続
    c = conn.cursor()
    c.execute('delete from task where id = ?',(id,))
    conn.commit() 
    conn.close
    return redirect("/task_list")










if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)
