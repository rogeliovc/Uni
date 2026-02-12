import re

class Automata:
    def __init__(self):
        self.estado = 'inicio'
        # Caracteres prohibidos
        self.prohibidos = {'$', '#', '(', '@'}
        # Tipos de datos válidos
        self.tipos_datos = {'int', 'double', 'str', 'bool'}
        self.variables_encontradas = set() 

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
    
    def es_tipo_dato_valido(self, token):
        return token.lower() in self.tipos_datos
    
    def get_descripcion_tipo(self, tipo):
        descripciones = {
            'int': 'tipo de dato entero corto',
            'double': 'tipo de dato entero largo',
            'str': 'tipo de dato cadena',
            'bool': 'tipo de dato booleano'
        }
        return descripciones.get(tipo.lower(), 'tipo de dato desconocido')
    
    def registrar_variable(self, variable):
        if variable in self.variables_encontradas:
            return True
        else:
            self.variables_encontradas.add(variable)
            return False 

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
        partes_de_la_expresion = re.findall(self.patron, entrada)
        print(f"Entrada: {entrada}\n")
        
        resultado = []
        
        for l in partes_de_la_expresion:
            # Limpieza de espacios parecido a Trim()
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
    
    def procesar_archivo_tokens(self, ruta_archivo):
        resultados = []
        
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
                
                for linea in lineas:
                    resultado = self.clasificar_linea_tokens(linea.strip())
                    if resultado:
                        resultados.append(resultado)
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_archivo}")
            return []
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []
            
        return resultados
    
    def clasificar_linea_tokens(self, linea):
        if not linea:
            return None
            
        tokens = re.findall(r'\w+|[^\w\s]', linea)
        
        if len(tokens) < 2:
            return f"{linea} // no identificado"
        
        if self.automata.es_tipo_dato_valido(tokens[0]):
            tipo_dato = tokens[0]
            
            for token in tokens[1:]:
                if self.automata.validar_variable(token):
                    variable = token
                    descripcion = self.automata.get_descripcion_tipo(tipo_dato)
                    
                    # Detectar ambigüedad
                    if variable in self.automata.variables_encontradas:
                        return f"{tipo_dato} {variable} // {descripcion}, ambigüedad con variable existente"
                    else:
                        self.automata.variables_encontradas.add(variable)
                        return f"{tipo_dato} {variable} // {descripcion}, variable {variable}"
        
        return f"{linea} // no identificado"

if __name__ == "__main__":
    contenido_prueba = """main(){
double x
int x2
2x str
Int !x
int x
int 2x
}"""
    
    nombre_archivo_prueba = "entrada_tokens.txt"
    with open(nombre_archivo_prueba, 'w') as f:
        f.write(contenido_prueba)
    
    analizador = AnalizadorLexico()
    resultados = analizador.procesar_archivo_tokens(nombre_archivo_prueba)
    
    print("Resultados del análisis:")
    for resultado in resultados:
        print(resultado)

#prueba = AnalizadorLexico()
#prueba.procesar('C:/Users/Ramiro/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Ramiro/Desktop/COMPILADORES ACTIVIDADES/act3_jasn.py"')