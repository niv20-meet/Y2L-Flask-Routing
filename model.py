from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class product(Base):
   __tablename__ = 'product'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   picture_link = Column(String)
   Description = Column(String)

class cart(Base):
	id=Column(Integer,primary_key=True)
	pid=Column(Integer)