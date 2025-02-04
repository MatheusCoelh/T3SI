from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Definindo as saudações
saudacoes_usuario = ["oi", "olá", "eae", "opa", "coe"]
saudacoes_bot = ["Olá!", "Oi, como posso ajudar?", "Oi, tudo bem?", "Olá, o que você gostaria de saber?"]

# Simulando um estoque
estoque = {
    "borracha": 10,
    "caneta": 20,
    "caderno": 15
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    mensagem = request.form['mensagem'].lower()

    if mensagem in saudacoes_usuario:
        resposta_bot = random.choice(saudacoes_bot)
    elif "estoque" in mensagem:
        item = mensagem.split()[-1]
        if item in estoque:
            resposta_bot = f"No momento, temos {estoque[item]} unidades de {item} em estoque."
        else:
            resposta_bot = f"Desculpe, não temos informações de estoque para {item}."
    else:
        resposta_bot = "Desculpe, eu não entendi. Poderia repetir, por favor?"

    return resposta_bot

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
