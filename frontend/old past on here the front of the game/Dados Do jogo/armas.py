
def possiveis_armas():
    raridade_arma = {
        'adaga': {
            'comum':    {'dano': 8, 'velocidade': 10},
            'raro':     {'dano': 12, 'velocidade': 10},
            'épico':    {'dano': 16, 'velocidade': 10},
            'lendário': {'dano': 20, 'velocidade': 10},
        },
        'espada': {
            'comum':    {'dano': 12, 'velocidade': 7},
            'raro':     {'dano': 18, 'velocidade': 7},
            'épico':    {'dano': 24, 'velocidade': 7},
            'lendário': {'dano': 30, 'velocidade': 7},
        },
        'cutelo': {
            'comum':    {'dano': 16, 'velocidade': 5},
            'raro':     {'dano': 24, 'velocidade': 5},
            'épico':    {'dano': 32, 'velocidade': 5},
            'lendário': {'dano': 40, 'velocidade': 5},
        },
        'machado': {
            'comum':    {'dano': 16, 'velocidade': 5},
            'raro':     {'dano': 24, 'velocidade': 5},
            'épico':    {'dano': 32, 'velocidade': 5},
            'lendário': {'dano': 40, 'velocidade': 5},
        },
        'espada curta': {
            'comum':    {'dano': 10, 'velocidade': 9},
            'raro':     {'dano': 15, 'velocidade': 9},
            'épico':    {'dano': 20, 'velocidade': 9},
            'lendário': {'dano': 25, 'velocidade': 9},
        },
        'espada longa': {
            'comum':    {'dano': 14, 'velocidade': 6},
            'raro':     {'dano': 21, 'velocidade': 6},
            'épico':    {'dano': 28, 'velocidade': 6},
            'lendário': {'dano': 35, 'velocidade': 6},
        },
        'lança': {
            'comum':    {'dano': 12, 'velocidade': 6},
            'raro':     {'dano': 18, 'velocidade': 6},
            'épico':    {'dano': 24, 'velocidade': 6},
            'lendário': {'dano': 30, 'velocidade': 6},
        },
        'arco': {
            'comum':    {'dano': 10, 'velocidade': 6},
            'raro':     {'dano': 15, 'velocidade': 6},
            'épico':    {'dano': 20, 'velocidade': 6},
            'lendário': {'dano': 25, 'velocidade': 6},
        },
        'monopola': {
            'comum':    {'dano': 6,  'velocidade': 8},
            'raro':     {'dano': 9,  'velocidade': 8},
            'épico':    {'dano': 12, 'velocidade': 8},
            'lendário': {'dano': 15, 'velocidade': 8},
        },
        'zarabatana': {
            'comum':    {'dano': 8,  'velocidade': 7},
            'raro':     {'dano': 12, 'velocidade': 7},
            'épico':    {'dano': 16, 'velocidade': 7},
            'lendário': {'dano': 20, 'velocidade': 7},
        },
        'adaga dupla': {
            'comum':    {'dano': 16, 'velocidade': 5},
            'raro':     {'dano': 24, 'velocidade': 5},
            'épico':    {'dano': 30, 'velocidade': 5},
            'lendário': {'dano': 40, 'velocidade': 5},
        },
        'espada dupla': {
            'comum':    {'dano': 24, 'velocidade': 4},
            'raro':     {'dano': 36, 'velocidade': 4},
            'épico':    {'dano': 48, 'velocidade': 4},
            'lendário': {'dano': 60, 'velocidade': 4},
        },
        'cutelo duplo': {
            'comum':    {'dano': 32, 'velocidade': 5},
            'raro':     {'dano': 48, 'velocidade': 5},
            'épico':    {'dano': 64, 'velocidade': 5},
            'lendário': {'dano': 80, 'velocidade': 5},
        },
        'escudo': {
            'comum':    {'dano': 34, 'velocidade': 5},
            'raro':     {'dano': 55, 'velocidade': 5},
            'épico':    {'dano': 65, 'velocidade': 5},
            'lendário': {'dano': 78, 'velocidade': 5},
        }
    }
    return raridade_arma

class armas:
    def __init__ (sef, arma, raridade):
        