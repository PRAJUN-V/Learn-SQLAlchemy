# Filter on data

from models import engine, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)  # This is used to tell which database should be used for transactions.

session = Session()

# # query all users
# users_all = session.query(User).all()

# # query all the users with age greater than or equal to 25
# users_filtered = session.query(User).filter(User.age >= 25).all()
# for user in users_filtered:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# # query all the users with age greater less than 25 and name = "Prajun v"
# users_filtered = session.query(User).filter(User.age < 25, User.name == "Prajun v").all()
# for user in users_filtered:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# # filter using where()
# users_filtered = session.query(User).where(User.age < 25, User.name == "Prajun v").all()
# for user in users_filtered:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# # implement 'or' condition in filter
# # query all the users with age greater less than 25 or name = "Biju V"
# users_filtered = session.query(User).filter(or_(User.age < 25, User.name == "Biju V")).all()
# for user in users_filtered:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# # Another method to implement 'or' in filter
# # query all the users with age greater less than 25 or name = "Biju V"
# users_filtered = session.query(User).filter((User.age < 25) | (User.name == "Biju V")).all() # | for or and & for and
# for user in users_filtered:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# and, or and not can be used in a single filter query for creating complex filter.
