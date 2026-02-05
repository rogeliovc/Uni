import re

class Automata:
    def __init__(self):
        self.estado = 'inicio'
        # Caracteres prohibidos
        self.prohibidos = {'$', '#', '(', '@'} 

    def transicion(self, caracter):
        if self.estado == 'inicio':
            # Debe iniciar con letra o guion bajo
            if caracter.isalpha() or caracter == '_':
                self.estado = 'valido'
            else:
                self.estado = 'invalido'
        elif self.estado == 'valido':
            if caracter.isalnum() or caracter in '_.:' and caracter not in self.prohibidos:
                self.estado = 'valido'
            else:
                self.estado = 'invalido'

    def validar_variable(self, nombre):
        self.estado = 'inicio'
        for caracter in nombre:
            self.transicion(caracter)
            if self.estado == 'invalido': return False
        return self.estado == 'valido'

class AnalizadorLexico:
    def __init__(self):
        self.automata = Automata()
        # Diccionario de lexemas
        self.tokens_fijos = {
            '+': 'TKN OPADD', '-': 'TKN OPSUB', '*': 'TKN OPMULT', '/': 'TKN OPDIV',
            '(': 'TKN PAREN_A', ')': 'TKN PAREN_C', '[': 'TKN CORAPER', ']': 'TKN CORCIERRE',
            '=': 'TKN ASIGN', '"': 'TKN COMILLA'
        }
        # Patrón regex para separar la expresion
        self.patron = r'[a-zA-Z]:|\d+\.\d+|[a-zA-Z_][\w.]*|\d+|[^\w\s]'

    def procesar(self, entrada):
        # Genera la lista expresiones separadas
        partes_de_la_expresion = re.findall(self.patron, entrada)
        print(f"Entrada: {entrada}\n")
        
        #Guarda la expresion clasificada
        resultado = []
        
        for l in partes_de_la_expresion:
            # Limpieza de espacios parecido a Trim() (considerar quitar o trabajar para cuando el usuario meta espacios sin querer cache errores y no los elimine, ya que esatria mal)
            l = l.strip()
            # ignorar espacios vacíos
            if not l: continue

            # Clasificación segun el TKN
            if l in self.tokens_fijos:
                tipo = self.tokens_fijos[l]
            elif l.replace('.', '', 1).isdigit():
                tipo = "TKN NUM"
            else:
                if self.automata.validar_variable(l):
                    tipo = "TKN ID"
                else:
                    tipo = "TKN ERROR"
            
            print(f"<{tipo}, {l}>")
            resultado.append(l)
        
        print(f"\nTokens encontrados:{resultado}")

prueba = AnalizadorLexico()
prueba.procesar('C:/Users/Ramiro/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Ramiro/Desktop/COMPILADORES ACTIVIDADES/act3_jasn.py"')