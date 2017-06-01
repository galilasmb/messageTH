# -*- coding: utf-8 -*-

import re
import sys
from nameError import NameE
from syntaxError import SyntaxE
from systemError import SystemE
from valueError import ValueE
from typeError import TypeE
from EOFError import EOFE
from indentationError import IndentationE
from indexError import IndexE
from attributeError import AttributeE
from keyError import KeyE
from unboundLocalError import UnboundLocalE
from fileNotFoundError import FileNotFoundE
from zeroDivisionError import ZeroDivisionE
from tabError import TabE
from importError import ImportE
from permissionError import PermissionE
from overflowError import OverflowE
from unicodeDecodeError import UnicodeDecodeE
from calendarIllegalMonthError import IllegalMonthE
from unicodeEncodeError import UnicodeEncodeE
from IOError import IOE
from bottle import run, post, request, debug

class Main(object):
    type = ""
    msg = ""
    line = ""
    code = ""
    
    def __init__(self, typ, msg, line, code):
        self.type = typ
        self.msg = msg
        self.line = line
        self.code = code
        
    def chainResponsability(self):   
              
        ''' Cadeia de Busca '''
        chain = [SyntaxE(self.msg).getErros(), SystemE(self.msg).getErros(), NameE(self.msg).getErros(),
                 ValueE(self.msg).getErros(), TypeE(self.msg).getErros(), EOFE(self.msg).getErros(),
                 IndentationE(self.msg).getErros(), IndexE(self.msg).getErros(), AttributeE(self.msg).getErros(),
                 KeyE(self.msg).getErros(), UnboundLocalE(self.msg).getErros(), FileNotFoundE(self.msg).getErros(),
                 ZeroDivisionE(self.msg).getErros(), TabE(self.msg).getErros(), ImportE(self.msg).getErros(),
                 PermissionE(self.msg).getErros(), OverflowE(self.msg).getErros(), UnicodeDecodeE(self.msg).getErros(),
                 IllegalMonthE(self.msg).getErros(), UnicodeEncodeE(self.msg).getErros(), IOE(self.msg).getErros()]
              
        foundType = False #Se encontrar a classe do tipo
        foundMsg = False #Se encontrar a mensagem de erro
        
        listError = [] #lista dos erros ao identificar a classe
        
        '''
            Cadeia das classes de erros, verificando se algum casa com a entrada
            Caso case, é passado a lista de erros deste tipo
        
        '''
        retorno = []
        for i in chain:
            if self.type in i:
                listError = i[self.type]
                foundType = True
                break
                #continue #encerra a busca pela cadeira
                
        ''' Se encontrou o tipo do erro da entrada
            
            Cadeia de erros, verificando se algum da cadeia casa com a entrada
            Caso case, é chamado o método correspondente que transforma a mensagem de erro
            
        '''
        
        if foundType:
            for l in listError:
                for i in l.keys():
                    if i in self.msg:
                        retorno.append("\nErro na linha "+self.line+"\n")
                        if not self.code == "": retorno.append("No trecho de código:\n")
                        retorno.append(self.code+"\n")
                        retorno.append("Descrição: "+l[i]+"\n")
                        foundMsg = True
                        break
                        #continue#encerra a busca pela cadeira
            if not foundMsg:
                #retorno.append("400")
                print self.msg
                retorno.append("Erro não encontrado!")
                
        else:
            #retorno.append("400")
            print self.msg                
            retorno.append("Tipo de erro não encontrado!")
            
        
        return ''.join(retorno)

   
def execute(errorMsg):
    
    '''
        Carregando a mensagem de erro
    '''        
    
    list_begin = []
    
    ''' Separando a mensagem em linhas e identificando a linha que contém a string Error
    filename = "..\\file\\baseErros.txt"
    with open(filename) as f:'''
    
    try:
        for line in errorMsg.split("\n"):
            list_begin.append(line)
    except:
        print errorMsg+sys.exc_info()[0]
        return "Mensagem de erro fora do padrão!"
        
    matriz_errors = []
    linha = []
    for i in list_begin:
        linha.append(i)
        if "Error" in i and not "sys.excepthook" in i and not "raise" in i:
            matriz_errors.append(linha)
            linha = []
    finalMsg = ""    
    if not matriz_errors:
        #return "400"
        print errorMsg+sys.exc_info()[0]
        return "Mensagem de erro fora do padrão!"
    else: 
        for list_erros in matriz_errors:
            list_new = []
            
            ''' Separando o tipo do erro e sua mensagem '''
            error = list_erros[::-1][0]
            classError = error.split(":")
            list_new.append(classError[0])
            list_new.append(re.sub(str(classError[0]+":"), "", error))
            
            ''' Pegando o código fonte '''
            
            entrou = False
            cod = []
            try:
                for i in list_erros[::-1]:
                    if "File \"" not in i and not entrou:
                        cod.append(i+"\n")
                    else:
                        entrou = True
                str_code = ''.join(cod[1:][::-1])  
            
            except:
                cod = ""
            
            
            ''' Pegando a linha que ocorreu o erro'''
            linha = ""
            for f in list_erros:
                try:
                    if "File \"" in f:            
                        linha = f            
                except:
                    continue
    
            ''' Identificando o número da linha que ocorreu o erro '''
            numberLine = ""
            try:
                l = linha.split(",")[1]
                
                if "line" in l:
                    for char in l:
                        if char.isdigit():
                            numberLine+=char
                else:
                    numberLine = "X"
                ''' Executando a chamada da cadeia com o tipo do erro e sua mensagem'''
                
                '''print numberLine
                print str_code
                print list_new[0]+":"+list_new[1]'''
                
                iniciar = Main(list_new[0], list_new[1], numberLine, str_code)
                finalMsg += iniciar.chainResponsability()
            except:
                #return "400"
                print errorMsg+sys.exc_info()[0]
                return "Mensagem de erro fora do padrão!"
        return finalMsg

def checkMsg(msg):
    return (True if "\n" in msg and msg is not None else False)
        
@post('/')
def postMsg():
    errorMsg = request.forms.get('errorMsg')
    if checkMsg(errorMsg):
        return execute(errorMsg)
    else:
        print errorMsg
        return "Mensagem de erro fora do padrão!"

if __name__ == '__main__':    
    debug(True)
    run(host='localhost', port=8080, debug=True, reloader=True)


