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
        cur.execute("SELECT id, name, email, password FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is None:
            return None
        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "password": row[3]
        }

    @staticmethod
    def get_user_by_id(user_id: int):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, password FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "password": row[3],
            }
        return None
