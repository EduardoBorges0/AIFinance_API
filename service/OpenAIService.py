from data.repository.OpenAIRepository import OpenAIRepository
from data.model.ExpenseData import ExpenseData
from config.securityprompt import extract_expenses

class OpenAIService(OpenAIRepository):
    @staticmethod
    def insert_expense_db(user_input, user_id):
        data = []
        response = extract_expenses(user_input)
        print(response)
        if not response:
            return [{"mensagem": "Nenhum gasto identificado na frase."}]

        # Itera e salva cada item
        for item in response:
            category = item.get("category")
            value = item.get("value")
            try:
                value = float(str(value).replace(",", "."))
            except (ValueError, TypeError):
                continue
            OpenAIRepository.insert_expense_db(category, value, user_id)
            data.append({"categoria": category, "valor": value})
        if not data:
            return [{"mensagem": "Nenhum gasto válido para salvar."}]

        print(data)
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
