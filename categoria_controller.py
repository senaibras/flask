import collections
import json
from fastapi.encoders import jsonable_encoder
from flask import Flask, jsonify, request

from categoria_repository import CategoriaRepository
from categoria import Categoria
from collections import OrderedDict

import categoria_repository

app = Flask(__name__)

@app.route("/ola", methods = ['GET'])
def ola():
    return "minha primeira API"

@app.route("/clientes", methods = ['GET'])
def listar_clientes():
     dados = [{"nome":"Leandro"}, {"nome":"Maria"}, {"nome":"Silvio"},{"nome":"Marta"}]
     return jsonify(dados)
    
@app.route("/categorias", methods = ['GET'])
def listar_categorias():
    repo = CategoriaRepository()
    dados = repo.find_all()

    cabecalhos = ["id", "nome", "descricao"]
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]

    return jsonify(dados_retorno)

@app.route("/categorias/<int:categoriaID>")
def buscar_por_id(categoriaID):
    repo = CategoriaRepository()
    categoria = repo.find_by_id(categoriaID)
    categoria_retorno = {"id":categoria[0], "nome":categoria[1], "descricao":categoria[2]}
    return jsonify(categoria_retorno)

@app.route("/categorias", methods = ['POST'])
def cadastrar_categoria():
    repo = CategoriaRepository()
    # recebendo os dados via protocolo POST http
    dados_json = request.get_json()
   
    # pegando os dados recebidos do json
    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")

    # enviando para o banco de dados
    repo.create(nome, descricao)

    return jsonify({
            "mensagem":"Categoria cadastrada com sucesso.",
            "nome":nome,
            "descricao":descricao
            }), 201


@app.route("/categorias/<int:id_categoria>", methods = ['DELETE'])
def remover_categoria(id_categoria):
    #objeto de comunicação com o banco de dados
    repo =CategoriaRepository()
    #removendo a categoria do banco de dados
    repo.delete(id_categoria)

    return jsonify({
        "mensagem":"Categoria removida com sucesso."
    })




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









# @app.route("/categorias", methods=['POST'])
# def cadastrar():
#     categoria = request.get_json()
#     descricao = categoria.get('descricao')
#     nome = categoria.get('nome')

#     # repo = CategoriaRepository()
#     # repo.create(nome,descricao)

#     resposta = OrderedDict([('mensagem', 'Cadastrado com sucesso'),('nome', nome),('Descricao', descricao)])
#     return json.dumps(resposta, ensure_ascii=False, indent=2), 201

# @app.route("/remover", methods = ["DELETE"])
# def remover():
#     repo = CategoriaRepository()
#     categoria = request.get_json()
#     id = categoria.get("id")
#     nome = categoria.get("nome")

#     return {'id':id,'nome':nome}
