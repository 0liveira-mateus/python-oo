def cria_camera(nome, endereco_ip, senha):
    camera = {"marca":nome, "ip":endereco_ip, "senha":senha}
    return camera

tekpix = cria_camera('Samsung', 321, 654)

def confirm_ip(camera, ip):
    return camera['ip'] == ip

escolha_da_camera = input("Qual a marca da camera deseja acessar?").strip().upper()


def validacao_senha(camera, senha):
    return camera['senha'] == senha


if(escolha_da_camera == tekpix['marca'].strip().upper()):
    print("Acessando {}".format(tekpix['marca']))
    senha_de_Acesso = int(input("Qual a senha de acesso da camera {} ? ".format(tekpix['marca'])))
    if validacao_senha(tekpix, senha_de_Acesso) == True:
        print("Acesso Permitido")
    else:
        print("Acesso Negado")


