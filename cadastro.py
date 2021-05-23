from os import getcwd
from csv import DictWriter
from pathlib import Path

def Gravar(src,dados):
    local = f'{getcwd()}/db/{src}.csv'
    verifica = Path(local)
    l = None
    if verifica.exists():
        l = 'a'
        if src == 'dbcli':
            with open(local, l) as clientes:
                grava_csv = DictWriter(clientes, fieldnames=['NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO'])
                grava_csv.writerow({'NOME':dados[0],'CPF':dados[1],'ENDERECO':dados[2],'BAIRRO':dados[3],'CEP':dados[4],'CELULAR':dados[5],'EMAIL':dados[6],'PROFICAO':dados[7]})
    else:
        l = 'w'
        if src == 'dbcli':
            with open(local, l) as clientes:
                    grava_csv = DictWriter(clientes, fieldnames=['NOME','CPF','ENDERECO','BAIRRO','CEP','CELULAR','EMAIL','PROFICAO'])
                    grava_csv.writeheader()
                    grava_csv.writerow({'NOME':dados[0],'CPF':dados[1],'ENDERECO':dados[2],'BAIRRO':dados[3],'CEP':dados[4],'CELULAR':dados[5],'EMAIL':dados[6],'PROFICAO':dados[7]})
    
def Cliente():
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
    cadcli = [nome,cpf,endereco,bairro,cep,numTel,email,prof]
    Gravar("dbcli",cadcli)
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

Cliente()
