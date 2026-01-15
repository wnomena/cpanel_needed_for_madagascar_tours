from flask import Flask, jsonify,make_response
import dotenv
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from Model.Setter_Method.insert_contact import Insert_Contact_Class
from Presenter.Getter_Method.Data_Modeliser_Before_Client import Modeliser_Class

dotenv.load_dotenv()
app = Flask(__name__)
user = os.getenv("user")
password = os.getenv("password")
database_name = os.getenv("database_name")
database_hosting = os.getenv("database_hosting")

engine = create_async_engine(f"mysql+aiomysql://{user}:{password}@{database_hosting}:3306/{database_name}")

getter_from_controller = Modeliser_Class(engine)
setter_for_contact = Insert_Contact_Class(engine)

@app.route("/")
def get_all_section():
    return jsonify({
        "circuit" : asyncio.run(getter_from_controller.Circuit_Modeliser()),
        "adrenaline" : asyncio.run(getter_from_controller.Adrenaline_Modeliser()),
        "itineraire" : asyncio.run(getter_from_controller.Itinerary_Modeliser()),
        "equipement" : asyncio.run(getter_from_controller.Equipement_Modeliser()),
        "included" : asyncio.run(getter_from_controller.Included_Modeliser())
    })

@app.route("/")
def add_contact():
    try:
        asyncio.run(setter_for_contact.Insert_Contact())
        return make_response("Votre données a bien été sauvegardé")
    except Exception as err:
        print(err)
        response = make_response("Queles chose s'est mal passé")
        response.status_code = 500
        return response


if __name__ == "__main__":
    app.run()