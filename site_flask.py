import psycopg2
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def startpage():
    title = 'каталог магазина'
    conn = psycopg2.connect(dbname='test', user='postgres', password='4r5t2w1q', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM shop')
    all_data = cursor.fetchall()
    res_list = []
    for s in all_data:
        d1 = {"name": s[1], "price": s[2], "image": s[3]}
        res_list.append(d1)
    return render_template("catalog.html", title=title, res_list=res_list)

@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
