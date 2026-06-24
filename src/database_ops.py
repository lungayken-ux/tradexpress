from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///wellken.db")

def fetch_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        return result.fetchall()

def update_user_role(user_id, new_role):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE users SET role = :role WHERE id = :id"),
            {"role": new_role, "id": user_id}
        )
        conn.commit()
