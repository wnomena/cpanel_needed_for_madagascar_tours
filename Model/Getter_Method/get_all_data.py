from concurrent.futures import ThreadPoolExecutor
from flask_sqlalchemy import SQLAlchemy
import asyncio
from sqlalchemy import select
from Model.Database_Model.flask_sqlalchemy import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model

class Instance_of_All_Data:
    circuit:list[Circuit_Model]
    adrenaline:list[Adrenaline_Model]
    itineraire:list[Itinerary_Model]
    equipement_needed:list[Equipement_Model]
    included:list[Included_task_in_Price_Model]
    def __init__(self,db:SQLAlchemy):
        self.db = db
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(asyncio.run,self.__Fetch_From_Database())
    

    async def __Fetch_From_Database(self):
        get_data_in_join = select(Circuit,Adrenaline,Itinerary,Equipement,Included_task_in_Price).outerjoin(Circuit.adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price)
        data_brute = await self.db.session.scalars(get_data_in_join).all()
        for circuit,adrenaline,itinerary,equipement,included in data_brute:
            await asyncio.to_thread(self.__Convert_Dict_Into_Class,circuit,adrenaline,itinerary,equipement,included)
        await asyncio.sleep(36)

    async def __Convert_Dict_Into_Class(self,circuit,adrenaline,itinerary,equipement,included):
        self.circuit.clear()
        self.adrenaline.clear()
        self.itineraire.clear()
        self.equipement_needed.clear()
        self.included.clear()
        circuit_dict = circuit.__dict__
        self.circuit.append(Circuit_Model(id=circuit_dict["id"],title=circuit_dict["title"],subtitle=circuit_dict["subtitle"],description=circuit_dict["description"],duration=circuit_dict["duration"],difficulty=circuit_dict["difficulty"],price=circuit_dict["price"],image=circuit_dict["image"]))
        adrenaline_dict = adrenaline.__dict__
        self.adrenaline.append(Adrenaline_Model(id=adrenaline_dict["id"],content=adrenaline_dict["content"],circuit_id=adrenaline_dict["circuit_id"]))
        itinerary_dict = itinerary.__dict__
        self.itineraire.append(Itinerary_Model(id=itinerary_dict["id"],place=itinerary_dict["place"],order_id=itinerary_dict["order_id"],circuit_id=itinerary_dict["circuit_id"]))
        equipement_dict = equipement.__dict__
        self.equipement_needed.append(Equipement_Model(id=equipement_dict["id"],equipment=equipement_dict["equipment"],circuit_id=equipement_dict["circuit_id"]))
        included_dict = included.__dict__
        self.included.append(Included_task_in_Price_Model(id=included_dict["id"],content=included_dict["content"],circuit_id=included_dict["circuit_id"]))