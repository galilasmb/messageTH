# -*- coding: utf-8 -*-

class TypeE(object):

    msg = ""
    id = "TypeError"
    unsupportedOperand = {}
    objectNotIterable = {}
    unorderableTypes = {}
    objectNoAttribute = {}
    notAllArgs = {}
    objectNotCallable = {}
    objectNotSubscriptable = {}
    cantMultiplyStr = {}
    objectCannotInteger = {}
    argumentMustNumber = {}
    objectToImplicitly = {}
    listMustIntegers = {}
    hasNoLen = {}
    aBytesObjectNumber = {}
    cannotConcatenate = {}
    integerArgsExpected = {}
    aFloatRequired = {}
    floatArgumentRequired = {}
    cantConvertComplex = {}
    takesExactly = {}
    formatANnumber = {}
    notFormatString = {}
    canOnlyConcatenate = {}

    def __init__(self, msg):
        self.msg = msg
        self.unsupportedOperand = {"unsupported operand":self.unsupportedOperandFunc()}
        self.objectNotIterable = {"object is not iterable":self.objectNotIterableFunc()}
        self.unorderableTypes = {"unorderable types":self.unorderableTypesFunc()}
        self.objectNoAttribute = {"object has no attribute":self.objectNoAttributeFunc()}
        self.notAllArgs = {"not all arguments converted during string formatting":self.notAllArgsFunc()}
        self.objectNotCallable = {"object is not callable":self.objectNotCallableFunc()}
        self.objectNotSubscriptable = {"object is not subscriptable":self.objectNotSubscriptableFunc()}
        self.cantMultiplyStr = {"can't multiply sequence by non-int of type":self.cantMultiplyStrFunc()}
        self.objectCannotInteger = {"object cannot be interpreted as an integer":self.objectCannotIntegerFunc()}
        self.argumentMustNumber = {"argument must be a string or a number":self.argumentMustNumberFunc()}
        self.objectToImplicitly = {"object to str implicitly":self.objectToImplicitlyFunc()}
        self.listMustIntegers = {"list indices must be integers":self.listMustIntegersFunc()}
        self.hasNoLen = {"has no len()":self.hasNoLenFunc()}
        self.aBytesObjectNumber = {"a bytes-like object or a number":self.aBytesObjectNumberFunc()}
        self.cannotConcatenate = {"cannot concatenate":self.cannotConcatenateFunc()}
        self.integerArgsExpected = {"integer end argument expected":self.integerArgsExpectedFunc()}
        self.aFloatRequired = {"a float is required":self.aFloatRequiredFunc()}
        self.floatArgumentRequired = {"float argument required":self.floatArgumentRequiredFunc()}
        self.cantConvertComplex = {"can't convert complex to":self.cantConvertComplexFunc()}
        self.takesExactly = {"takes exactly":self.takesExactlyFunc()}
        self.formatANnumber = {"format: a number is required":self.formatANnumberFunc()}
        self.notFormatString = {"not enough arguments for format string":self.notFormatStringFunc()}
        self.canOnlyConcatenate = {"can only concatenate":self.canOnlyConcatenateFunc()}
        
        '''self. = {"":self.()}
        self. = {"":self.()}
        self. = {"":self.()}
        self. = {"":self.()}
        self. = {"":self.()}
        self. = {"":self.()}
        self. = {"":self.()}
        '''
        

    '''    Funções    '''
        
    def unsupportedOperandFunc(self):
        try:
            doisP = self.msg.split()[::-1]
            type1 = doisP[0]
            type2 = doisP[2]
            op = doisP[3].replace(":", "")            
            return """A operação """+op+""" não é suportada para os tipos """+type1+""" e """+type2+""". Verifique os tipos e suas operações."""
        except:
            return """"""
        
    
    def objectNotIterableFunc(self):
        try:
            typ = self.msg.split("'")[1]
            return """O objeto do tipo """+typ+""" não é iterável, é apenas uma literal, verifique se não é necessário o uso de uma lista ou o comando range()."""    
        except:
            return ""
    
    def unorderableTypesFunc(self):
        try:
            return """Os tipos não são comparáveis, por isso não é possível realizar a comparação: """+self.msg.split(":")[1]+""". Modifique-os para que sejam do mesmo tipo."""    
        except:
            return ""

    
    def objectNoAttributeFunc(self):
        try:
            typ = self.msg.split("'")
            type1 = typ[1]
            type2 = typ[3]
            message = ""
            if "getitem" in type2:
                message = """(não posso acessar item com o tipo """+type1+")." 
            return """O objeto do tipo """+type1+""" não tem nenhum atributo do tipo """+type2+""" """+message
        except:
            return ""

    
    def notAllArgsFunc(self):
        return """Nem todos os argumentos foram convertidos durante a formatação. Verifique a formatação, os tipos das variáveis e argumentos."""    


    
    def objectNotCallableFunc(self):
        try:
            return self.msg.split("'")[1]+""" não é um objeto que possa ser invocado/chamado como uma função, verifique o uso dos () neste objeto. Para acessar um item use [ ], exemplo: [ item ]."""    
        except:
            return ""
    
    def objectNotSubscriptableFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não pode ser acessado utilizando posição de memória através do uso de [], retire os colchetes."""    
        except:
            return ""
    

    def cantMultiplyStrFunc(self):
        try:
            return """Não é possível multiplicar uma sequência não numérica pelo tipo """+self.msg.split("'")[::-1][1]+""", corriga o problema convertendo para o tipo requerido, utilize o comando 'type'(). """    
        except:
            return ""
    
    
    def objectCannotIntegerFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não pode ser interpretado como um inteiro, verifique os tipos para corrigir o problema."""
        except:
            return ""
    
    
    def argumentMustNumberFunc(self):
        try:
            return """A função"""+self.msg.split("(")[0]+"""() deve ter o argumento do tipo string ou número, não o tipo """+self.msg.split("'")[::-1][1]+"""."""
        except:
            return ""
    
    
    def objectToImplicitlyFunc(self):
        try:
            return """Não é possível converter o tipo """+self.msg.split("'")[2]+""" implicitamente para o tipo str, ou seja, por mais que seja compreensível sua conversão, não é possível."""
        except:
            return ""
    
    
    def listMustIntegersFunc(self):
        try:
            return """Os índices de uma lista deve ser do tipo inteiro, não do tipo """+self.msg.split(",")[1].replace(" not ", "")
        except:
            return ""
        
    
    def hasNoLenFunc(self):
        try:
            return """O objeto do tipo """+self.msg.split("'")[1]+""" não tem tamanho, por isso não é possível utilizar a função len()."""
        except:
            return ""

    
    def aBytesObjectNumberFunc(self):
        try:
            return """O argumento da função"""+self.msg.split("(")[0]+"""() deve ser uma seqüência de caracteres ou bytes - como um objeto ou um número, não """+self.msg.split("'")[::-1][1] 
        except:
            return ""
    
    
    def cannotConcatenateFunc(self):
        try:
            t = self.msg.split("'")
            return """Não é possível concatenar os objetos do tipo """+t[1]+""" e """+t[3]
        except:
            return ""
    
    
    def integerArgsExpectedFunc(self):
        try:
            typ = self.msg.split(",")[1].replace(" got ","")
            return """O argumento do comando range() esperava que fosse um objeto do tipo inteiro, não do tipo """+typ
        except:
            return ""

    
    def aFloatRequiredFunc(self):
        return """O código esperava por um objeto do tipo float."""    

    
    def floatArgumentRequiredFunc(self):
        try:
            typ = self.msg.split(",")[1].replace(" not ", "")
            return """É necessário que o argumento seja do tipo  float, não do tipo """+typ
        except:
            return ""

    
    def cantConvertComplexFunc(self):
        try:
            typ = self.msg.split(" ")[-1]
            return """Não é possível converter um número complexo para um número do tipo """+typ
        except:
            return ""

    
    def takesExactlyFunc(self):
        try:
            sep = self.msg.split("(")
            has = sep[-1].replace(" given)", "")
            func = sep[0]
            typ = self.msg.split(" ")[4]
            args = ""
            args = " argumento" if "1" in typ or "one" in typ else " argumentos"
            typ = "1" if typ=="one" else typ
            go = "foi passado " if "1" in has or "0" in has else "foram passados "  
            return """A função"""+func+"""() necessita de """+typ+args+""" e """+go+has
        except:
            return ""

    
    def formatANnumberFunc(self):
        try:
            typ = self.msg.split("not")[1]
            return """É necessário que o tipo a ser formatado seja um número, não o tipo"""+typ
        except:
            return ""

    
    def notFormatStringFunc(self):
        return """Os argumentos são insuficientes para formatar a string, verifique a quantidade de argumentos ou utilize parênteses para formatar em tuplas."""    

    
    def canOnlyConcatenateFunc(self):
        try:
            typ = self.msg.split("\"")[1]
            return """Não é possível concatenar o tipo """+typ+""" com uma lista, é necessário inserir este elemento, tente utilizar o comando append()."""
        except:
            return ""

    '''
    def (self):
        return """ """    


    def (self):
        return """ """    


    def (self):
        return """ """    


    def (self):
        return """ """    


    def (self):
        return """ """    


    def (self):
        return """ """    


    def (self):
        return """ """    

    '''
    '''    Criação do dicionário    '''
    
    def getErros(self):
        return {self.id:[self.unsupportedOperand, self.objectNotIterable, self.unorderableTypes, self.objectNoAttribute, self.notAllArgs,
                         self.objectNotCallable, self.objectNotSubscriptable, self.cantMultiplyStr, self.objectCannotInteger, 
                         self.argumentMustNumber, self.objectToImplicitly, self.listMustIntegers, self.hasNoLen, self.aBytesObjectNumber,
                         self.cannotConcatenate, self.integerArgsExpected, self.aFloatRequired, self.floatArgumentRequired, self.cantConvertComplex,
                         self.takesExactly, self.formatANnumber, self.notFormatString, self.canOnlyConcatenate]}

    
