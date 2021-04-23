from os import getcwd
def Gravar(src,dados):
    local = f'{getcwd()}/db/{src}.txt'
    gravar = open(local, 'a')
    gravar.write(f"{dados}\n")
    gravar.close()

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

    endRuaAV = input(f"Digite o Endereco do Cliente\nRua/AV >>> ")
    endComp = input("Complemento >>> ")
    endNum = input("Numero >>> ")
    numTel = input(f"Digite um numero para contato\n>>> ")
    email = input(f"Digite o email\n>>> ")
    prof = input(f"Digite sua Proficao\n>>> ")
    cadastro = (f'{nome}, {cpf}, {endRuaAV}, {endComp},{endNum}, {numTel}, {email}, {prof}')
    Gravar("dbcli",cadastro)
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


