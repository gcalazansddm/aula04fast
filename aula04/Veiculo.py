####
## Classe `Veiculo`:
##    - Atributos: `marca`, `modelo`.
##    - Métodos:
##        - `__init__(marca, modelo)`: Inicializa os atributos.
##        - `movimentar()`: Exibe uma mensagem indicando que o veículo está se movendo.
####

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def movimentar(self):
        print("Está se movendo")