## 3. Classe `VeiculoComMotor` (herda de `Veiculo`):
##    - Atributos: `combustivel` (ex.: gasolina, elétrico).
##    - Métodos:
##        - Sobrescreva `movimentar()` para exibir uma mensagem indicando o tipo de combustível.

from Veiculo import Veiculo

class VeiculoComMotor(Veiculo):
    def __init__(self, marca, modelo, combustivel):
        super().__init__(marca, modelo)
        self.combustivel = combustivel

    def movimentar(self):
        print(f"Estamos andando usando {self.combustivel}")
