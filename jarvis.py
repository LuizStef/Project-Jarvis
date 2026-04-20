from base import Assistente

class Jarvis(Assistente):
    def __init__(self):
        super().__init__("Jarvis", "0,1")
        self.humor = "Neutro"

    def responder(self, perguntar):
        print(f"[{self.nome}]: Recebi sua mensagem: '{perguntar}'")


jarvis = Jarvis()
jarvis.apresentar()
jarvis.responder("Olá, jarvis!")
print(jarvis)
