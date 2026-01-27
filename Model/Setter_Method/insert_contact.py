from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncEngine,async_sessionmaker
from sqlalchemy.orm import Session

from Model.Database_Model.flask_sqlalchemy import Contact_Model_without_Pydantic,Contact
class Insert_Contact_Class:
    def __init__(self,db:AsyncEngine):
        self.async_session = async_sessionmaker(db,expire_on_commit=False)

    async def Insert_Contact(self,contact:Contact_Model_without_Pydantic):
        async with self.async_session() as session:
            query = insert(Contact).values(name=contact.name,subject=contact.subject,body=contact.body,circuit_id=contact.circuit_id,number=contact.number,mail=contact.mail,begining=contact.begining,number_of_person=contact.number_of_person,total_price=contact.total_price)
            async with session.begin():
                await session.execute(query)
                await session.commit()