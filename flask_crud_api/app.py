from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Task

app = Flask(__name__)
CORS(app)

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Cria o banco se ainda não existir
with app.app_context():
    db.create_all()

# -----------------------------
# ROTAS DA API
# -----------------------------
@app.route("/")
def index():
    return jsonify({"message": "API Flask CRUD está online!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    return jsonify(task.to_dict()), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Campo 'title' é obrigatório"}), 400

    new_task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.done = data.get("done", task.done)
    db.session.commit()

    return jsonify(task.to_dict()), 200

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarefa removida com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)
