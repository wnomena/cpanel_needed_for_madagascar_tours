from sqlalchemy.ext.asyncio import AsyncEngine
from Model.Database_Model.flask_sqlalchemy import Adrenaline_Model, Circuit_Model, Equipement_Model, Itinerary_Model,Included_task_in_Price_Model
from Model.Getter_Method.get_all_data import Instance_of_All_Data
import asyncio
 
class Modeliser_Class(Instance_of_All_Data):
    __circuit_like_hash:list[Circuit_Model] = []
    __itinerary_like_hash:list[Itinerary_Model] = []
    __eqipement_like_hash:list[Equipement_Model] = []
    __included_in_price:list[Included_task_in_Price_Model] = []
    __adrenaline_like_hash:list[Adrenaline_Model] = []
    def __init__(self, db:AsyncEngine):
        super().__init__(db)

# traitement pour modeliser les données de adrenaline
    async def __For_Loop_For_Circuit(self,dataframe:Circuit_Model):
        if len(self.__circuit_like_hash) == 0:
            self.__circuit_like_hash.append(Circuit_Model(id=dataframe.id,title=dataframe.title,subtitle=dataframe.subtitle,description=dataframe.description,duration=dataframe.duration,difficulty=dataframe.difficulty,price=dataframe.price,image=dataframe.image))
        else:
            for key,element in enumerate(self.__circuit_like_hash):
                if element.id != dataframe.id and key == len(self.__circuit_like_hash) - 1:
                    await self.__circuit_like_hash.append(Circuit_Model(id=dataframe.id,title=dataframe.title,subtitle=dataframe.subtitle,description=dataframe.description,duration=dataframe.duration,difficulty=dataframe.difficulty,price=dataframe.price,image=dataframe.image))
        await asyncio.sleep(0)
    async def Circuit_Modeliser(self):
        for element in self.circuit:
            await self.__For_Loop_For_Circuit(element)
        return self.__circuit_like_hash
# traitement pour modeliser les données de circcuit
    async def __For_Loop_For_Adrenaline(self,dataframe:Adrenaline_Model):
        if len(self.__adrenaline_like_hash) == 0:
            self.__adrenaline_like_hash.append(Adrenaline_Model(id=dataframe.id,content=dataframe.content,circuit_id=dataframe.circuit_id))
        else:
            for key,element in enumerate(self.__adrenaline_like_hash):
                if element.id != dataframe.id and key == len(self.__adrenaline_like_hash) - 1:
                    await self.__adrenaline_like_hash.append(Adrenaline_Model(id=dataframe.id,content=dataframe.content,circuit_id=dataframe.circuit_id))
        await asyncio.sleep(0)
    async def Adrenaline_Modeliser(self):
        for element in self.adrenaline:
            await self.__For_Loop_For_Adrenaline(element)
        return self.__adrenaline_like_hash
#traitement pour les itineraires
    async def __For_Loop_For_Itinerary(self,dataframe:Itinerary_Model):
        if len(self.__itinerary_like_hash) == 0:
            self.__itinerary_like_hash.append(Itinerary_Model(id=dataframe.id,place=dataframe.place,order_id=dataframe.order_id,circuit_id=dataframe.circuit_id))
        else:
            for key,element in enumerate(self.__itinerary_like_hash):
                if element.id != dataframe.id and key == len(self.__itinerary_like_hash) - 1:
                    await self.__itinerary_like_hash.append(Itinerary_Model(id=dataframe.id,place=dataframe.place,order_id=dataframe.order_id,circuit_id=dataframe.circuit_id))
        await asyncio.sleep(0)
    async def Itinerary_Modeliser(self):
        for element in self.itineraire:
            await self.__For_Loop_For_Itinerary(element)
        return self.__itinerary_like_hash

#traitement pour les équipements

    async def __For_Loop_For_Equipement(self,dataframe:Equipement_Model):
        if len(self.__eqipement_like_hash) == 0:
            self.__eqipement_like_hash.append(Equipement_Model(id=dataframe.id,equipment=dataframe.equipment,circuit_id=dataframe.circuit_id))
        else:
            for key,element in enumerate(self.__eqipement_like_hash):
                if element.id != dataframe.id and key == len(self.__eqipement_like_hash) - 1:
                    await self.__eqipement_like_hash.append(Equipement_Model(id=dataframe.id,equipment=dataframe.equipment,circuit_id=dataframe.circuit_id))
        await asyncio.sleep(0)
    async def Equipement_Modeliser(self):
        for element in self.equipement_needed:
            await self.__For_Loop_For_Equipement(element)
        return self.__eqipement_like_hash
#traitement de included in price
    async def __For_Loop_For_Included(self,dataframe:Included_task_in_Price_Model):
        if len(self.__included_in_price) == 0:
            self.__included_in_price.append(Included_task_in_Price_Model(id=dataframe.id,content=dataframe.content,circuit_id=dataframe.circuit_id))
        else:
            for key,element in enumerate(self.__included_in_price):
                if element.id != dataframe.id and key == len(self.__included_in_price) - 1:
                    await self.__included_in_price.append(Included_task_in_Price_Model(id=dataframe.id,content=dataframe.content,circuit_id=dataframe.circuit_id))
        await asyncio.sleep(0)
    async def Included_Modeliser(self):
        for element in self.adrenaline:
            await self.__For_Loop_For_Included(element)
        return self.__included_in_price