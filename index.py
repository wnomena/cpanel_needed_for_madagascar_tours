from flask import Flask
from Model.Database_Model.flask_sqlalchemy import db
import dotenv
import asyncio
import os

from Presenter.Getter_Method.Data_Modeliser_Before_Client import Modeliser_Class

dotenv.load_dotenv()
app = Flask(__name__)
user = os.getenv("user")
password = os.getenv("password")
database_name = os.getenv("database_name")
database_hosting = os.getenv("database_hosting")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+aiomysql://{user}:{password}@{database_hosting}:3306/{database_name}"
db.init_app(app=app)

getter_from_controller = Modeliser_Class(db)

@app.route("/")
def get_all_section():
    return {
        "circuit" : asyncio.run(getter_from_controller.Circuit_Modeliser),
        "itineraire" : asyncio.run(getter_from_controller.Itinerary_Modeliser),
        "equipement" : asyncio.run(getter_from_controller.Equipment_Modeliser),
        "included" : asyncio.run(getter_from_controller.included)
    }

if __name__ == "__main__":
    app.run()