from data.repository.OpenAIRepository import OpenAIRepository
from data.model.ExpenseData import ExpenseData
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class OpenAIService(OpenAIRepository):
    @staticmethod
    def insert_expense_db(user_input, user_id):
        data = []
        prompt = (
            f"Extraia os gastos da seguinte frase: '{user_input}'.\n"
            "Para cada gasto, retorne em uma linha separada no formato:\n"
            "Categoria: Valor\n"
            "- Apenas categorias e valores.\n"
            "- Use ponto como separador decimal.\n"
            "- Não inclua palavras extras.\n"
            "- Exemplo de saída:\n"
            "Alimentação: 2.50\n"
            "Bebidas: 1.50"
        )
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            max_output_tokens=60
        )

        output_text = response.output_text
        for line in output_text.split("\n"):
            if ":" in line:
                categoria, valor = line.split(":", 1)
                categoria = categoria.strip()
                valor = float(valor.strip().replace(",", "."))
                expense = ExpenseData(categoria, valor, user_id)
                data.append({"categoria": expense.categoria, "valor": expense.valor})

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
