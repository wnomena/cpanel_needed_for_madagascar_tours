from Model.Database_Model.flask_sqlalchemy import Circuit_Model, Itinerary_Model
from Model.Getter_Method.get_all_data import Instance_of_All_Data
import asyncio
import pandas as pd
 
class Modeliser_Class(Instance_of_All_Data):
    circuit_like_hash:list[Circuit_Model]
    itinerary_like_hash:list[Itinerary_Model]
    def __init__(self, db):
        super().__init__(db)
# traitement pour modeliser les données de circcuit
    async def For_Loop_For_Circuit(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.circuit_like_hash.append(Circuit_Model(id=rows["id"],title=rows["title"],subtitle=rows["subtitle"],description=rows["description"],duration=rows["duration"],difficulty=rows["difficulty"],price=rows["price"],image=rows["image"])))
    async def Circuit_Modeliser(self):
        data = pd.DataFrame(self.circuit).drop_duplicates()
        await self.For_Loop_For_Circuit(data)
        return self.circuit_like_hash

#traitement pour les itineraires

    async def For_Loop_For_Itinerary(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.circuit_like_hash.append(Itinerary_Model(id=rows["id"],place=rows["place"],order_id=rows["order_id"],circuit_id=rows["circuit_id"])))
    

    async def Itinerary_Modeliser(self):
        data = pd.DataFrame(self.itineraire).drop_duplicates()
        await self.For_Loop_For_Itinerary(data)

