import streamlit as st
import pandas as pd
from database_ops import fetch_users, update_user_role

st.title("Wellken Admin")

menu = st.sidebar.radio("Navigation", ["View Data", "Manage Roles"])

if menu == "View Data":
    # Just call the function!
    data = fetch_users()
    df = pd.DataFrame(data, columns=['id', 'name', 'role'])
    st.dataframe(df)

elif menu == "Manage Roles":
    st.subheader("Update User Role")
    
    # Define the inputs
    user_id = st.number_input("User ID", min_value=1, step=1)
    new_role = st.text_input("New Role")
    
    # Perform the update ONLY when the button is clicked
    if st.button("Update"):
        # The variables user_id and new_role are used safely here
        update_user_role(user_id, new_role)
        st.success(f"User {user_id} updated to {new_role}!")
        st.rerun()
