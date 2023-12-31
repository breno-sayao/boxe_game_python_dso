class Habilidade:
    def __init__(self, nome, descricao, tipo, custo):
        self.__nome = nome
        self.__descricao = descricao
        self.__tipo = tipo
        self.__custo = custo
        self.__habilidades = []


    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tipo(self):
        return self.__tipo

    @property
    def custo(self):
        return self.__custo

    @property
    def habilidades(self):
        return self.__habilidades

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError('A descrição deve ser uma string')

    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise TypeError('O tipo deve ser uma string')

    @custo.setter
    def custo(self, custo):
        if isinstance(custo, int):
            self.__custo = custo
        else:
            raise TypeError('O custo deve ser um inteiro')