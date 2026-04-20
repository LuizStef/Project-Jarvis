class Assistente:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}, versão {self.versao}.")

    def __str__(self):
        return f"{self.nome} v{self.versao}"
