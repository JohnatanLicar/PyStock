from os import getcwd
from csv import DictWriter, DictReader
from pathlib import Path


class Pessoa():

    def __init__(self,nome, cpf,endereco,bairro,cep,celular,email):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__bairro = bairro
        self.__cep = cep
        self.__celular = celular
        self.__email = email

class Cliente(Pessoa):
    def __init__(self,nome,cpf,endereco,bairro,cep,celular,email,proficao,credito,situacao):
        super().__init__(nome,cpf,endereco,bairro,cep,celular,email)
        self.__proficao = proficao
        self.__credito = credito
        self.__situacao = situacao

    @property
    def mostra_nome(self):
        return self._Pessoa__nome

    def gravar(self):
        try:
            with open(f'{getcwd()}/db/dbcli.csv') as ler:
                ler_csv = DictReader(ler,delimiter=';')
                for linha in ler_csv:
                    id_Cli = int(linha['ID'])
                id_Cli = id_Cli + 1

            with open(f'{getcwd()}/db/dbcli.csv', 'a') as dados:
                grava_csv = DictWriter(dados,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO','SALDO/DEVEDOR','SITUACAO'])
                grava_csv.writerow({'ID':id_Cli,'NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'PROFICAO':self.__proficao,'SALDO/DEVEDOR':self.__credito,'SITUACAO':self.__situacao})
                return 'ok'
        except:
            with open(f'{getcwd()}/db/dbcli.csv', 'w') as dados:
                    grava_csv = DictWriter(dados,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO','SALDO/DEVEDOR','SITUACAO'])
                    grava_csv.writeheader()
                    grava_csv.writerow({'ID':'100','NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'PROFICAO':self.__proficao,'SALDO/DEVEDOR':self.__credito,'SITUACAO':self.__situacao})
                    return 'ok'

class Colaborador(Pessoa):
    def __init__(self,nome,cpf,endereco,bairro,cep,celular,email,cargo,setor,usuario):
        super().__init__(nome,cpf,endereco,bairro,cep,celular,email)
        self.__cargo = cargo
        self.__setor = setor
        self.__usuario = usuario

    @property
    def mostra_nome(self):
        return self._Pessoa__nome

    def gravar(self):
        try:
            with open(f'{getcwd()}/db/dbcolab.csv') as ler:
                ler_csv = DictReader(ler,delimiter=';')
                for linha in ler_csv:
                    id_colab = int(linha['ID'])
                id_colab = id_colab + 1

            with open(f'{getcwd()}/db/dbcolab.csv', 'a') as dados:
                grava_csv = DictWriter(dados,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','CARGO','SETOR','USUARIO'])
                grava_csv.writerow({'ID':id_colab,'NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'CARGO':self.__cargo,'SETOR':self.__setor,'USUARIO':self.__usuario})
                return 'ok'
        except:
            with open(f'{getcwd()}/db/dbcolab.csv', 'w') as dados:
                    grava_csv = DictWriter(dados,delimiter=';', fieldnames=['ID','NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','CARGO','SETOR','USUARIO'])
                    grava_csv.writeheader()
                    grava_csv.writerow({'ID':'100','NOME':self._Pessoa__nome,'CPF':self._Pessoa__cpf,'ENDERECO':self._Pessoa__endereco,'BAIRRO':self._Pessoa__bairro,'CEP':self._Pessoa__cep,'CELULAR':self._Pessoa__celular,'EMAIL':self._Pessoa__email,'CARGO':self.__cargo,'SETOR':self.__setor,'USUARIO':self.__usuario})
                    return 'ok'

class Fornecedor():
    def __init__(self,razaosocial,nomefantasia,cnpj,endereco,bairro,cep,contato,email):
        self.__razaosocial = razaosocial
        self.__nomefantasia = nomefantasia
        self.__cnpj = cnpj
        self.__endereco = endereco
        self.__bairro = bairro
        self.__cep = cep
        self.__contato = contato
        self.__email = email

    def gravar(self):
        try:
            with open(f'{getcwd()}/db/dbforn.csv',) as ler_csv:
                forn_csv = DictReader(ler_csv, delimiter=';')
                for linha in forn_csv:
                    id_forn = int(linha['ID'])
                id_forn = id_forn + 1

            with open(f'{getcwd()}/db/dbforn.csv', 'a') as dados:
                grava_forn = DictWriter(dados,delimiter=';', fieldnames=['ID','RAZAO_SOCIAL','NOME_FANTASIA','CNPJ','ENDERECO','BAIRRO','CEP','CONTATO','EMAIL'])
                grava_forn.writerow({'ID':id_forn,'RAZAO_SOCIAL':self.__razaosocial,'NOME_FANTASIA':self.__nomefantasia,'CNPJ':self.__cnpj,'ENDERECO':self.__endereco,'BAIRRO':self.__bairro,'CEP':self.__cep,'CONTATO':self.__contato,'EMAIL':self.__email})
                return 'ok'
        except:
            with open(f'{getcwd()}/db/dbforn.csv', 'w') as dados:
                grava_forn = DictWriter(dados,delimiter=';',fieldnames=['ID','RAZAO_SOCIAL','NOME_FANTASIA','CNPJ','ENDERECO','BAIRRO','CEP','CONTATO','EMAIL'])
                grava_forn.writeheader()
                grava_forn.writerow({'ID':'100','RAZAO_SOCIAL':self.__razaosocial,'NOME_FANTASIA':self.__nomefantasia,'CNPJ':self.__cnpj,'ENDERECO':self.__endereco,'BAIRRO':self.__bairro,'CEP':self.__cep,'CONTATO':self.__contato,'EMAIL':self.__email})



class Produtos():
    def __init__(self,descricao,fornecedor,codbarras,quantidades,valor,):
        self.__decricao = descricao
        self.__fornecedor = fornecedor
        self.__codbarras = codbarras
        self.__quantidade = quantidades
        self.__valor = valor

class Usuario():
    def __init__(self,usuario,senha,privilegio):
        self.usuario = usuario
        self.__senha = senha
        self.__privilegio = privilegio


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

def colaborador():
    """ Colaborador para realizar uma venda e atender ao cliente
    Codigo / Nome Completo / CPF Valido / Endereco: AV ou Rua, Complemento, Numero da residencia /
    Numero de contato / Email / Cargo na empresa / Setor / Usuario """

    novo_colaborador = Colaborador('Johnatan Licar','111.111.111-11','Rua x, QD y,Nº 0','Bairro Ruim','00000-000','(00)91111 1111','johnatanlicar@gmail.com','Programador','Imformatica','johnatanlicar')
    novo_colaborador.gravar()

def fornecedor():
    """ Aquele que fornerce produtos para a empresa
    Nome Razao Social / CNPJ Valido / Endereco AV. ou Rua, Complemento, Numero(residencia/Predio/Escritorio) / 
    Numero de Contato / Email / Web Site(Opcional) / Categoria / Nome do Promotor Atual / Numero de contato do Promotor"""

def produto():
    """ Produto de um Fornecedor e pronto para venda ao cliente
    Descrica do Produto / Quantidade em estoque / Valor de Venda / Categoria / Nome do fornecedor /
     """

def usuario():
    """ Usuario que vai estar utilizando o sistema
    Nome de usuario / Senha / Permicoes (Adm,Comum,Basico) / Codigo do Colaborador / Nome do Colaborador """
