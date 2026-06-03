class Lexico:
    def __init__(self, fuente, traza=False):
        self.traza = traza
        self.tokens = list(fuente.replace(";", " ; ").replace("{", " { ").replace("}", " } ").replace("(", " ( ").replace(")", " ) ").split())
        self.pos = 0
        self.linea = 1

    def tokenizar(self, fuente):
        return fuente.split()

    def siguienteToken(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

    def devuelveToken(self, token):
        self.pos -= 1

    def existeTraza(self):
        return self.traza

    def lineaActual(self):
        return self.linea


class GeneraCodigo:

    def code(self):
        print("Generando código para main")

    def end(self):
        print("Fin del código")

    def pusha(self, token):
        print(f"Push variable: {token}")

    def store(self):
        print("Almacenando valor")

    def load(self):
        print("Cargando variable")

    def input(self, token):
        print(f"Entrada para: {token}")

    def output(self, token):
        print(f"Salida de: {token}")

    def pushc(self, token):
        print(f"Push constante: {token}")

    def add(self):
        print("Suma")

    def neg(self):
        print("Negar")

    def mul(self):
        print("Multiplicación")

    def div(self):
        print("División")

    def mod(self):
        print("Módulo")


class Sintactico:

    def __init__(self, fuente, traza=False):
        self.lexico = Lexico(fuente, traza)
        self.generaCodigo = GeneraCodigo()

        if self.lexico.existeTraza():
            print("INICIO DE ANALISIS SINTACTICO")

        self.programa()

    def programa(self):
        if self.lexico.existeTraza():
            print("ANALISIS SINTACTICO: <PROGRAMA>")

        token = self.lexico.siguienteToken()

        if token == 'M':
            self.generaCodigo.code()
        else:
            self.errores(8)

        token = self.lexico.siguienteToken()

        if token != '{':
            self.errores(9)

        self.bloque()

        token = self.lexico.siguienteToken()

        if token == '}':
            self.generaCodigo.end()
        else:
            self.errores(2)

    def bloque(self):

        if self.lexico.existeTraza():
            print("ANALISIS SINTACTICO: <BLOQUE>")

        self.sentencia()
        self.otra_sentencia()

    def otra_sentencia(self):

        token = self.lexico.siguienteToken()

        if token == ';':
            self.sentencia()
            self.otra_sentencia()
        else:
            self.lexico.devuelveToken(token)

    def sentencia(self):

        token = self.lexico.siguienteToken()

        if token == '}':
            self.lexico.devuelveToken(token)
            return

        if token.isalpha() and token.islower():
            self.lexico.devuelveToken(token)
            self.asignacion()

        elif token == 'R':
            self.lectura()

        elif token == 'W':
            self.escritura()

        else:
            self.errores(6)

    def asignacion(self):

        if self.lexico.existeTraza():
            print("ANALISIS SINTACTICO: <ASIGNACION>")

        self.variable()

        token = self.lexico.siguienteToken()

        if token != '=':
            self.errores(3)

        self.expresion()
        self.generaCodigo.store()

    def variable(self):

        token = self.lexico.siguienteToken()

        if token.isalpha() and token.islower():
            self.generaCodigo.pusha(token)
        else:
            self.errores(5)

    def expresion(self):

        if self.lexico.existeTraza():
            print("ANALISIS SINTACTICO: <EXPRESION>")

        self.termino()
        self.mas_terminos()

    def termino(self):

        if self.lexico.existeTraza():
            print("ANALISIS SINTACTICO: <TERMINO>")

        self.factor()
        self.mas_factores()

    def mas_terminos(self):

        token = self.lexico.siguienteToken()

        if token == '+':
            self.termino()
            self.generaCodigo.add()
            self.mas_terminos()

        elif token == '-':
            self.termino()
            self.generaCodigo.neg()
            self.generaCodigo.add()
            self.mas_terminos()

        else:
            self.lexico.devuelveToken(token)

    def factor(self):

        token = self.lexico.siguienteToken()

        if token.isdigit():
            self.lexico.devuelveToken(token)
            self.constante()

        elif token == '(':
            self.expresion()
            token = self.lexico.siguienteToken()

            if token != ')':
                self.errores(4)

        else:
            self.lexico.devuelveToken(token)
            self.variable()
            self.generaCodigo.load()

    def mas_factores(self):

        token = self.lexico.siguienteToken()

        if token == '*':
            self.factor()
            self.generaCodigo.mul()
            self.mas_factores()

        elif token == '/':
            self.factor()
            self.generaCodigo.div()
            self.mas_factores()

        elif token == '%':
            self.factor()
            self.generaCodigo.mod()
            self.mas_factores()

        else:
            self.lexico.devuelveToken(token)

    def lectura(self):

        token = self.lexico.siguienteToken()

        if not token.isalpha():
            self.errores(5)

        self.generaCodigo.input(token)

    def escritura(self):

        token = self.lexico.siguienteToken()

        if not token.isalpha():
            self.errores(5)

        self.generaCodigo.output(token)

    def constante(self):

        token = self.lexico.siguienteToken()

        if token.isdigit():
            self.generaCodigo.pushc(token)
        else:
            self.errores(7)

    def errores(self, codigo):

        mensajes = {
            1: "ESPERABA ;",
            2: "ESPERABA }",
            3: "ESPERABA =",
            4: "ESPERABA )",
            5: "ESPERABA IDENTIFICADOR",
            6: "INSTRUCCION DESCONOCIDA",
            7: "ESPERABA CONSTANTE",
            8: "ESPERABA M DE MAIN",
            9: "ESPERABA {"
        }

        print(f"ERROR SINTACTICO {codigo}: {mensajes.get(codigo)}")
        exit()


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
    return contenido


if __name__ == "__main__":

    archivo = "entrada.txt"

    codigo_fuente = leer_archivo(archivo)

    Sintactico(codigo_fuente, True)