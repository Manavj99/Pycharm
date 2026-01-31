# import sqlite3 as sq
# conn = sq.connect("test.db")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

# cursor.execute("INSERT INTO users VALUES (1, 'Manav')")
# cursor.execute("INSERT INTO users VALUES (2, 'John')")
# cursor.execute("INSERT INTO users VALUES (3, 'Jane')")
# cursor.execute("INSERT INTO users VALUES (4, 'Jim')")
# cursor.execute("INSERT INTO users VALUES (5, 'Jill')")

# conn.commit()
# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
# conn.close()

# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker

# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# engine = create_engine('sqlite:///sqlalchemy.db')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# new_user = User(name='Alice')
# session.add(new_user)
# session.commit()

# def repr(self):
#         return f"<User(id={self.id}, name='{self.name}')>"
# print(session.query(User.id, User.name).all())

# def new_user(name):
#     new_user = User(name=name)
#     session.add(new_user)
#     session.commit()
#     return new_user
# new_user("Alan")
# new_user("Bob")
# new_user("Charlie")
# print(session.query(User.id, User.name).all())


# name=['a','b','c','d']
# for name in name:
#     new_user(name)
# print(session.query(User.id, User.name).all())



# import pandas as pd
# import sqlite3 as sq
# conn = sq.connect("sqlalchemy.db")
# df = pd.read_sql_query("SELECT * FROM users", conn)
# print(df)


from sqlalchemy import create_engine, MetaData, Table, select

# Database credentials
db_user = ""
db_password = ""
db_host = ""          # or your server host
db_port = ""
db_name = ""

# Connection string
DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create MetaData object to reflect existing tables
metadata = MetaData()
metadata.reflect(bind=engine, schema="endeavour")  # automatically loads existing tables

# Access an existing table, e.g., 'students'
stocks = metadata.tables['endeavour.stocks_lookup']

# Query data
with engine.connect() as conn:
    result = conn.execute(select(stocks))
    for row in result:
        print(row)



