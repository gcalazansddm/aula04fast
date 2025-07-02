## Classe `Carro` (herda de `VeiculoComMotor`):
##    - Atributos: `quantidade_portas`.
##    - Métodos:
##        - Implemente um método `detalhes()` que exibe todas as informações do carro.
from VeiculoComMotor import VeiculoComMotor

class Carro(VeiculoComMotor):
    def __init__(self, marca, modelo, combustivel, quantidade_portas):
        super().__init__(marca, modelo, combustivel)
        self.quantidade_portas = quantidade_portas
    
    def detalhes(self):
        print(f"Marca {self.marca}\n" \
        f"Modelo {self.modelo}\n" \
        f"Combustivel {self.combustivel}\n" \
        f"Quantidade portas {self.quantidade_portas}")