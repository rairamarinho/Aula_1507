class Personagem:
    def __init__(self, nome, pontuacao, moedas):
        self.nome = nome
        self.pontuacao = pontuacao
        self.moedas = moedas

    def usar_poder(self):
        if self.nome == "Mario":
            return "Super Mario!"
        elif self.nome == "Luigi":
            return "Fire Luigi!"
        else:
            return "Flying Yoshi!"


personagem1 = Personagem("Luigi", 97, 34)
print(f"Nome do personagem: {personagem1.nome} Poder Especial: {personagem1.usar_poder()}")
