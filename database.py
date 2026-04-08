import sqlite3
import pandas as pd

def load_data_to_db():
    conn = sqlite3.connect("campus.db")
    df = pd.read_csv("campus_pulse_data.csv")
    df.to_sql("student_feedback", conn, if_exists="replace", index=False)
    conn.close()

def get_department_avg():
    conn = sqlite3.connect("campus.db")
    query = """
    SELECT Department, AVG(Rating) as Avg_Rating
    FROM student_feedback
    GROUP BY Department
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result

def get_facility_avg():
    conn = sqlite3.connect("campus.db")
    query = """
    SELECT Facility, AVG(Rating) as Avg_Rating
    FROM student_feedback
    GROUP BY Facility
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result