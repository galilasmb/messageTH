# -*- coding: utf-8 -*-

class SystemE(object):

    msg = ""
    id = "SystemError"
    erro1 = {}
    
    def __init__(self, msg):
        self.msg = msg
        self.erro1 = {"E:Unable to read":self.func1()}
    
    
    '''    Funções    '''
        
    def func1(self):
        return """Houve erro de permissão do sistema para leitura do arquivo no caminho E:Unable to read /etc/apt/apt.conf.d/ - ao abrir o diretório e executar os testes no servidor."""

    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.erro1]}

    
