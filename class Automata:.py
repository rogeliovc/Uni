class Automata:
    def __init__(self):
        self.estado = 'inicio'
        self.prohibidos = {'$', '#', '/', '(', '@'}

    def transicion(self, caracter):
        if self.estado == 'inicio':
            if caracter.isalpha() or caracter == '_':
                self.estado = 'valido'
            else:
                self.estado = 'invalido'
        
        elif self.estado == 'valido':
            # Si ya es válido, solo se invalida si encuentra un prohibido
            if caracter in self.prohibidos:
                self.estado = 'invalido'
            elif caracter.isalnum() or caracter == '_':
                self.estado = 'valido' 
            else:
                self.estado = 'invalido'

    def validar_variable(self, nombre):
        self.estado = 'inicio' # Reiniciar estado para cada validación
        for i, caracter in enumerate(nombre):
            self.transicion(caracter)
            
            if self.estado == 'invalido':
                return f"Error en la posición {i}. El carácter '{caracter}' no es válido"
        
        if self.estado == 'valido':
            return "El nombre de la variable es válido"
        else:
            return "Error: El nombre de la variable no puede estar vacío"

# --- Pruebas ---
automata = Automata()
variables_test = ["variable1","_variable", "1variable", "var-name", "var_name","vae123","varName","varName_2","variable$"]

for v in variables_test:
    resultado = automata.validar_variable(v)
    print(f"Probando {v} `{resultado}`")
