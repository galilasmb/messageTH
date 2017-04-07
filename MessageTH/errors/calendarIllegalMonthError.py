# -*- coding: utf-8 -*-

class IllegalMonthE(object):

    msg = ""
    id = "calendar.IllegalMonthError"
    erro1 = {}
    erro2 = {}

    def __init__(self, msg):
        self.msg = msg
        self.erro1 = {"erro att 1":self.func1()}
        self.erro2 = {"erro att 2":self.metodo2()}

    
    '''    Funções    '''
        
    def func1(self):
        return "erro 1: "+ self.msg


    def func2(self):
        return "erro 2"
    


    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.erro1, self.erro2]}

    
