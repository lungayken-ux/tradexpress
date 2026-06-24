import sqlite3
import datetime

# Centralized location for your DB path
DB_PATH = 'wellken.db'

def log_action(user_id, action, table, old_value=None, new_value=None):
    """
    Centralized controller for audit logging.
    Call this from any route or database function.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO audit_logs (timestamp, user_id, action, table_affected, old_value, new_value)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (datetime.datetime.now(), user_id, action, table, str(old_value), str(new_value)))
            conn.commit()
    except Exception as e:
        print(f"Logging failed: {e}")

def get_recent_logs(limit=50):
    """Retrieve logs for your dashboard."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT ?', (limit,))
        return cursor.fetchall()
