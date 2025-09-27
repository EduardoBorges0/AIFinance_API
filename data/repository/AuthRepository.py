from config.pgconfig import get_connection

class AuthRepository:
    @staticmethod
    def register_user(name: str, email: str, password: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password),
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_user_by_email(email: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        if row is None:
            return None
        else:
            return row
        cur.close()
        conn.close()
