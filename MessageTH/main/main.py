# -*- coding: utf-8 -*-


'''

Por Galileu Santos - Universidade Federal de Sergipe

'''
import re
from errors.nameError import NameE
from errors.syntaxError import SyntaxE
from errors.systemError import SystemE
from errors.valueError import ValueE
from errors.typeError import TypeE
from errors.EOFError import EOFE
from errors.indentationError import IndentationE
from errors.indexError import IndexE
from errors.attributeError import AttributeE
from errors.keyError import KeyE
from errors.unboundLocalError import UnboundLocalE
from errors.fileNotFoundError import FileNotFoundE
from errors.zeroDivisionError import ZeroDivisionE
from errors.tabError import TabE
from errors.importError import ImportE
from errors.permissionError import PermissionE
from errors.overflowError import OverflowE
from errors.unicodeDecodeError import UnicodeDecodeE
from errors.calendarIllegalMonthError import IllegalMonthE
from errors.unicodeEncodeError import UnicodeEncodeE
from errors.IOError import IOE

'''
from errors.attributeError import AttributeE
from errors.indentationError import IndentationE
'''

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
                        print "Erro na linha "+self.line
                        if not self.code == "": print "No trecho de código:"
                        print self.code,
                        print "Descrição: "+l[i]
                        foundMsg = True
                        break
                        #continue#encerra a busca pela cadeira
            if not foundMsg: 
                print "Erro não encontrado!"
        else:
            print "Tipo de erro não encontrado!"


'''
    Carregando a mensagem de erro
'''        
            
filename = "..\\file\\baseErros.txt"
list_begin = []
encontrou = False
''' Separando a mensagem em linhas e identificando a linha que contém a string Error '''
with open(filename) as f:
    for line in f:
        list_begin.append(line)

matriz_errors = []
linha = []
for i in list_begin:
    linha.append(i)
    if "Error" in i and not "sys.excepthook" in i and not "raise" in i:
        matriz_errors.append(linha)
        linha = []
        
if not matriz_errors:
    print "Mensagem de erro fora do padrão!"
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
                    cod.append(i)
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
            
            iniciar.chainResponsability()
        except:
            print "Mensagem de erro fora do padrão!"
        