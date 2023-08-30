from ataque import Ataque
from boxeador import Boxeador
from defesa import Defesa
from equipamento import Equipamento
from esquiva import Esquiva
from habilidade import Habilidade
from status import Status


# Path: main.py
class init_game:

    def __init__(self):
        pass

    def init_habilidade(self):
        Ataque('Jab', 'Soco direto', 'Ataque', 2, 3)
        Ataque('Cross', 'Soco cruzado', 'Ataque', 4, 6)
        Ataque('Hook', 'Soco gancho', 'Ataque', 3, 5)
        Ataque('Uppercut', 'Soco uppercut', 'Ataque', 5, 8)

        Defesa('Bloqueio', 'Bloqueio de soco', 'Defesa', 3, 35)
        Defesa('Guarda Alta', 'Posição defensiva com os braços', 'Defesa', 4, 43)
        Defesa('Cobertura', 'Cobrir a cabeça e o corpo com os braços', 'Defesa', 7, 75)
        Defesa('Clinch', 'Segurar o oponente para interromper ataques', 'Defesa', 9, 90)

        Esquiva('Esquiva Rápida', 'Esquiva rápida para desviar de socos', 'Esquiva', 10, 15)
        Esquiva('Deslizamento', 'Movimento sutil para desviar de golpes', 'Esquiva', 15, 20)
        Esquiva('Esquiva Diagonal', 'Esquiva diagonal para evitar ataques', 'Esquiva', 20, 25)
        Esquiva('Esquiva para Trás', 'Movimento de recuo para escapar de golpes', 'Esquiva', 25, 30)


    def init_boxeador(self):
        adversario_1 = Boxeador('Muhammad Ali', 'The Greatest', 74, 107.5, 1.91, 'Estados Unidos', self.init_equipamento(), self.init_status())
        adversario_2 = Boxeador('Mike Tyson', 'Iron Mike', 54, 109.8, 1.78, 'Estados Unidos', self.init_equipamento(), self.init_status())
        adversario_3 = Boxeador('Floyd Mayweather Jr', 'Money', 43, 70.3, 1.73, 'Estados Unidos', self.init_equipamento(), self.init_status())

        return adversario_1, adversario_2, adversario_3


init_game = init_game()
init_game.init_habilidade()