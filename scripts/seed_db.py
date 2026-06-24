from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///wellken.db")
metadata = MetaData()

# Define a simple table
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('role', String)
)

# Create the table and add dummy data
metadata.create_all(engine)
with engine.connect() as conn:
    conn.execute(users.insert(), [
        {'name': 'Kenny', 'role': 'Developer'},
        {'name': 'System', 'role': 'Admin'}
    ])
    conn.commit()

print("Database seeded successfully!")
