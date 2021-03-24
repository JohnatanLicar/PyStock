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

