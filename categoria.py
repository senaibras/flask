class Categoria:
    def __init__(self, id=None, nome="", descricao=""):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    # Getter e Setter para ID
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        if valor is None or isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError("ID deve ser inteiro ou None")

    # Getter e Setter para Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__nome = valor.strip()
        else:
            raise ValueError("Nome deve ser string não vazia (máx. 100 caracteres)")

    # Getter e Setter para Descrição
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        if isinstance(valor, str) and len(valor) <= 500:
            self.__descricao = valor.strip()
        else:
            raise ValueError("Descrição deve ser string (máx. 500 caracteres)")

    def __str__(self):
        return f"Categoria(id={self.__id}, nome='{self.nome}', descricao='{self.descricao[:50]}...')"


