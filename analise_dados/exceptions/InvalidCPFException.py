

class InvalidCPFException(Exception):
    def __init__(self, cpf):
        super().__init__("CPF invalido")
