# Ordering data

from models import engine, User
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)  # This is used to tell which database should be used for transactions.

session = Session()

# query all users ordered by age (ascending)
# users = session.query(User).order_by(User.age).all()
# for user in users:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# query all users ordered by age (descending)
# users = session.query(User).order_by(User.age.desc()).all()
# for user in users:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")

# query all users ordered by age and name
# users = session.query(User).order_by(User.age, User.name.desc()).all()
# for user in users:
#     print(f"user_id: {user.id}, user_name: {user.name}, user_age: {user.age}")


