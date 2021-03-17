print("# "*25)
print("Bem-vindo ao PyStock - Estoques de Produtos".center(50))

def titulo(texto):
    print("# "*25)
    print(texto.center(50))
    print("# "*25)
def lista():
    print("""
    1 - Cliente
    2 - Usuarios
    3 - Fornecedor
    4 - Produtos
    5 - Colaborador
    0 - Retornar ou Menu""")
def TrataResp(opcao):
    while True:
        if opcao.isnumeric():
            return int(opcao)
        else:
            return None
def MenuPrinc():
    while True:
        titulo("Menu Principal - PyStock")            
        print("""
            1 - Cadastro
            2 - Consultar
            3 - Alterar/Deletar
            0 - Sair""")
        resp = input(">>> ")
        valida = TrataResp(resp)
        if valida is None:
            print("Opcao invalida")
        elif valida == 0:
            print("Adeus, Volte sempre")          
            break
        elif valida == 1:
            while True:
                    titulo("Menu Cadastro")
                    lista()
                    resp = input(">>> ")
                    cadastro = TrataResp(resp)
                    if cadastro is None:
                        print("Opcao invalida, por favor escolha uma opcao valida!")
                    elif cadastro == 0:
                        MenuPrinc()
        
        elif valida == 2:
            while True:
                titulo("Menu Consultar")
                lista()
                resp = input(">>> ")
                consulta = TrataResp(resp)
                if consulta is None:
                    print("Opcao invalida, por favor escolha uma opcao valida!")
                elif consulta == 0:
                    MenuPrinc()
                
        elif valida == 3:
            titulo("Menu Alterar/Deletar")
            lista()
            resp = input(">>")
            altdel = TrataResp(resp)
            if altdel is None:
                print("Opcao invalida, por favor escolha uma opcao valida!")
            elif altdel == 0:
                MenuPrinc()
            
        else:
            print(f"\x1b[31;1m Opcao nao existe!\x1b[0m")


MenuPrinc()
                

