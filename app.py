# CRUD operations

from models import engine, User
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)  # This is used to tell which database should be used for transactions.

session = Session()

# # inserted a data into the user table.
# user1 = User(name="Prajun v", age=25)
# session.add(user1)
# session.commit() # To commit the changes to the database.

# # insert multiple data into the user table at a time.
# user2 = User(name="Arjun V", age=25)
# user3 = User(name="Biju V", age=52)
# user4 = User(name="Preeja V", age=42)
# user5 = User(name="Theja Lakshmi V", age=17)
# session.add_all([user2, user3, user4, user5])
# session.commit()

# To retrieve all the data from user table.
# users = session.query(User).all()
# for user in users:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# To retrieve data from user table based on filter conditions.
# users = session.query(User).filter_by(id=1).all()
# for user in users:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# user = session.query(User).filter_by(id=1).one_or_none() # It will either return one object that satisfies the condition else return None.
# print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# user = session.query(User).filter_by(id=1).first() # It will return the first object that satisfies the condition.
# print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# Update the data in user table.
# user = session.query(User).filter_by(id=1).first()
# user.age = 23
# session.commit()

# Deleting the data in user table.
# user = session.query(User).filter_by(id=2).first()
# session.delete(user)
# session.commit()
