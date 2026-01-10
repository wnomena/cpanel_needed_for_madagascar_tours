from flask_sqlalchemy import SQLAlchemy
from Model.Database_Model.flask_sqlalchemy import Adrenaline_Model, Circuit, Circuit_Model, Equipement_Model, Included_task_in_Price_Model, Itinerary_Model


class Get_All_Data_Class:
    circuit:list[Circuit_Model]
    adrenaline:list[Adrenaline_Model]
    itineraire:list[Itinerary_Model]
    equipement_needed:list[Equipement_Model]
    included:list[Included_task_in_Price_Model]
    def __init__(self,db:SQLAlchemy):
        self.db = db
    

    def Fetch_From_Database():
        pass

    