from Controller import serverftp


def Validarip():
    print("estou aqui")

def BuscarIP():
    ip = serverftp.ServerFtp()
    ip = ip.obter_ip()
    print(ip)
    return ip
