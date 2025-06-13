## 5. Teste:
##    - Crie instâncias de `Carro` e `VeículoSemMotor` para realizar testes com as funções e atributos.
from Carro import Carro
from VeiculoSemMotor import VeiculoSemMotor

if __name__ == '__main__':
    carro1 = Carro("marea", "marea", "hibrido", "4")
    carro1.detalhes()
    carro1.movimentar()

    carro2 = Carro("Sedan", "Sedan", "combustivel", "4")
    carro2.detalhes()
    carro2.movimentar()

    carro3 = Carro("Brasilia amarela", "Brasilia amarela", "combustivel", "2")
    carro3.detalhes()
    carro3.movimentar()

    veiculo_sem_motor = VeiculoSemMotor("balsa", "azul", "remo")
    veiculo_sem_motor.movimentar()

    veiculo_sem_motor2 = VeiculoSemMotor("bicicleta", "Caloi", "pedal")
    veiculo_sem_motor2.movimentar()

    veiculo_sem_motor3 = VeiculoSemMotor("Pedal", "peto", "perna")
    veiculo_sem_motor3.movimentar()