from flask import Flask

app = Flask(__name__)
app.secret_key= "Stay Safe"
DATABASE = "recipes_schema"