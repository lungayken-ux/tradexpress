# Conceptual SQL for your database initialization
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        user_id TEXT,
        action TEXT,
        table_affected TEXT,
        old_value TEXT,
        new_value TEXT
    )
''')
def log_action(user_id, action, table, old_val=None, new_val=None):
    """Logs a system action to the audit_logs table."""
    conn = get_db_connection() # Assuming you have a connection helper
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO audit_logs (user_id, action, table_affected, old_value, new_value)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, action, table, str(old_val), str(new_val)))
    conn.commit()
    conn.close()
# Inside your update user role logic:
old_role = get_user_role(user_id)
update_user_role(user_id, new_role)
log_action(admin_id, "UPDATE_ROLE", "users", old_val=old_role, new_val=new_role)
