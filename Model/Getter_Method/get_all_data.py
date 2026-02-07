import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker,AsyncEngine
from Model.Database_Model.flask_sqlalchemy import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model

class Instance_of_All_Data:
    circuit:list[Circuit_Model] = []
    adrenaline:list[Adrenaline_Model]  = []
    itineraire:list[Itinerary_Model] = []
    equipement_needed:list[Equipement_Model] = []
    included:list[Included_task_in_Price_Model] = []
    def __init__(self,db:AsyncEngine):
        self.async_session = async_sessionmaker(db,expire_on_commit=False)
        asyncio.run(self.__Fetch_From_Database())
    

    async def __Fetch_From_Database(self):
        self.circuit = []
        self.adrenaline = []
        self.itineraire = []
        self.included = []
        self.equipement_needed = []
        async with self.async_session() as session:
            get_data_in_join = select(Circuit,Adrenaline,Itinerary,Equipement,Included_task_in_Price).outerjoin(Circuit.adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price)
            data_brute = await session.execute(get_data_in_join)
            for row in data_brute:
                await self.__Convert_Dict_Into_Class(row[0],row[1],row[2],row[3],row[4])
            await session.close()
 
    async def __Convert_Dict_Into_Class(self,circuit:Circuit_Model,adrenaline:Adrenaline_Model,itinerary:Itinerary_Model,equipement:Equipement_Model,included:Included_task_in_Price_Model):
        
        self.circuit.append(Circuit_Model(id=circuit.id,title=circuit.title,subtitle=circuit.subtitle,description=circuit.description,duration=circuit.duration,difficulty=circuit.difficulty,price=circuit.price,image=circuit.image))
        self.adrenaline.append(Adrenaline_Model(id=adrenaline.id,content=adrenaline.content,circuit_id=adrenaline.circuit_id))
        self.itineraire.append(Itinerary_Model(id=itinerary.id,place=itinerary.place,order_id=itinerary.order_id,circuit_id=itinerary.circuit_id))
        self.equipement_needed.append(Equipement_Model(id=equipement.id,equipment=equipement.equipment,circuit_id=equipement.circuit_id))
        self.included.append(Included_task_in_Price_Model(id=included.id,content=included.content,circuit_id=included.circuit_id))
        await asyncio.sleep(0)