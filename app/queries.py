# app/queries.py
# WHY: All SQL is in one file. This separates business logic from UI code.
# If you need to fix a query, you know exactly where to look.

import pandas as pd
from sqlalchemy import text
from app.db import get_engine

def get_all_opportunities():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM opportunities ORDER BY created_at DESC", engine)

def get_opportunities_filtered(category=None, city=None, work_mode=None, status=None,
                                 salary_min=None, salary_max=None, experience=None, search=None):
    conditions = []
    params = {}
    if category:
        conditions.append("category = :category")
        params["category"] = category
    if city:
        conditions.append("city = :city")
        params["city"] = city
    if work_mode:
        conditions.append("work_mode = :work_mode")
        params["work_mode"] = work_mode
    if status:
        conditions.append("status = :status")
        params["status"] = status
    if salary_min:
        conditions.append("salary_min >= :salary_min")
        params["salary_min"] = salary_min
    if salary_max:
        conditions.append("salary_max <= :salary_max")
        params["salary_max"] = salary_max
    if experience:
        conditions.append("experience_level = :experience")
        params["experience"] = experience
    if search:
        conditions.append("(LOWER(company_name) LIKE :search OR LOWER(job_title) LIKE :search OR LOWER(required_skills) LIKE :search)")
        params["search"] = f"%{search.lower()}%"

    where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
    query = f"SELECT * FROM opportunities {where} ORDER BY created_at DESC"
    engine = get_engine()
    return pd.read_sql(text(query), engine, params=params)

def insert_opportunity(data: dict):
    engine = get_engine()
    sql = text("""
        INSERT INTO opportunities
        (company_name, job_title, category, city, country, work_mode, required_skills,
         salary_min, salary_max, currency, experience_level, application_deadline, status, source_link)
        VALUES (:company_name, :job_title, :category, :city, :country, :work_mode, :required_skills,
                :salary_min, :salary_max, :currency, :experience_level, :application_deadline, :status, :source_link)
    """)
    with engine.begin() as conn:
        conn.execute(sql, data)

def update_opportunity(opportunity_id: int, data: dict):
    engine = get_engine()
    set_clause = ", ".join([f"{k} = :{k}" for k in data.keys()])
    data["opportunity_id"] = opportunity_id
    sql = text(f"UPDATE opportunities SET {set_clause} WHERE opportunity_id = :opportunity_id")
    with engine.begin() as conn:
        conn.execute(sql, data)

def delete_opportunity(opportunity_id: int):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM opportunities WHERE opportunity_id = :id"), {"id": opportunity_id})

def get_opportunity_by_id(opportunity_id: int):
    engine = get_engine()
    df = pd.read_sql(text("SELECT * FROM opportunities WHERE opportunity_id = :id"),
                     engine, params={"id": opportunity_id})
    return df.iloc[0] if not df.empty else None

def get_deadline_alerts():
    engine = get_engine()
    query = """
        SELECT *, 
               (application_deadline - CURRENT_DATE) AS days_left
        FROM opportunities
        WHERE application_deadline <= CURRENT_DATE + INTERVAL '7 days'
          AND status = 'Open'
        ORDER BY application_deadline ASC
    """
    return pd.read_sql(query, engine)

def get_expired_opportunities():
    engine = get_engine()
    return pd.read_sql(
        "SELECT * FROM opportunities WHERE application_deadline < CURRENT_DATE AND status != 'Expired'",
        engine
    )

def get_duplicates():
    engine = get_engine()
    query = """
        SELECT a.*
        FROM opportunities a
        JOIN opportunities b
          ON a.company_name = b.company_name
         AND LOWER(a.job_title) = LOWER(b.job_title)
         AND a.city = b.city
         AND a.opportunity_id > b.opportunity_id
    """
    return pd.read_sql(query, engine)

def bulk_insert(df: pd.DataFrame):
    """Insert a DataFrame of opportunities. Returns (inserted_count, errors)."""
    engine = get_engine()
    required_cols = ["company_name", "job_title", "category", "required_skills"]
    errors = []
    inserted = 0
    for i, row in df.iterrows():
        missing = [c for c in required_cols if c not in row or pd.isna(row.get(c))]
        if missing:
            errors.append(f"Row {i+1}: missing {missing}")
            continue
        try:
            data = {
                "company_name": row.get("company_name"),
                "job_title": row.get("job_title"),
                "category": row.get("category"),
                "city": row.get("city", ""),
                "country": row.get("country", "Pakistan"),
                "work_mode": row.get("work_mode", "Onsite") if row.get("work_mode") in ["Remote","Onsite","Hybrid"] else "Onsite",
                "required_skills": row.get("required_skills"),
                "salary_min": row.get("salary_min", None),
                "salary_max": row.get("salary_max", None),
                "currency": row.get("currency", "PKR"),
                "experience_level": row.get("experience_level", ""),
                "application_deadline": row.get("application_deadline", None),
                "status": row.get("status", "Open") if row.get("status") in ["Open","Closed","Expired","Shortlisted"] else "Open",
                "source_link": row.get("source_link", ""),
            }
            insert_opportunity(data)
            inserted += 1
        except Exception as e:
            errors.append(f"Row {i+1}: {str(e)}")
    return inserted, errors