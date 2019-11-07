from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link,Description):
    """
    Add a student to the database, given
    their name, year, and whether they have
    finished the lab.
    """
    product_object = product(
        name=name,
        price=price,
        picture_link=picture_link,
        Description=Description)
    session.add(product_object)
    session.commit()

def edit_product(new_name,pid):

    student_object = session.query(
     Product).filter_by(
     id=pid ).first()
    student_object.name=new_name
    session.commit()

def delete_product(pid):
   """
   Delete all students with a
   certain name from the database.
   """
   session.query(product).filter_by(
       id=pid).delete()
   session.commit()

def query_all():
   """
   Print all the students
   in the database.
   """
   Products = session.query(
      product).all()
   return Products


print(query_all())

def query_by_id(pid):
   """
   Print all the students
   in the database.
   """
   Product = session.query(
      id=pid).filter_by(
      )
   return Product


print(query_all())


