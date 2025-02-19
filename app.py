from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

# Rota para renderizar o index.html
@app.route("/")
def index():
    return render_template("index.html")

# Evento para receber e enviar mensagens
@socketio.on("message")
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    send(msg, broadcast=True)  # Envia a mensagem para todos os usuários conectados

if __name__ == '__main__':
    socketio.run(app, debug=True)
