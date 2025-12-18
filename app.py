from flask import Flask
from controllers.categoria_controller import categoria_bp

app = Flask(__name__)

app.register_blueprint(categoria_bp)

@app.route("/")
def home():
    return {"status": "API rodando 🚀"}
