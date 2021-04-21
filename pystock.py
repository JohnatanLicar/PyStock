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

def PrintOpInvalida():
    print(f"\x1b[31;1m Opcao nao existe ou invalida, por favor verifique a opcao correta e tente novamente\x1b[0m")

def SubOpcao(selecao,texto):
    if selecao == "Cadastro":
        return f"Janela para Cadastro de {texto}"
    elif selecao == "Consultar":
        return f"Janela para Consulta de {texto}"
    elif selecao == "Alterar/Deletar":
        return f"Janela para Alterar/Deletar de {texto}"
    
        

def MenuPrinc(sair):
    while sair == 1:
        titulo("Menu Principal - PyStock")            
        print("""
            1 - Cadastro
            2 - Consultar
            3 - Alterar/Deletar
            0 - Sair""")
        resp = input(">>> ")
        valida = TrataResp(resp)
        if valida is None:
            PrintOpInvalida()
        elif valida == 0:
            print("Adeus, Volte sempre")          
            sair = 0
            break
        elif valida == 1:
            while True:
                    titulo("Menu Cadastro")
                    lista()
                    resp = input(">>> ")
                    cadastro = TrataResp(resp)
                    if cadastro is None:
                        PrintOpInvalida()
                    elif cadastro == 0:
                        sair = 1
                        break
                    elif cadastro == 1:
                        print(SubOpcao("Cadastro","Clientes"))
                        import Cadastros.cadcli as CadCli
                        CadCli
                        sair = 0
                        break
                    elif cadastro == 2:
                        print(SubOpcao("Cadastro","Usuarios"))
                        import Cadastros.caduser as CadUser
                        CadUser
                        sair = 0
                        break
                    elif cadastro == 3:
                        print(SubOpcao("Cadastro","Fornecedor"))
                        import Cadastros.cadforn as CadForn
                        CadForn
                        sair = 0
                        break
                    elif cadastro == 4:
                        print(SubOpcao("Cadastro","Produtos"))
                        import Cadastros.cadprod as CadProd
                        CadProd
                        sair = 0
                        break
                    elif cadastro == 5:
                        print(SubOpcao("Cadastro","Colaborador"))
                        import Cadastros.cadcolab as CadColab
                        CadColab
                        sair = 0
                        break
                    else:
                        PrintOpInvalida()

        
        elif valida == 2:
            while True:
                titulo("Menu Consultar")
                lista()
                resp = input(">>> ")
                consulta = TrataResp(resp)
                if consulta is None:
                    PrintOpInvalida()
                elif consulta == 0:
                    sair = 1
                    break
                elif consulta == 1:
                    print(SubOpcao("Consultar","Clientes"))
                    sair = 0
                    break
                elif consulta == 2:
                    print(SubOpcao("Consultar","Usuarios"))
                    sair = 0
                    break
                elif consulta == 3:
                    print(SubOpcao("Consultar","Fornecedor"))
                    sair = 0
                    break
                elif consulta == 4:
                    print(SubOpcao("Consultar","Produtos"))
                    sair = 0
                    break
                elif consulta == 5:
                    print(SubOpcao("Consultar","Colaborador"))
                    sair = 0
                    break
                
        elif valida == 3:
            while True:
                titulo("Menu Alterar/Deletar")
                lista()
                resp = input(">>")
                altdel = TrataResp(resp)
                if altdel is None:
                    PrintOpInvalida()
                elif altdel == 0:
                    sair = 1
                    break
                elif altdel == 1:
                    print(SubOpcao("Alterar/Deletar","Clientes"))
                    sair = 0
                    break
                elif altdel == 2:
                    print(SubOpcao("Alterar/Deletar","Usuarios"))
                    sair = 0
                    break
                elif altdel == 3:
                    print(SubOpcao("Alterar/Deletar","Fornecedor"))
                    sair = 0
                    break
                elif altdel == 4:
                    print(SubOpcao("Alterar/Deletar","Produtos"))
                    sair = 0
                    break
                elif altdel == 5:
                    print(SubOpcao("Alterar/Deletar","Colaborador"))
                    sair = 0
                    break
            
        else:
            PrintOpInvalida()


MenuPrinc(1)
                