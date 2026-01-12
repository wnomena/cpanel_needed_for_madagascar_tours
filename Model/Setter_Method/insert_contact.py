from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert

from Model.Database_Model.flask_sqlalchemy import Contact_Model_without_Pydantic,Contact


class Insert_Contact_Class:
    def __init__(self,db:SQLAlchemy):
        self.db = db

    async def Insert_Contact(self,contact:Contact_Model_without_Pydantic):
        query = insert(Contact).values(Contact(name=contact.name,subject=contact.subject,body=contact.body,circuit_id=contact.circuit_id,number=contact.number,mail=contact.mail,begining=contact.begining,number_of_person=contact.number_of_person,total_price=contact.number_of_person*contact.number_of_person))
        await self.db.session.execute(query)
        await self.db.session.commit()
        