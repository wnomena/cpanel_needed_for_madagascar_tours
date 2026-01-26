from flask import Flask, jsonify,make_response,request
import dotenv
import asyncio
import os
from flask_cors import CORS
from sqlalchemy.ext.asyncio import create_async_engine
from Model.Setter_Method.insert_contact import Insert_Contact_Class
from Presenter.Getter_Method.Data_Modeliser_Before_Client import Modeliser_Class
from Model.Database_Model.flask_sqlalchemy import Circuit_Model,Adrenaline_Model, Itinerary_Model,Equipement_Model,Included_task_in_Price_Model,Contact_Model_without_Pydantic
from itertools import zip_longest

dotenv.load_dotenv()
app = Flask(__name__)
CORS(app, supports_credentials=True)
user = os.getenv("user")
password = os.getenv("password")
database_name = os.getenv("database_name")
database_hosting = os.getenv("database_hosting")

engine = create_async_engine(f"mysql+aiomysql://{user}:{password}@{database_hosting}:3306/{database_name}")

getter_from_controller = Modeliser_Class(engine)
setter_for_contact = Insert_Contact_Class(engine)

@app.route("/")
def get_all_section():
    circuit:list[dict] = []
    adrenaline :list[dict] = []
    itineraire:list[dict] = []
    equipement:list[dict] = []
    included :list[dict] = []
    for loop_circuit, loop_adrenaline, loop_itineraire, loop_equipement, loop_included in zip_longest(asyncio.run(getter_from_controller.Circuit_Modeliser()),asyncio.run(getter_from_controller.Adrenaline_Modeliser()),asyncio.run(getter_from_controller.Itinerary_Modeliser()),asyncio.run(getter_from_controller.Equipement_Modeliser()),asyncio.run(getter_from_controller.Included_Modeliser()),fillvalue=0):
        if loop_circuit:
            circuit.append(loop_circuit.to_dict())
        if loop_adrenaline:
            adrenaline.append(loop_adrenaline.to_dict())
        if loop_itineraire:
            itineraire.append(loop_itineraire.to_dict())
        if loop_equipement:
            equipement.append(loop_equipement.to_dict())
        if loop_included:
            included.append(loop_included.to_dict())
    return jsonify({
        "code" : 1,
        "error" : "",
        "data" : {
        "circuit" : circuit,
        "adrenaline" : adrenaline,
        "itinerary" : itineraire,
        "equipment" : equipement,
        "included_in_price" : included
    }})

@app.route("/",methods=["POST"])
def add_contact():
    data = request.form
    temp:Contact_Model_without_Pydantic = None
    if data.get("subjet"):
        temp = Contact_Model_without_Pydantic(name=data.get("name"),subject=data.get("subject"),body=data.get("body"),number=data.get("number"),begining=data.get("begining"),number_of_person=data.get("number_of_person"),circuit_id=data.get("circuit_id"))
    else:
        temp = Contact_Model_without_Pydantic(name=data.get("name"),body=data.get("body"),mail=data.get("mail"))
    try:
        asyncio.run(setter_for_contact.Insert_Contact(temp))
        return make_response("Votre données a bien été sauvegardé")
    except Exception as err:
        print(err)
        response = make_response("Queles chose s'est mal passé")
        response.status_code = 500
        return response

if __name__ == "__main__":
    app.run()