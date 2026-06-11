# app/auth.py
# WHY: Provides a simple two-role login (Admin / Viewer) using st.session_state.
# No real database auth — just hardcoded for this assignment demo.

import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "viewer": {"password": "view123",  "role": "Viewer"},
}

def login_page():
    st.title("🔐 Login")
    st.markdown("Please log in to access the dashboard.")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            user = USERS.get(username)
            if user and user["password"] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["role"] = user["role"]
                st.success(f"Welcome, {username}! Role: {user['role']}")
                st.rerun()
            else:
                st.error("Invalid username or password.")

def require_admin():
    """Call at top of Admin-only pages."""
    if st.session_state.get("role") != "Admin":
        st.error("⛔ This page requires Admin access.")
        st.stop()

def logout():
    for key in ["logged_in", "username", "role"]:
        st.session_state.pop(key, None)
    st.rerun()