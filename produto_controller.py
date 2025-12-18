from decimal import Decimal
from flask import Blueprint, request, jsonify
from produto_repository import ProdutoRepository
from produto import Produto

produto_bp = Blueprint("produto", __name__)
repo = ProdutoRepository()


# GET /produtos  -> lista todos
@produto_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    rows = repo.find_all()
    return jsonify(rows), 200


# GET /produtos/<id>  -> busca por id
@produto_bp.route("/produtos/<int:produto_id>", methods=["GET"])
def buscar_produto(produto_id):
    row = repo.find_by_id(produto_id)
    if not row:
        return jsonify({"mensagem": "Produto não encontrado"}), 404
    return jsonify(row), 200


# POST /produtos  -> cria
@produto_bp.route("/produtos", methods=["POST"])
def criar_produto():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    if not nome:
        return jsonify({"erro": "Campo 'nome' é obrigatório"}), 400

    descricao = dados.get("descricao", "")
    preco_str = str(dados.get("preco", "0.00"))
    quantidade_estoque = int(dados.get("quantidade_estoque", 0))
    categoria_id = dados.get("categoria_id")

    preco = Decimal(preco_str)

    novo_id = repo.create(
        nome=nome,
        descricao=descricao,
        preco=preco,
        quantidade_estoque=quantidade_estoque,
        categoria_id=categoria_id
    )

    if novo_id is None:
        return jsonify({"erro": "Erro ao criar produto"}), 500

    return jsonify({"mensagem": "Produto criado com sucesso", "id": novo_id}), 201


# PUT /produtos/<id>  -> atualiza
@produto_bp.route("/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    dados = request.get_json() or {}

    nome = dados.get("nome")
    if not nome:
        return jsonify({"erro": "Campo 'nome' é obrigatório"}), 400

    descricao = dados.get("descricao", "")
    preco_str = str(dados.get("preco", "0.00"))
    quantidade_estoque = int(dados.get("quantidade_estoque", 0))
    categoria_id = dados.get("categoria_id")

    preco = Decimal(preco_str)

    ok = repo.update(
        produto_id=produto_id,
        nome=nome,
        descricao=descricao,
        preco=preco,
        quantidade_estoque=quantidade_estoque,
        categoria_id=categoria_id
    )

    if not ok:
        return jsonify({"erro": "Produto não encontrado ou não atualizado"}), 404

    return jsonify({"mensagem": "Produto atualizado com sucesso"}), 200


# DELETE /produtos/<id>  -> remove
@produto_bp.route("/produtos/<int:produto_id>", methods=["DELETE"])
def deletar_produto(produto_id):
    ok = repo.delete(produto_id)
    if not ok:
        return jsonify({"erro": "Produto não encontrado ou não deletado"}), 404
    return jsonify({"mensagem": "Produto deletado com sucesso"}), 200

