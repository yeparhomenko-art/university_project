import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect(
    r"E:\Європейськи університет\SQLite pract\university_project\digital_university.db"
)

query = """
SELECT faculty_id, COUNT(*) as students_count
FROM Student
GROUP BY faculty_id
"""

df = pd.read_sql_query(query, conn)

print(df)

plt.bar(df["faculty_id"], df["students_count"])

plt.xlabel("Faculty ID")
plt.ylabel("Кількість студентів")
plt.title("Кількість студентів по факультетах")

plt.show()