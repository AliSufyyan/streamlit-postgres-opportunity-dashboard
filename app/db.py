# app/db.py
# WHY: Centralizes database connection so we don't repeat connection code everywhere.
# Uses SQLAlchemy engine with psycopg2 as the driver.
# st.cache_resource means Streamlit creates the connection ONCE and reuses it.

import os
import streamlit as st
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()  # Load .env file if it exists (for local dev)

def get_connection_string():
    host     = os.getenv("DB_HOST", "localhost")
    port     = os.getenv("DB_PORT", "5432")
    dbname   = os.getenv("DB_NAME", "student_opportunities_db")
    user     = os.getenv("DB_USER", "app_user")
    password = os.getenv("DB_PASSWORD", "app_password")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

@st.cache_resource
def get_engine():
    """Create and cache the SQLAlchemy engine."""
    return create_engine(get_connection_string())

def test_connection():
    """Returns (True, version_string) or (False, error_message)."""
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
        return True, version
    except Exception as e:
        return False, str(e)