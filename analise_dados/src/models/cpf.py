import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)),'../..'))
import exceptions.InvalidCPFException

class CPF():
    @staticmethod
    def validar_cpf(cpf):
        cpf_tratado = cpf.replace(".","").replace("-","")
        if(len(cpf) != 11 ):
            raise InvalidCPFException(cpf)

        primeiro_digito = 0
        segundo_digito = 0
        for i in range(0, 9):
            primeiro_digito += int(cpf_tratado[i]) * (10 - i)
        primeiro_digito = (primeiro_digito * 10) % 11

        if(primeiro_digito > 9):
            primeiro_digito = 0

        for i in range(0, 9):
            segundo_digito += int(cpf_tratado[i]) * (11 - i)

        segundo_digito += primeiro_digito * 2
        segundo_digito = (segundo_digito * 10) % 11

        if(segundo_digito > 9):
            segundo_digito = 0
            
        if(int(cpf_tratado[-1]) != segundo_digito or int(cpf_tratado[-2]) != primeiro_digito ):
            return False
        return True
