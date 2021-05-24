import mysql.connector as mysql
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
HOST = 'sql6.freesqldatabase.com'
USER = 'sql6412984'
PW = 'EUxK6p6ciM'
DB = 'sql6412984'

engine = mysql.connect(host=HOST, database=DB, user=USER, password=PW)
cur = engine.cursor(buffered=True)


@app.route("/")
def home_view():
    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()
    return jsonify(rows)


@app.route("/data")
def index():
    cur.execute("select * from test")
    nm = cur.fetchall()
    rs = cur.column_names
    return render_template('data.html', nm=nm, rs=rs)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        mob = request.form['mob']
        cur.execute(''' INSERT INTO test(name, mob) VALUES(%s,%s)''', (name, mob))
        engine.commit()
        cur.close()
        return f"Submitted Successfully"


cur.close()
