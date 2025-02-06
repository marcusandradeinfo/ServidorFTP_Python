from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import socket
import logging
import threading 

class ServerFtp():
    def __init__(self):
        self.ip = self.obter_ip()

    def obter_ip(self):
        try:
            # Conectar a um host externo para determinar o IP local
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))  # IP público do Google DNS
                ip = s.getsockname()[0]    # Obtém o endereço local usado na conexão
            return ip
        except Exception as e:
            print(f"Erro ao obter o IP local: {e}")
            return None

    def start_server(self,ip,porta,usuario,senha):
        try:
            caminho_xml = os.getcwd()

            # Configurar a autorização de usuários
            authorizer = DummyAuthorizer()
            authorizer.add_user(usuario, senha, caminho_xml, perm="elradfmw")  # Permissões: 'elradfmw'
            authorizer.add_anonymous(caminho_xml, perm="elradfmw")  # Permitir usuários anônimos (opcional)

            # no escrever log
            logging.basicConfig(level=logging.CRITICAL)
            
            # Configurar o manipulador de conexões
            handler = FTPHandler
            handler.authorizer = authorizer

            # Criar o servidor FTP
            self.server = FTPServer((ip, porta), handler)  # Escuta na porta 2121
            print(self.server)

            self.server.max_cons = 10
            self.server.max_cons_per_ip = 5

            # Iniciar o servidor em uma nova thread
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            # self.server.serve_forever()
            result_servidor = f"Servidor FTP iniciado: Ip: {ip}, Porta: {porta}, Usuário: {usuario}, Senha: {senha} "
            print(self.server)
            # return result_servidor
            
        except Exception as e:
            result_servidor = f"Erro ao iniciar servidor FTP: {e}"
            return result_servidor

    def stop_server(self):
        try:
            print(self.server)
            if self.server is not None and self.server_thread.is_alive():
                self.server.close_all()
                self.server_thread.join()
            else:
                result_servidor = "Nenhum servidor FTP em execução para parar."
            return result_servidor
        except Exception as e:
            result_servidor = f"Erro ao parar servidor FTP: {e}"
            return result_servidor
        
a = ServerFtp()
a.start_server('192.168.1.1',2121,'admin','admin')
a.stop_server()