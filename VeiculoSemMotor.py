####
## 2. Classe `VeiculoSemMotor` (herda de `Veiculo`):
##     - Atributos: `tipo_propulsao` (ex.: pedal, remo).
##    - Métodos:
##        - Sobrescreva `movimentar()` para exibir uma mensagem indicando o tipo de propulsão.
####
from Veiculo import Veiculo

class VeiculoSemMotor(Veiculo):
    def __init__(self, marca, modelo, tipo_propulsao):
        super().__init__(marca, modelo)
        self.tipo_propulsao = tipo_propulsao

    def movimentar(self):
        print(f"Está se movendo usado {self.tipo_propulsao}")