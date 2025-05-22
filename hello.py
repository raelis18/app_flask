from flask import Flask
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

db_user = str(os.getenv("db_user"))
db_password = str(os.getenv("db_password"))
app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            port=3306,
            user=db_user,
            password=db_password,
            database="app_flask"
        )
        mycursor = mydb.cursor()
        #mycursor.execute("show databases")
        mycursor.close()
        mydb.close()
        return "<p>Banco de dados conectado</p>"
    except Error as e:
        return f"<p>Erro ao conectar ao banco de dados: {e}</p>"
