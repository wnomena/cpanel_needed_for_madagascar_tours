from flask import Flask
from Model.Database_Model.flask_sqlalchemy import db
import dotenv
import os

dotenv.load_dotenv()
app = Flask(__name__)
user = os.getenv("user")
password = os.getenv("password")
database_name = os.getenv("database_name")
database_hosting = os.getenv("database_hosting")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{database_hosting}:3306/{database_name}"
db.init_app(app=app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()