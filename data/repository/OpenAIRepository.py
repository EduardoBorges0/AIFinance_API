from config.pgconfig import get_connection


class OpenAIRepository:
    @staticmethod
    def insert_expense_db(category, value, userId):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO despesas (categoria, valor, user_id) VALUES (%s, %s, %s)",
            (category, value, userId)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("Gasto inserido com sucesso!")

    @staticmethod
    def remove_expense_db(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM despesas WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        print("Gasto eliminado com sucesso!")

    @staticmethod
    def update_expense_db(id, category, value):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE despesas SET valor = %s, categoria = %s WHERE id = %s",
            (value, category, id)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("Gasto atualizado com sucesso!")

    @staticmethod
    def get_expenses_db():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM despesas ORDER BY categoria ASC")
        expenses = cur.fetchall()
        cur.close()
        conn.close()
        return expenses