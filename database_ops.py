# In src/database_ops.py
from src.logger import log_action # Import the logger we designed

def get_current_role(user_id):
    """Fetches the current role to support audit logging."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "unknown"    
    # 2. Perform your existing update
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, user_id))
    conn.commit()
    
    # 3. Log the audit entry
    log_action("admin", "UPDATE_ROLE", "users", old_role, new_role)
