import streamlit as st
import pandas as pd

st.subheader("Audit Logs")
df_logs = pd.read_sql("SELECT * FROM audit_logs ORDER BY timestamp DESC", conn)
st.dataframe(df_logs)
# In src/dashboard.py
if st.button("Update Role"):
    # You already have this logic
    update_user_role(user_id, new_role)
    st.success(f"User {user_id} updated to {new_role}!")
