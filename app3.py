# group by

from models import engine, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

Session = sessionmaker(bind=engine)  # This is used to tell which database should be used for transactions.

session = Session()

# count number of users in different age group.
users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(users)
