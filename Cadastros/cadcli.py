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
bdclientes = list()
bdclientes.append(cadastro)
print(type(cadastro))
print(cadastro[:1])
print(bdclientes)
from os import getcwd
local = f'{getcwd()}/db/dbcli.txt'
with open(local, "w") as gravar:
    gravar.writelines(bdclientes)

