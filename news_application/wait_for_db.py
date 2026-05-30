import time
import MySQLdb

while True:
    try:
        conn = MySQLdb.connect(
            host="db",
            user="django_user",
            passwd="django_pass",
            db="news_app_db",
        )
        conn.close()
        break
    except Exception:
        print("Waiting for DB...")
        time.sleep(2)

print("DB is ready!")