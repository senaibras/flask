from decimal import Decimal
from conexao import Conexao  # mesmo padrão do CategoriaRepository
from produto import Produto  # classe Produto com @property


class ProdutoRepository:
    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        """
        Retorna todos os produtos como dicionários.
        """
        cursor = self.conexao.get_cursor()  # dictionary=True já configurado
        cursor.execute("""
            SELECT 
                ProdutoID      AS id,
                Nome           AS nome,
                Descricao      AS descricao,
                Preco          AS preco,
                QuantidadeEstoque AS quantidade_estoque,
                CategoriaID    AS categoria_id
            FROM Produto
            ORDER BY ProdutoID
        """)
        return cursor.fetchall()

    def find_by_id(self, produto_id: int):
        """
        Retorna um produto (dict) pelo ID ou None.
        """
        cursor = self.conexao.get_cursor()
        cursor.execute("""
            SELECT 
                ProdutoID      AS id,
                Nome           AS nome,
                Descricao      AS descricao,
                Preco          AS preco,
                QuantidadeEstoque AS quantidade_estoque,
                CategoriaID    AS categoria_id
            FROM Produto
            WHERE ProdutoID = %s
        """, (produto_id,))
        return cursor.fetchone()

    def create(self, nome: str, descricao: str = "", preco: Decimal = Decimal("0.00"),
               quantidade_estoque: int = 0, categoria_id: int | None = None):
        """
        Insere um novo produto (ID auto-increment) e retorna o ID gerado.
        """
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("""
                INSERT INTO Produto 
                    (Nome, Descricao, Preco, QuantidadeEstoque, CategoriaID)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, descricao, preco, quantidade_estoque, categoria_id))
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def update(self, produto_id: int, nome: str, descricao: str,
               preco: Decimal, quantidade_estoque: int, categoria_id: int | None):
        """
        Atualiza um produto existente. Retorna True se alterou alguma linha.
        """
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("""
                UPDATE Produto
                SET Nome = %s,
                    Descricao = %s,
                    Preco = %s,
                    QuantidadeEstoque = %s,
                    CategoriaID = %s
                WHERE ProdutoID = %s
            """, (nome, descricao, preco, quantidade_estoque, categoria_id, produto_id))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar produto {produto_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def delete(self, produto_id: int):
        """
        Remove produto pelo ID. Retorna True se removeu.
        """
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("DELETE FROM Produto WHERE ProdutoID = %s", (produto_id,))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar produto {produto_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def fechar_conexao(self):
        """
        Fecha conexão do repositório.
        """
        self.conexao.fechar_conexao()
