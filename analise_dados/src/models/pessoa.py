from mensagens import MSG_CELULAR_INVALIDO, MSG_CELULAR_VAZIO
from cpf import CPF

class Pessoa():
    __LISTA_PREPOSICOES = ["da", "de", "do", "das", "dos", "e"]

    def __init__(self, nome_completo, email, celular, cpf, cep, interesse):
        self.__obs = []
        self.__nome_completo = self.__convert_to_camel_case(nome_completo)

        splitted_name = self.__nome_completo.split(" ")
        self.__primeiro_nome = splitted_name[0]

        self.__segundo_nome = splitted_name[1]
        if self.__segundo_nome.lower() in self.__LISTA_PREPOSICOES:
            self.__segundo_nome = f"{self.__segundo_nome} {splitted_name[2]}"
        
        self.__genero = None
        self.__email = email

        self.cpf = CPF.validar_cpf(cpf)
        self.cep, self.DDD = None, None # fazer a chamada para o viacep
        
        self.celular = self.__normalize_cellphone(celular, "")
        if self.celular == "":
            self.__obs.append(MSG_CELULAR_VAZIO)
        if self.celular == None:
            self.__obs.append(MSG_CELULAR_INVALIDO)

    def __get_ddd(self,local):
        return "81"
    
    def __normalize_cellphone(self, value : str , local : str) -> str:
        normalized_str = value.replace(" ", "") \
                              .replace("(", "") \
                              .replace(")", "") \
                              .replace("-", "")
        if len(normalized_str) == 8:
            ddd = self.__get_ddd(local)
            return ddd + " 9" + normalized_str
        elif len(normalized_str) == 9:
            ddd = self.__get_ddd(local)
            return ddd + " " + normalized_str
        elif len(normalized_str) == 11:
            ddd = normalized_str[0:2]
            number = normalized_str[2:]
            return ddd + " " + number
        elif len(normalized_str) == 10:
            ddd = normalized_str[0:2]
            number = normalized_str[2:]
            return ddd + " 9" + number
        elif len(normalized_str) == 0:
            return ""
        else:
            return None

    def __convert_to_camel_case(self, value : str) -> str:
        final_name = ""
        value_ = value.lower()
        names = value_.split(" ")
        for name in names:
            if name in self.__LISTA_PREPOSICOES:
                final_name = f"{final_name}{name} "
            else:
                name = f"{name[0]}".upper() + name[1:]
                final_name = f"{final_name}{name} "
        return final_name
    
    def __str__(self):
        return f"{self.__nome_completo}, {self.__primeiro_nome}, {self.__segundo_nome}, {self.celular}, {self.__obs}"
    
if __name__ == '__main__':
    print(Pessoa("RAFAELA TEIXEIRA DAS GRAÇAS BORIN","a@gmail.com" ,"52127281","1","1",""))
    print(Pessoa("mateus araújo teixeira","a@gmail.com",     "(92) 93484-5633","1","1",""))
    print(Pessoa("Luiza Ribeiro Jorocó","a@gmail.com",         "(38)4132-3807","1","1",""))
    print(Pessoa("CarLoS De SOuzA","a@gmail.com",                 "94132-3807","1","1",""))
    print(Pessoa("CarLoS De SOuzA","a@gmail.com",                          "9","1","1",""))


