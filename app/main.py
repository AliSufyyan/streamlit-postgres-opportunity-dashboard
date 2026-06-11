# app/main.py
# WHY: This is the file Streamlit runs first.
# It handles login, sidebar navigation, and the Home page content.

import streamlit as st
from app.auth import login_page, logout

st.set_page_config(
    page_title="Internship & Job Tracker",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Authentication gate ──────────────────────────────────────────────────────
if not st.session_state.get("logged_in"):
    login_page()
    st.stop()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"**User:** {st.session_state.get('username')}  \n**Role:** {st.session_state.get('role')}")
    if st.button("Logout"):
        logout()
    st.divider()
    st.markdown("### Navigation")
    st.markdown("Use the pages menu above ↑ to navigate.")

# ── Home page content ─────────────────────────────────────────────────────────
st.title("💼 Internship & Job Tracking Dashboard")
st.markdown("### University of Central Punjab — Faculty of IT & CS")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("📋 About This App")
    st.markdown("""
    This dashboard helps faculty manage student internship and job opportunities.
    
    **Features:**
    - Add, view, update, and delete opportunities
    - Upload bulk data via CSV
    - View analytics and KPIs
    - Detect duplicate entries
    - Monitor application deadlines
    - Role-based access (Admin / Viewer)
    """)

with col2:
    st.subheader("🛠️ Technology Stack")
    st.markdown("""
    | Component | Technology |
    |-----------|------------|
    | Frontend  | Streamlit  |
    | Database  | PostgreSQL |
    | DB Admin  | pgAdmin 4  |
    | Containers | Docker Compose |
    | ORM / Driver | SQLAlchemy + psycopg2 |
    | Charts    | Plotly     |
    """)

st.divider()
st.subheader("👥 Team Members")
st.markdown("""
| Member | Role | GitHub |
|--------|------|--------|
| Member 1 | Database & Docker | @username1 |
| Member 2 | Streamlit UI      | @username2 |
| Member 3 | Analytics & Report | @username3 |
""")

st.subheader("🏗️ System Architecture")
st.code("""
Browser → Streamlit App (port 8501)
              ↓
    PostgreSQL DB (port 5432)  ←→  pgAdmin (port 5050)
              ↓
     Docker Volume (persistent storage)
""")