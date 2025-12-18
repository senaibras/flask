from conexao import Conexao  # Ajuste o nome do arquivo se necessário

class CategoriaRepository:
    def __init__(self):
        self.conexao = Conexao()  # Armazena instância completa da Conexao

    def find_all(self):
            cursor = self.conexao.get_cursor()  # dictionary=True já configurado
            cursor.execute("SELECT CategoriaID as id, Nome as nome, Descricao as descricao FROM Categoria ORDER BY CategoriaID")
            return cursor.fetchall()


    def find_by_id(self, categoria_id):
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "SELECT CategoriaID as id, Nome as nome, Descricao as descricao FROM Categoria WHERE CategoriaID = %s",
                (categoria_id,)
            )
            return cursor.fetchone()


    def create(self, nome, descricao=""):
        """Insere novo registro (ID auto-increment)."""
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "INSERT INTO Categoria (Nome, Descricao) VALUES (%s, %s)",
                (nome, descricao)
            )
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

#     def update(self, categoria_id, nome, descricao=""):
#         """Atualiza registro existente."""
#         cursor = None
#         try:
#             cursor = self.conexao.get_cursor()
#             cursor.execute(
#                 "UPDATE Categoria SET Nome = %s, Descricao = %s WHERE CategoriaID = %s",
#                 (nome, descricao, categoria_id)
#             )
#             self.conexao.get_conexao().commit()
#             return cursor.rowcount > 0
#         except Exception as e:
#             print(f"Erro ao atualizar categoria {categoria_id}: {e}")
#             self.conexao.get_conexao().rollback()
#             return False
#         finally:
#             if cursor:
#                 cursor.close()

    def delete(self, categoria_id):
        """Remove registro pelo ID."""
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("DELETE FROM Categoria WHERE CategoriaID = %s", (categoria_id,))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar categoria {categoria_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def fechar_conexao(self):
        """Fecha conexão do repositório."""
        self.conexao.fechar_conexao()


# # Instância global
# repo = CategoriaRepository()

# # Teste funcionando

# categorias = repo.find_all()
# print("Categorias encontradas:", categorias)
    
# cat = repo.find_by_id(1)
# print("Categoria 1:", cat)
    
   