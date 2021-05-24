from os import getcwd
from csv import DictWriter, DictReader
from pathlib import Path


class Pessoa():

    def __init__(self,nome, cpf,endereco,bairro,cep,celular,email,proficao):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__bairro = bairro
        self.__cep = cep
        self.__celular = celular
        self.__email = email
        self.__proficao = proficao


class Cliente(Pessoa):
    def __init__(self,nome,cpf,endereco,bairro,cep,celular,email,proficao,credito,situacao):
        super().__init__(nome,cpf,endereco,bairro,cep,celular,email,proficao)
        self.__credito = credito
        self.__situacao = situacao

    def mostra_nome(self):
        return self._Pessoa__nome

    def gravar(self):
        try:
            with open(f'{getcwd()}/db/dbcli.csv') as ler:
                ler_csv = DictReader(ler,delimiter=';')
                for linha in ler_csv:
                    id_Cli = int(linha['ID'])
                id_Cli = id_Cli + 1

            with open(f'{getcwd()}/db/dbcli.csv', 'a') as clientes:
                grava_csv = DictWriter(clientes,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO','SALDO/DEVEDOR','SITUACAO'])
                grava_csv.writerow({'ID':id_Cli,'NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'PROFICAO':self._Pessoa__proficao,'SALDO/DEVEDOR':self.__credito,'SITUACAO':self.__situacao})
                return 'ok'
        except:
            with open(f'{getcwd()}/db/dbcli.csv', 'w') as clientes:
                    grava_csv = DictWriter(clientes,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO','SALDO/DEVEDOR','SITUACAO'])
                    grava_csv.writeheader()
                    grava_csv.writerow({'ID':'100','NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'PROFICAO':self._Pessoa__proficao,'SALDO/DEVEDOR':self.__credito,'SITUACAO':self.__situacao})
                    return 'ok'
        
def cliente():
    """ Cliente com seus dados para cadastro
    Nome completo / CPF valido / Endereco: Av ou Rua, Complemento, e Numero da residencia / 
    Numero de contato / Email / e Proficao """
    while True:
        nome = input(f"Digite o Nome Completo  do Cliente\n>>> ")
        if not nome.isalpha:
            print("Isso nao e um Nome!")
        else:
            break
    while True:
        cpf = input(f"Digite o CPF do Cliente(apenas numeros)\n>>> ")
        if not cpf.isnumeric() or len(cpf) != 11:
            print("CPF invalido")
        else:
            break

    endereco = input(f"Digite o Endereco: >>> ")
    bairro = input("Digite o Bairro >>> ")
    cep = input("Numero do CEP >>> ")
    numTel = input(f"Digite um numero para contato\n>>> ")
    email = input(f"Digite o email\n>>> ")
    prof = input(f"Digite sua Proficao\n>>> ")
    novo_cliente = Cliente(nome,cpf,endereco,bairro,cep,numTel,email,prof,0,'Ativa')
    resp = novo_cliente.gravar()
    if resp == 'ok':
        print(f'Cliente {novo_cliente.mostra_nome()} Gravado com Sucesso!')
    else:
        print(f'ERRO ao gravar o Cliente {novo_cliente.mostra_nome()}, tente novamente!')
def Colaborador():
    """ Colaborador para realizar uma venda e atender ao cliente
    Codigo / Nome Completo / CPF Valido / Endereco: AV ou Rua, Complemento, Numero da residencia /
    Numero de contato / Email / Cargo na empresa / Setor """


def Fornecedor():
    """ Aquele que fornerce produtos para a empresa
    Nome Razao Social / CNPJ Valido / Endereco AV. ou Rua, Complemento, Numero(residencia/Predio/Escritorio) / 
    Numero de Contato / Email / Web Site(Opcional) / Categoria / Nome do Promotor Atual / Numero de contato do Promotor"""

def Produto():
    """ Produto de um Fornecedor e pronto para venda ao cliente
    Descrica do Produto / Quantidade em estoque / Valor de Venda / Categoria / Nome do fornecedor /
     """

def Usuario():
    """ Usuario que vai estar utilizando o sistema
    Nome de usuario / Senha / Permicoes (Adm,Comum,Basico) / Codigo do Colaborador / Nome do Colaborador """

