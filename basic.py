from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='khushi1234',
        database='your_database_name'
    )
    return conn

@app.route('/')
def home():
    return render_template('login.html')  # Update to your HTML file name

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    email = request.form['email']

    # Insert the name and email into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO your_table (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()

    cursor.close()
    conn.close()

    return 'Successfully logged in!'

if __name__ == '__main__':
    app.run(debug=True)
