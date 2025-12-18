from decimal import Decimal

class Produto:
    def __init__(self,
                 produto_id: int = None,
                 nome: str = None,
                 descricao: str = None,
                 preco: Decimal = Decimal("0.00"),
                 quantidade_estoque: int = 0,
                 categoria_id: int = None):
        self._produto_id = produto_id
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._quantidade_estoque = quantidade_estoque
        self._categoria_id = categoria_id

    # ProdutoID
    @property
    def produto_id(self) -> int:
        return self._produto_id

    @produto_id.setter
    def produto_id(self, value: int) -> None:
        self._produto_id = value

    # Nome
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        self._nome = value

    # Descricao
    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, value: str) -> None:
        self._descricao = value

    # Preco
    @property
    def preco(self) -> Decimal:
        return self._preco

    @preco.setter
    def preco(self, value: Decimal) -> None:
        self._preco = value

    # QuantidadeEstoque
    @property
    def quantidade_estoque(self) -> int:
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, value: int) -> None:
        self._quantidade_estoque = value

    # CategoriaID
    @property
    def categoria_id(self) -> int:
        return self._categoria_id

    @categoria_id.setter
    def categoria_id(self, value: int) -> None:
        self._categoria_id = value
