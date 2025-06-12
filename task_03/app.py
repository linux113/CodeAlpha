from flask import Flask, request, redirect, render_template, session
from werkzeug.security import check_password_hash
import sqlite3
import os
from dotenv import load_dotenv

# Load secret key from environment
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
        result = cursor.fetchone()
        if result and check_password_hash(result['password'], pwd):
            session.clear()
            session['user'] = user
            return redirect('/dashboard')
        else:
            return "Invalid credentials"
    return render_template('login.html')
