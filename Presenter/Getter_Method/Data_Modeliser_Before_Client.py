from Model.Database_Model.flask_sqlalchemy import Circuit_Model, Equipement_Model, Itinerary_Model,Included_task_in_Price_Model
from Model.Getter_Method.get_all_data import Instance_of_All_Data
import asyncio
import pandas as pd
 
class Modeliser_Class(Instance_of_All_Data):
    __circuit_like_hash:list[Circuit_Model]
    __itinerary_like_hash:list[Itinerary_Model]
    __eqipement_like_hash:list[Equipement_Model]
    __included_in_price:list[Included_task_in_Price_Model]
    def __init__(self, db):
        super().__init__(db)
# traitement pour modeliser les données de circcuit
    async def __For_Loop_For_Circuit(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.__circuit_like_hash.append,Circuit_Model(id=rows["id"],title=rows["title"],subtitle=rows["subtitle"],description=rows["description"],duration=rows["duration"],difficulty=rows["difficulty"],price=rows["price"],image=rows["image"]))
    async def Circuit_Modeliser(self):
        data = pd.DataFrame(self.circuit).drop_duplicates()
        await self.__For_Loop_For_Circuit(data)
        return self.__circuit_like_hash

#traitement pour les itineraires
    async def __For_Loop_For_Itinerary(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.__itinerary_like_hash.append,Itinerary_Model(id=rows["id"],place=rows["place"],order_id=rows["order_id"],circuit_id=rows["circuit_id"]))
    

    async def Itinerary_Modeliser(self):
        data = pd.DataFrame(self.itineraire).drop_duplicates()
        await self.__For_Loop_For_Itinerary(data)
        return self.__itinerary_like_hash

#traitement pour les équipements

    async def __For_Loop_For_Equipement(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.__eqipement_like_hash.append,Equipement_Model(id=rows["id"],equipment=rows["equipment"],circuit_id=rows["circuit_id"]))

    async def Equipment_Modeliser(self):
        data = pd.DataFrame(self.equipement_needed).drop_duplicates()
        await self.__For_Loop_For_Equipement(data)
        return self.__eqipement_like_hash
    
#traitement de included in price

    async def __For_Loop_For_Included(self,dataframe:pd.DataFrame):
        for index,rows in dataframe.iterrows():
            await asyncio.to_thread(self.__included_in_price.append,Included_task_in_Price_Model(id=rows["id"],content=rows["content"],circuit_id=rows["circuit_id"]))

    async def Included_Modeliser(self):
        data = pd.DataFrame(self.included).drop_duplicates()
        await self.__For_Loop_For_Included(data)
        return self.__eqipement_like_hash