from data.repository.OpenAIRepository import OpenAIRepository
from data.model.ExpenseData import ExpenseData
from config.securityprompt import extract_expenses

class OpenAIService(OpenAIRepository):
    @staticmethod
    def insert_expense_db(user_input, user_id):
        data = []
        response = extract_expenses(user_input)
        output_text = getattr(response, "output_text", "") or ""

        if not output_text.strip():
            return [{"mensagem": "Nenhum gasto identificado na frase."}]

        for line in output_text.split("\n"):
            if ":" in line:
                categoria, valor = line.split(":", 1)
                categoria = categoria.strip()
                try:
                    valor = float(valor.strip().replace(",", "."))
                except ValueError:
                    continue  # ignora linhas inválidas
                expense = ExpenseData(categoria, valor, user_id)
                data.append({
                    "categoria": expense.categoria,
                    "valor": expense.valor
                })

        if not data:
            return [{"mensagem": "Nenhum gasto identificado na frase."}]

        for item in data:
            category = item["categoria"]
            value = item["valor"]
            OpenAIRepository.insert_expense_db(category, value, user_id)

        return data

    @staticmethod
    def remove_expense_db(id):
        OpenAIRepository.remove_expense_db(id)

    @staticmethod
    def update_expense_db(id, category, value):
        OpenAIRepository.update_expense_db(id, category, value)

    @staticmethod
    def get_expenses_db():
        return OpenAIRepository.get_expenses_db()
