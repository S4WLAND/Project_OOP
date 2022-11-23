"""Importamos la librería sqlite3 y de esta librería importamos el control de errores de sqlite3 """
import sqlite3 # importar sqlite3
from sqlite3 import Error # importar el manejo de errores


#################################### CLASE MATERIAS CON SUS MÉTODOS ########################################################################
############################################################################################################################################  


class materias():
    '''
    Clase materias con sus métodos

    '''

# Método constructor

    def __init__(self):
        '''
        MÉTODO CONSTRUCTOR
        '''
        self.__codigo_materia = None
        self.__nombre = None
        self.__facultad_dicta = None
        self.__departamento_dicta = None
        self.__creditos = None
        self.__idioma = None



    def crear_tabla_materias(self, con): # función para la creación de la tabla materias
        '''
        Función que permite crear la tabla materias donde se almacena la información correspondiente a las materias.

        Args:
            con (clase): _description_
        '''
        cursor_obj = con.cursor() # creamos el objeto cursor para manipular la BDD
        cursor_obj.execute('CREATE TABLE IF NOT EXISTS materias(codigo_materia integer PRIMARY KEY,\
                            nombre text,\
                            facultad_dicta text,\
                            departamento_dicta text,\
                            creditos integer,\
                            idioma text)') # Creamos la tabla materias en la BDD con sus respectivas columnas y sus tipo de datos
        con.commit() # guardamos cambios en la BDD (datos permanentes)


    def leer_info_materias(self): # función para la captura de información
        '''
        Función que permite obtener la información de una materia para ser almacenada en la tabla materia

        Entradas:
            self.__nombre (char): captura del nombre de la materia
            sel.__facultad_dicta (char): captura del nombre de la facultad que dicta la materia
            self.__departamento_dicta (char): captura del nombre del departamento que dicta la materia
            self.__creditos (int): captura del total de créditos que tiene la materia
            self.__idioma (char): captura del idioma en que se dicta la materia
        
        Returns:
            materia (tuple): Tupla con la información obtenida de la nueva materia
        '''

        while True:
            try:
                self.__codigo_materia = int(input('codigo de la materia: ')) # captura del codigo de la materia
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')

        self.__nombre = input('nombre de la materia: ') # captura del nombre de la materia
        self.__facultad_dicta = input('facultad que dicta la materia: ') # captura de la facultad que dicta la materia
        self.__departamento_dicta = input('departamento que dicta la materia: ') #  captura del departamento que dicta la materia
        while True:
            try:
                self.__creditos = int(input('creditos de la materia: ')) # captura de los creditos de la materia
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un tipo de dato valido')

        self.__idioma = input('idioma en que se dicta la materia: ') # idioma de la materia
        materia = (self.__codigo_materia, self.__nombre, self.__facultad_dicta, self.__departamento_dicta, self.__creditos, self.__idioma) # tupla con las capturas de la materia
        return materia # retorno de los datos de la materia


    def insertar_materias(self, con, mi_mat): # función para inserción de la información capturada de la materia la la tabla materia en la BDD
        '''
        Función que permite insertar una materia con los datos obtenidos en la función leer_info_materias

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            mi_mat (tuple): tupla con la información obtenida en la función leer_info_materias

        '''        
        cursor_obj = con.cursor() # objeto cursor para manipular la BDD
        cursor_obj.execute("""INSERT INTO materias VALUES(?,?,?,?,?,?)""", mi_mat) # insertamos la captura de información en la tabla materias
        con.commit() # guardamos cambios en la BDD


    def insertar_materias_2(self,con): # función para la inserción de datos sin captura de información en la tabla materias
        '''
        Función que permite insertar una materia con valores por defecto

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
        
        Entradas: 
            cod (int): captura del codigo que desea asignarse para la materia
        '''      
        cursor_obj = con.cursor() # objeto cursor para manipular la BDD

        while True:
            try:
                cod = int(input('ingrese el codigo de la materia: ')) # captura del codigo de la materia
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')
        sent = f'INSERT INTO materias VALUES ({cod},"programación","ingeniería", "S&I", 3, "ingles")' #  creamos datos por defecto a insertar en la tabla materias
        cursor_obj.execute(sent) # ejecutamos la inserción de los datos por defecto en la tabla materias
        con.commit() # guardamos cambios en la BDD


    def consultar_info_materias(self,con): # consulta de información de una materia
        '''
        Función que permite consultar la información de una materia en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        Entradas:
            codigo_materia (int): captura del código de la materia que desea consultarse (debe estar en la tabla materias)

        Returns:
            Impresión que devuelve la información de la materia que se buscó
        '''
        cursor_obj = con.cursor() # objeto cursor para manipular la BDD
        codigo_materia = input('Codigo de la materia a consultar: ')
        consulta = "SELECT * FROM materias WHERE codigo_materia = '"+codigo_materia+"'" # creamos la consulta a hacerse a la BDD
        cursor_obj.execute(consulta) # ejecutamos la consulta
        filas = cursor_obj.fetchall()
        for fila in filas:
            print(f'\nInformacion de materia:\n\
    \n    Codigo: {fila[0]}\n\
    Nombre: {fila[1]}\n\
    Facultad: {fila[2]}\n\
    Departamento: {fila[3]}\n\
    Creditos: {fila[4]}\n\
    Idioma: {fila[5]}\n')

    def actualizar_materia(self, con, codigo_mat):# Actualización del idioma de una materia args = conexion, codigo_a_actualizar
        '''
        Función que permite actualizar el idioma en que se dicta una materia en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            codigo_mat (int): Código de la materia de la que se desea actualizar el idioma

        Entradas:
            nuevo_idioma (char): Captura del nuevo idioma que se asignará a la materia
        
        Returns:
            Impresión que devuelve la actualización que se ejecutó
        '''
        cursor_obj = con.cursor() # objeto cursor para manipular la BDD
        nuevo_idioma = input('Actualice el idioma en que se dicta: ') # capturamos el idioma para remplazar
        actualizar = 'UPDATE materias SET idioma = "'+nuevo_idioma+'" WHERE codigo_materia = "'+codigo_mat+'"' # creamos la petición de actualización del idioma
        cursor_obj.execute(actualizar) # ejecutamos la actualización del idioma
        print("El update que se ejecuta es: ", actualizar) # imprimimos el proceso realizado
        con.commit()


    def borrar_materia(self, con):
        '''
        Método que permite borrar una materia de la tabla materias

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
        
        Entradas:
            materia_borrar (int): Captura del código de la materia que desea borrarse

        Returns:
            Impresión que devuelve el delete que se ejecutó
        '''            
        cursor_obj = con.cursor()
        materia_borrar = input('Codigo de la materia a borrar: ') # captura de teclado del id de la materia
        borrar = 'DELETE FROM materias WHERE codigo_materia = "'+materia_borrar+'"' # consulta para borrar fila de la materia que coincida con el id capturado
        cursor_obj.execute(borrar)
        print("El delete que se ejecuta es: ", borrar) # impresión del proceso realizado
        con.commit() # guardado de cambios realizado en la BDD


    def promedio_tabla_materias(self, con):
        '''
        Método que permite calcular el promedio de los créditos de las materias registradas en la tabla

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        Returns:
            promedio (float): Promedio de los créditos de las materias actuales en la tabla.
        '''
        cursor_obj = con.cursor()
        cantidad_materias = "SELECT count(*) FROM materias" # consulta de selección de conteo de informacion en a la tabla materias
        cursor_obj.execute(cantidad_materias) # ejecución de consulta
        cant_materias = cursor_obj.fetchall() # cambiando el objeto a lista para su iteración
        print(cant_materias)
        for row in cant_materias: # iteración del la cantidad total de las materias
            cantidad = row[0]
            print('la cantidad es: ', cantidad) # impresión del dato cantidad
        sumatoria_creditos = 'SELECT sum(creditos) FROM materias' # consulta sumatoria de los creditos registrado en la tabla materias
        cursor_obj.execute(sumatoria_creditos) # ejecución de la consulta
        sum_creditos = cursor_obj.fetchall()
        print(sum_creditos)
        for row in sum_creditos:
            sumatoria = row[0]
            print('la sumatoria es: ', sumatoria)
        promedio = sumatoria/cantidad
        print(promedio)
############################################################################################################################################
############################################################################################################################################  



#################################### CLASE PERSONA CON SUS MÉTODOS #########################################################################
############################################################################################################################################  
class persona():
    '''
    clase gestora del objeto persona junto con sus propiedades y métodos
    '''
    def __init__(self):
        '''
        MÉTODO CONSTRUCTOR DE PERSONA
        '''
        self.__codigo = None
        self.__nombre = None
        self.__apellido = None
        self.__fechaNacimiento = None
        self.__procedencia = None
        self.__fotografia = None
    
    def set_leerInfoPersona(self, tipo_persona):
        '''Método para la captura de información del objeto persona

        Args:
            tipo_persona (string): string que determina de tipo de persona es

        Entradas:
            codigo (int): captura de id del objeto persona
            nombre (string): captura de nombre del objeto persona
            apellido (string): captura del apellido del objeto persona
            fechaNacimiento (string -formato fecha definido): captura de la fecha de nacimiento del objeto persona
            procedencia (string): captura del lugar de procedencia del objeto persona
            fotografia (binario): NO ESPECIFICADO
        '''
        while True: # bucle para la captura correcta de informacion
            try:
                self.__codigo = int(input(f"Identificación de {tipo_persona}: "))  # Se ingresa la identificación unica del estudiante
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')

        self.__nombre = input(f"Nombre de {tipo_persona}: ")  # Se ingresa el nombre
        self.__apellido = input(f"Apellido de {tipo_persona}: ") # Se ingresa el apellido

        while True: # bucle para la captura correcta de la fecha de nacimiento del objeto persona

            self.__fechaNacimiento = input('Fecha de nacimiento(dia/mes/año) de la forma **/**/**** : ').strip()

            if len (self.__fechaNacimiento) == 10:
                break
            else:
                print('MENSAJE: Debe ingresar la fecha de nacimiento de la forma mencionada.')

            print()

        self.__procedencia = input(f"Procedencia de {tipo_persona}: ") # Se ingresa la ciudad de origen
        self.__fotografia = input(f"Fotografía de {tipo_persona} : ") # entrada de la fotografia de la persona

    def get_info_persona(self):
        '''Método para obtener la información del objeto persona

        Returns:
            _tuple_: tupla con la información de las propiedades del objeto persona, en este caso sus características 
        '''
        return self.__codigo, self.__nombre, self.__apellido, self.__fechaNacimiento, self.__procedencia, self.__fotografia # return con la tupla
############################################################################################################################################
############################################################################################################################################ 


 
#################################### CLASE ESTUDIANTES CON SUS MÉTODOS #####################################################################
############################################################################################################################################         
class estudiantes(persona):
    '''clase gestora de registro de la información de estudiantes

    Args:
        persona (Clase -- padre): clase persona con sus propiedades y métodos
    '''
    def __init__(self):
        '''
        MÉTODO CONSTRUCTOR DE ESTUDIANTES
        '''
        self.__carrera = None
        self.__fechaIngreso = None
        self.__cantidadMatriculas = None
        self.__correo = None

    def crearTablaEstudiante(self, con): # creación de la tabla estudiante
        '''Método creador de la tabla estudiante

        Args:
            con (Class): sqlite3 connection
        '''
        cursorObj = con.cursor() # Objeto cursor para manejar la BDD
        cursorObj.execute("CREATE TABLE IF NOT EXISTS Estudiante(Identificacion integer PRIMARY KEY,\
                        Nombre text, Apellido text,\
                        Carrera text, FechaNacimiento integer,\
                        FechaIngreso integer, Procedencia text,\
                        CorreoElectrónico text,\
                        CantidadMatrículas integer, Fotografia text)") #Se crea la tabla de estudiantes con las columnas especificas
        con.commit() # Se envía la información a la db

    def leerInfoEstudiante(self): # Se toman los datos necesarios para la creación de un nuevo estudiante
        '''Método de lectura de información general de estudiantes para su registro

        Entradas:
            carrera (string): carrera del objeto estudiante
            fechaIngreso (String - formato fecha): fecha de ingreso a la carrera
            cantidadMatriculas (int): cantidad de matrículas del estudiante
            correo (string): correo del objeto estudiante

        Returns:
            estudiante _tuple_: tupla que porta toda la informacion de entradas de estudiantes lista para registrar en la tabla estudiantes
        '''
        estudiantes.set_leerInfoPersona(self,'estudiante') # ejecutamos un set para editar las características del objeto persona
        self.__correo = input("Correo institucional: ") # Se ingresa el correo institucional
        self.__carrera = input("Carrera que estudia: ") # Se ingresa la carrera que cursa el estudiante
        while True:
            self.__fechaIngreso = input('Fecha de ingreso(dia/mes/año) de la forma **/**/**** : ').strip() # Se solicita que se ingresen los datos de la forma pedida

            if len (self.__fechaIngreso) == 10: # Se ejecuta el ingreso si los valores agregados concuerdan con el formato
                break
            else:
                print('MENSAJE: Debe ingresar la fecha de nacimiento de la forma mencionada.') # Se solicita que se ingrese los datos de la forma requerida

            print()

        while True:
            try:
                self.__cantidadMatriculas = int(input("Cantidad de matrículas: ")) # La cantidad de matrículas realizadas
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un tipo de dato valido') # Se pide que se siga el formato establecido
        info_principal = estudiantes.get_info_persona(self) # llamamos a la informacion básica de persona (características del objeto persona)
        estudiante = (info_principal[0], info_principal[1], info_principal[2], self.__carrera, info_principal[3], self.__fechaIngreso, info_principal[4], self.__correo, self.__cantidadMatriculas, info_principal[5]) # Tupla que captura la información
        return estudiante

    def crearEstudiante(self, con, miEstudiante): # creación del estudiante
        '''
        Función que permite crear un estudiante con los datos obtenidos en la función leerInfoEstudiante

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            mi_mat (tuple): tupla con la información obtenida en la función leer_info_materias

        '''

        cursorObj = con.cursor() # Se crea el cursor con el que se maneja la bd
        cursorObj.execute('''INSERT INTO Estudiante VALUES(?,?,?,?,?,?,?,?,?,?)''', miEstudiante) # Se inserta la información recibida en la tabla de estudiantes
        print("El estudiante es: ", miEstudiante)
        con.commit() # Se guardan los cambios efectuados

    def consultarInformacionEstudiantes(self, con): #consulta en la tabla estudiantes
        '''
        Función que permite consultar la información de un estudiante en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
        
        Entradas:
            codigo (int): captura del código del estudiante que desea consultarse (debe estar en la tabla estudiantes)

        Returns:
            Impresión que devuelve la información del estudiante que se buscó
        '''
        cursorObj = con.cursor()
        identificacion_estudiante = input('identificación del estudiante: ') # Se solicita al usuario que digíte la identificación del estudiante
        consulta = 'SELECT * FROM Estudiante WHERE Identificacion = "'+identificacion_estudiante+'"' # Seleccionamos todos los datos del estudiante con el id a buscar
        cursorObj.execute(consulta) #Ejecutamos la consulta en la base de datos
        filas = cursorObj.fetchall()
        for fila in filas: #Mediante un ciclo for buscamos y navegamos en las listas
            print(f'\nInformacion de estudiante:\n\
    \n    Id: {fila[0]}\n\
    Nombre: {fila[1]}\n\
    Apellido: {fila[2]}\n\
    Carrera: {fila[3]}\n\
    Fecha de nacimiento: {fila[4]}\n\
    Fecha de ingreso: {fila[5]}\n\
    Procedencia: {fila[6]}\n\
    Email: {fila[7]}\n\
    Cantidad de Matriculas: {fila[8]}\n\
    Fotografía: {fila[9]}\n') # Se presenta la información del estudiante que fue consultado mediante la búsqueda dentro de las listas

    def actualizarEstudiante(self, con, codest): #actualización de la tabla estudiante
        '''
        Función que permite actualizar el número de matrículas efectuadas por el estudiante

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            codest (int): Identificación del estudiante que se le va a actualizar las matrículas

        Entradas:
            nuevaMatrícula (int): Captura del nuevo valor de matrículas efectuadas

        Returns:
            Impresión que devuelve la actualización que se ejecutó
        '''
        cursorObj = con.cursor()
        while True:
            try:
                nuevaMatricula = int(input("Actualice el número de matrículas efectuadas: ")) # Se solicita la identificación del estudiante a actualizar
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un tipo de dato valido') # Se solicita que el dato ingresado sea válido
        actualizar = f'UPDATE Estudiante SET CantidadMatrículas= {nuevaMatricula} WHERE Identificacion="'+codest+'"'
        cursorObj.execute(actualizar) # Se actualiza la información de matrícula del estudiante específico
        print("La sentencia que se ejecuta es: ", actualizar)
        con.commit()
############################################################################################################################################
############################################################################################################################################



#################################### CLASE HISTORIA ACADEMICA CON SUS MÉTODOS ##############################################################
############################################################################################################################################
class historia_academica():
    '''
    Clase para la gestión de la historia academica de los estudiantes
    '''
    def __init__(self):
        self.__cod_materia = None
        self.__id_estudiante = None
        self.__NotaFinal = None
        self.__Creditos_Cursados = None


    def crearTablaHistoriaAcademica(self, con):
        '''
        Método que permite crear la tabla de historia académica en la base de datos

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        '''

        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS HistoriaAcademica(codigo integer,\
                            identificacion integer,\
                            NotaFinal float,\
                            CreditosCursados integer, PRIMARY KEY (codigo,identificacion))")
        con.commit() # Guardar la información en el disco (persistencia de la información)


    def leerInfoHistoriaAcademica(self,con): # captura de informacion para la historia academica
        '''
        Método que permite obtener los datos que se desean colocar en una nueva historia académica

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        Entradas:
            self.__cod_materia (int): captura de codigo de la materia (tiene que ser un valor registrado en tabla materias)
            self.__id_estudiante (int): captura de la identificacion del estudiante
            self.__NotaFinal (float): captura de la nota final de la materia

        Returns:
            HistoriaAcademica (tuple): Información de la historia académica con los datos obtenidos
        '''

        cursorObj = con.cursor()
        while True:
            try:
                self.__cod_materia = int(input("Código de la materia: "))  # captura del codigo de la materia
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')

        consulta_materia = f'SELECT codigo_materia FROM materias WHERE codigo_materia = {self.__cod_materia}' # consulta para verificación
        cursorObj.execute(consulta_materia)
        verificador_materia = cursorObj.fetchall()

        while len(verificador_materia) == 0: # lógica para el proceso de validación de los datos de la materia

            print('el codigo de la materia no existe, ingresa una id valida') # alerta de no autenticación
            while True:
                try:
                    self.__cod_materia = int(input("Código de la materia: ")) # opción para ingresar materias validad o registradas previamente
                    break
                except ValueError:
                    print('tipo de dato equivocado, coloca un numero entero')

            consulta_materia = f'SELECT codigo_materia FROM materias WHERE codigo_materia = {self.__cod_materia}' # consulta para validación
            cursorObj.execute(consulta_materia)
            verificador_materia = cursorObj.fetchall()

        while True:
            try:
                self.__id_estudiante = int(input("Identificación del estudiante: ")) # captura del codigo de la materia
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')

        consulta_estudiante = f'SELECT Identificacion FROM Estudiante WHERE Identificacion = {self.id_estudiante}' # consulta estudiante para validar informacion
        cursorObj.execute(consulta_estudiante)
        verificador_id = cursorObj.fetchall()
        
        while len(verificador_id) == 0: # verifica que la identificacion del estudiante sea valida. --- si la lista esta vacía no hay id valido 

            print('la id del estudiante no existe, ingresa una id valida') # alerta de error
            while True:
                try:
                    self.__id_estudiante = int(input("Identificación del estudiante: ")) # opción para autenticar un valor verdadero
                    break
                except ValueError:
                    print('tipo de dato equivocado, coloca un numero entero')

            consulta_estudiante = f'SELECT Identificacion FROM Estudiante WHERE Identificacion = {self.id_estudiante}' # validación de la identificacion del estudiante
            cursorObj.execute(consulta_estudiante) # ejecución de la captura de información para realizar validación de registros
            verificador_id = cursorObj.fetchall() # re asignando registro para validación
        
        while True:
            try:
                self.__NotaFinal = float(input("Nota final de la materia: ")) # captura de informacion por teclado sobre la calificación de la materia
                break
            
            except ValueError:
                print('tipo de dato equivocado, coloca un tipo de dato valido')
            
        cred_consulta_materia = f'SELECT creditos FROM materias WHERE codigo_materia = {self.__cod_materia}'
        cursorObj.execute(cred_consulta_materia)
        self.__Creditos_Cursados = int(cursorObj.fetchall()[0][0]) # captura de informacion para la asignación automática de los creditos de la materia
        HistoriaAcademica = (self.__cod_materia, self.__id_estudiante, self.__NotaFinal, self.__Creditos_Cursados) #Guardamos la información en la tupla Historia Académica
        print("La materia es:", HistoriaAcademica) #Devolvemos la información
        return HistoriaAcademica



    def CrearNuevaHistoriaAcademica(self, con, miHistoria):
        ''''
        Método que permite insertar una historia académica a la base tabla Historia Académica los datos obtenidos

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            miHistoria (tuple): Tupla con los valores obtenidos en el Método leerInfoHistoriaAcademica
        '''
        cursorObj = con.cursor()
        cursorObj.execute('''INSERT INTO HistoriaAcademica VALUES(?,?,?,?)''', miHistoria) #Ejecutamos el insert para agregar la nueva historia académica a la base de datos.
        con.commit() # Guardar la información en el disco


    def consultarInformacion(self,con):
        '''
        Método que permite consultar la historia académica de un estudiante en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
        
        Entradas:
            self.__id_estudiante (int): captura de la identificacion del estudiante

        Returns:
            Impresión que devuelve la información de las materias del estudiante solicitado
        '''
        cursorObj = con.cursor() #Creamos el cursor de la base de datos para poder controlarla
        while True:
            try:
                self.__id_estudiante = int(input("coloque el id del estudiante para consultar sus notas: "))
                break
            except ValueError:
                print('tipo de dato equivocado, coloca un numero entero')

        consulta = f'SELECT * FROM HistoriaAcademica WHERE identificacion = {self.id_estudiante}' # Seleccionamos todos los datos de la tabla (* --> Trae todos los campos)
        consulta_nombre_estudiante = f'SELECT Nombre, Apellido FROM Estudiante WHERE Identificacion = {self.id_estudiante}' #Creamos variable para obtener el nombre y apellido del estudiante
        cursorObj.execute(consulta_nombre_estudiante) #Ejecutamos la variable para obtener el nombre y apellido del estudiante en cuestión
        estudiante = cursorObj.fetchall()
        try:
            print(f'\n Historia Academica de: {estudiante[0][0]} {estudiante[0][1]}') # Imprimimos el nombre del estudiante que lo traemos de la variable estudiante que a su vez proviene de la base de datos.
        except IndexError:
            print('El estudiante no existe')
        cursorObj.execute(consulta) #Ejecutamos la variable consulta en la base de datos
        filas = cursorObj.fetchall()
        for i in filas:
            codigo = i[0] #código es la columna 1, por eso colocamos el número 0
            NotaFinal = i[2] #NotaFinal es la columna 3, por eso colocamos el número 2
            CreditosCursados = i[3] #CreditosCursados es la columna 4, por eso colocamos el número 3
            print(f'Codigo de la materia: {codigo}\nNota final: {NotaFinal}\nCreditos Cursados: {CreditosCursados}\n') #Devolvemos la información


    def BorrarMateria(self, con, materiaBorrar, idBorrar): # Borrado de información de la tabla materias
        '''
        Método que permite borrar una materia de la historia académica de un estudiante en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            materiaBorrar (int): captura del código de la materia que se desea borrar
            idBorrar (int): captura de la id del estudiante del que se desea borrar la materia

        Returns:
            Impresión que devuelve el delete que se ejecutó
        '''
        cursorObj = con.cursor()
        borrar = 'DELETE FROM HistoriaAcademica WHERE codigo = "'+materiaBorrar+'" and identificacion = "'+idBorrar+'"' # Creamos la variable borrar y borramos la materia del estudiante que queremos borrar.
        cursorObj.execute(borrar) #EJecutamos el borrado dentro de la base de datos
        print("El delete que se ejecuta es: ", borrar) #Llamamos el borrado
        con.commit() #Guardar la información en el disco --> Mantener persistencia


    def actualizarNota(self, con, materiaAct, idActualizar):
        '''
        Método que permite actualizar la nota de una materia que pertenece a un estudiante en específico

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
            materiaAct (int): captura del código de la materia que se desea actualizar su nota
            idActualizar (int): captura de la id del estudiante del que se desea actualizar la nota de la materia.

        Entradas:
            nuevaNota (int): Captura de la nueva nota de la materia

        Returns:
            Impresión que devuelve la información de la actualización que se ejecuta
        '''
        cursorObj = con.cursor() #Creamos el cursor de la base de datos para poder controlarla
        nuevaNota = input("Actualicemos la nota de la materia: ") # Solicitamos la nueva nota para actualizarla
        actualizar = 'UPDATE HistoriaAcademica SET NotaFinal = "'+nuevaNota+'" WHERE codigo = "'+materiaAct+'" and identificacion = "'+idActualizar+'"' #Traemos el código que solicitamos antes para actualizar la nota de esa materia y utilizamos el update para actualizar la nota en la base de datos
        cursorObj.execute(actualizar) #Ejecutamos la actualización en la base de datos
        print("El update que se ejecuta es: ", actualizar) #Devolvemos la información
        con.commit() #Guardar la información en el disco --> Mantener persistencia

############################################################################################################################################
############################################################################################################################################


######################################### CLASE CLASIFICACION CON SUS MÉTODOS ##############################################################
############################################################################################################################################
class clasificacion():
    '''
    Clasificacion permite crear y consultar información del promedio de todos los estudiantes
    '''

    def __init__(self):
        '''
        MODULO CONSTRUCTOR DE CLASIFICACION
        '''
        self.__data_estudiante = None
        self.__data_Cantidad_materias = None
        self.__suma_creditos = None
        self.__promedio = None


    def crear_tabla_clasificacion(self,con): # creación de la tabla clasificación
        """Método crear tabla clasificacion con sus respectivos campos

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        retorno:
            comando de ejecución para la creación de la tabla clasificacion con sus respectivos campos
        """

        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS clasificacion(identificacion text,\
                        nombre text, apellido text,\
                        cantidad_materias text, creditos_acumulados  integer,\
                        Promedio_estudiante integer, PRIMARY KEY (identificacion))") # Creación de tabla con sus respectivos items
        con.commit()

    def leer_info_clasificacion(self,con):
        """Método leer información de las demás tablas para incluir en tabla clasificacion

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        retorno:
            Informacion completa en la tabla clasificacion con Informacion preestablecida en otras tablas y con la operación Promedio 
        """
        cursorObj = con.cursor()
        cursorObj.execute('DELETE FROM clasificacion') # vaciamos tabla para actualizar toda la Informacion
        con.commit() # guardamos cambios de la tabla vacía

        consulta_estudiante = 'SELECT Identificacion, Nombre, Apellido FROM Estudiante' # consulta para captura de Informacion de los datos del estudiante
        cursorObj.execute(consulta_estudiante) # ejecución de la consulta
        self.__data_estudiante = cursorObj.fetchall() # obtenemos los datos del estudiante en una lista compuesta por tuplas con la cual vamos a realizar la clasificación

        for item in range(len(self.__data_estudiante)): # iteramos la lista para la captura de cada estudiante registrado

            consulta_cantidad_materias = f'SELECT codigo FROM HistoriaAcademica WHERE identificacion = {self.__data_estudiante[item][0]}' # consultamos la cantidad de materias desde HistoriaAcademica
            cursorObj.execute(consulta_cantidad_materias)
            self.__data_Cantidad_materias = len(cursorObj.fetchall()) #contamos las materias capturadas por cada estudiante

            consulta_cred_acumulados = f'SELECT CreditosCursados FROM HistoriaAcademica WHERE identificacion = {self.__data_estudiante[item][0]}' # consultamos la cantidad de creditos para realizar la sumatoria de ello
            cursorObj.execute(consulta_cred_acumulados)
            data_creditos = cursorObj.fetchall() # creamos variable para recorrer y contar el total de creditos
            self.__suma_creditos = 0

            for tup in data_creditos: # realizamos la sumatoria de los creditos
                for i in tup:
                    self.__suma_creditos += i

            consulta_cred_y_nota = f'SELECT CreditosCursados, NotaFinal FROM HistoriaAcademica WHERE identificacion = {self.__data_estudiante[item][0]}' # consulta creditos y notas
            cursorObj.execute(consulta_cred_y_nota) # consultamos creditos y notas desde HistoriaAcademica para realizar nuestro promedio
            data_cred_nota = cursorObj.fetchall()
            numerador = 0 # variable numerador para operar la ecuación del promedio académico
            denominador = 0 # variable denominador perteneciente a la ecuación
            try:
                for value in data_cred_nota: # operación para sacar el promedio académico, a traves de la sumatoria, multiplicación y division de item de la lista recorrida
                    numerador = value[0]*value[1] + numerador # sumatoria del (CreditoN*NotaN)+(CreditoN+1*NotaN+1)
                    denominador = value[0] + denominador # sumatoria de los creditos para dividir por el numerador
                self.__promedio = numerador/denominador # resultado de la operación

                clasificacion_item = (self.__data_estudiante[item][0],\
                                    self.__data_estudiante[item][1],\
                                    self.__data_estudiante[item][2],\
                                    self.__data_Cantidad_materias,\
                                    self.__suma_creditos,\
                                    self.__promedio) # tupla para almacenar todos los datos a plasmar en la tabla de clasificacion

                cursorObj.execute('''INSERT INTO clasificacion VALUES(?,?,?,?,?,?)''', clasificacion_item) # ingreso de datos en la tabla clasificacion
                con.commit() # Guardar la información en el disco
            except ZeroDivisionError:
                continue


    def consultar_clasificacion(self, con): # función consulta para traer todos los promedios de los estudiantes con historia Academica
        """Método presentación de la información perteneciente a la tabla de clasificacion de forma listado interactivo

        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)

        retorno:
            comando de ejecución para la creación de la tabla clasificacion con sus respectivos campos
        """
        cursorObj = con.cursor() # nueva variable cursor
        consulta = 'SELECT * FROM clasificacion' # consulta para traer todos los datos de la tabla
        cursorObj.execute(consulta) # ejecución de la consulta 
        clasificacion = cursorObj.fetchall() # almacenamiento de los datos de la tabla para muestra de la consulta
        for i in clasificacion: # iteración de los datos para mostrar datos de cualquier tamaño
            print(f'    Id: {i[0]}\n\
    Nombre: {i[1]}\n\
    Apellido: {i[2]}\n\
    Cantidad de materias: {i[3]}\n\
    Creditos acumulados: {i[4]}\n\
    Promedio académico: {i[5]:.1f}\n') # presentación de los promedios académicos de los estudiantes con historia Academica
############################################################################################################################################
############################################################################################################################################


######################################## CLASE MENU CON SUS MÉTODOS PRIVADOS Y PÚBLICOS ####################################################
############################################################################################################################################
class menu():
    '''
    Menu permite gestionar el menu principal del programa
    '''
    def __init__(self):
        '''
        MODULO CONSTRUCTOR DE MENU 
        '''
        self.moduloMaterias = materias()
        self.modulo_estudiantes = estudiantes()
        self.modulo_historia_academica = historia_academica()
        self.modulo_clasificacion = clasificacion()
        self.__salir_materias = False
        self.__salir_estudiantes = False
        self.__salir_historia_academica = False
        self.__salir_clasificacion = False
        self.__salir_principal = False
        self.__opc_materia = None
        self.__opc_estudiante = None
        self.__opc_historia_academica = None
        self.__opc_clasificacion = None
        self.opc_principal = None

    def __reset_state(self):
        '''Método que pone en estado inicial las propiedades = False 
        '''
        self.__salir_materias = False
        self.__salir_estudiantes = False
        self.__salir_historia_academica = False
        self.__salir_clasificacion = False
        
    def __error_tabla(self, num, modulo_a_usar):
        """Método encapsulado con propósito interno para presentar el error de tabla no existente 

        Args:
            num (integer): numero para identificar el mensaje ideal para usar en la presentación del error 
            modulo_a_usar (string): cadena de texto para completar el mensaje de presentación del error con el modulo en que se aplica dicho mensaje
        return:
            retorna un impresión en pantalla con el mensaje de error y con la recomendación para que no se repita el error
        """    
        if num == 1:
            print(f'No se puede realizar la operacion {modulo_a_usar}, no existen valores. Crea una materia!')
        if num == 2:
            print(f'No se puede realizar la operacion {modulo_a_usar}, no existen valores. Crea un estudiante!')
        if num == 3:
            print(f'No se puede realizar la operacion {modulo_a_usar}, no existen valores o están repetidos!')
        if num == 4:
            print(f'No se puede realizar la operacion {modulo_a_usar}, no existen valores. Crea una historia academica!')
        if num == 5:
            print(f'No se puede realizar la operacion {modulo_a_usar}, no existen valores. Crea un estudiante con su historia academica!')    

    def __error_rep_id(self, modulo):
        """Método encapsulado con propósito interno para presentación del error de repetición de identificador único en la BDD o registro con incorrecto tipo de dato

        Args:
            modulo (string): cadena de texto con el modulo en donde ocurre el error de identificador único o registro con incorrecto tipo de dato
        return:
            impresión en pantalla con el error junto con (modulo asociado al error)
        """    
        print(f'El identificador no es NUMERO ENTERO o ya existe un identificador de {modulo}')

    def menu_ejecutar(self, con): # Creamos una función menú para que el usuario navegue y sea entendible
        '''Método presentar menú interactivo para la utilización de las distintas funcionalidades de control académico
        Argumentos:
            con (clase): conexión a la base de datos (sqlite3.connection)
        retorno:
            menu interactivo para el control de flujo de los distintos módulos de las funcionalidades del programa
        '''
        while not self.__salir_principal:
            self.__reset_state()
            self.opc_principal = input('''
                                Menu Principal 
                                
                                1. Materias
                                2. Estudiantes
                                3. Historia Académica
                                4. Clasificación
                                5. Salir
    ''') #Creamos la interfaz del menú principal
            if self.opc_principal == '1': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú principal
                while not self.__salir_materias:
                    self.__opc_materia = input('''
                                        Menu Materias
                                    1. Insertar Materia leyendo info
                                    2. Insertar materia sin leer info
                                    3. Consultar materia
                                    4. Actualizar materia
                                    5. Borrar información materia
                                    6. Calcular promedio de créditos
                                    7. Salir
    ''') #Creamos la interfaz del menú materias
                    if self.__opc_materia == '1': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú materias
                        self.moduloMaterias.crear_tabla_materias(con) # crea tabla materias
                        try: # control de errores, intenta crear el registro en la tabla del modulo
                            mi_mat = self.moduloMaterias.leer_info_materias() # lee información a insertar en tabla materias
                            self.moduloMaterias.insertar_materias(con, mi_mat) #inserta información pedida como entrada en tabla materias
                        except Error: # presentación de error en caso que el intento de registro falle
                            self.__error_rep_id('materia') # control de errores de repetición de ID 
                    elif self.__opc_materia == '2':
                        try: # control de errores, intenta crear el registro en la tabla del modulo
                            self.moduloMaterias.crear_tabla_materias(con) # crea tabla materias si no existe
                            self.moduloMaterias.insertar_materias_2(con) # inserta información predeterminada a tabla materias
                        except Error: # presentación de error en caso que el intento de registro falle
                            self.__error_rep_id('materia') # control de errores de repetición de ID
                    elif self.__opc_materia == '3':
                        try: # control de errores, intenta ejecutar la consulta en la tabla del modulo
                            self.moduloMaterias.consultar_info_materias(con) # consulta informacion de tabla materias
                        except Error: # presentación de error en caso que la consulta falle
                            self.__error_tabla(1,'consulta informacion de la materia') # mensaje de error
                    elif self.__opc_materia == '4':
                        try: # control de errores, intenta ejecutar la actualización en la tabla del modulo
                            codigo_materia_act = input('Codigo de la materia a actualizar: ') # entrada de codigo de materia a actualizar
                            self.moduloMaterias.actualizar_materia(con, codigo_materia_act) # actualización de la materia
                        except Error: # presentación de error en caso que la actualización falle
                            self.__error_tabla(1,'actualizar informacion de la materia') # control de errores de no existencia de tabla
                    elif self.__opc_materia == '5':
                        try: # control de errores, intenta ejecutar el borrado en la tabla del modulo
                            self.moduloMaterias.borrar_materia(con) # borrado de materia
                        except Error: # presentación de error en caso que que la ejecución del borrado falle
                            self.__error_tabla(1,'borrar materia') # control de errores de no existencia de tabla
                    elif self.__opc_materia == '6': #Llamamos las funciones determinadas según lo solicitado por el usuario y la opción seleccionada
                        try: # control de errores, intente presentar la operación del promedio 
                            self.moduloMaterias.promedio_tabla_materias(con) # promedio de registro de historia academica
                        except Error: # presentación de error en caso que la operación del promedio falle
                            self.__error_tabla(1, 'promedio creditos de materias') # control de errores no existencia de tabla
                    elif self.__opc_materia == '7':
                        self.__salir_materias = True #Asignamos true en salir materias para romper el bucle con la opción 7 y regresar al menú principal
                    
            elif self.opc_principal == '2': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú estudiantes
                while not self.__salir_estudiantes:
                    self.__opc_estudiante = input('''
                                        Menu Estudiante
                                    1. Insertar estudiante
                                    2. Actualizar estudiante
                                    3. Consultar estudiante
                                    4. Salir
    ''') #Creamos la interfaz del menú estudiantes
                    if self.__opc_estudiante == '1': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú materias
                        self.modulo_estudiantes.crearTablaEstudiante(con)
                        try: # control de errores, intenta crear el registro en la tabla del modulo
                            miEst = self.modulo_estudiantes.leerInfoEstudiante()
                            self.modulo_estudiantes.crearEstudiante(con, miEst) 
                        except Error: # presentación de error en caso que el intento de registro falle
                            self.__error_rep_id('estudiante')
                    elif self.__opc_estudiante == '2':
                        try: # control de errores, intenta ejecutar la actualización en la tabla del modulo
                            codestact = input("Identificación del estudiante a actualizar: ")
                            self.modulo_estudiantes.actualizarEstudiante(con,codestact)
                        except Error: # presentación de error en caso que la actualización falle
                            self.__error_tabla(2, 'actualizar informacion del estudiante')
                            
                    elif self.__opc_estudiante == '3':
                        try: # control de errores, intenta ejecutar la consulta en la tabla del modulo
                            self.modulo_estudiantes.consultarInformacionEstudiantes(con) #Llamamos las funciones determinadas según lo solicitado por el usuario y la opción seleccionada
                        except Error: # presentación de error en caso que la consulta falle
                            self.__error_tabla(2,'consultar informacion del estudiante')
                    elif self.__opc_estudiante == '4':
                        self.__salir_estudiantes = True #Asignamos true en salir estudiantes para romper el bucle con la opción 4 y regresar al menú principal
                    
            elif self.opc_principal == '3': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú historia académica
                while not self.__salir_historia_academica:
                    self.__opc_historia_academica = input('''
                                        Menu Historia Academica
                                    1. Crear historia académica
                                    2. Consultar información academica 
                                    3. borrar materia del historial académico
                                    4. Actualizar nota del historial académico
                                    5. Salir
    ''') #Creamos la interfaz del menú historia académica
                    if self.__opc_historia_academica == '1': #Creamos un condicional para poder acceder a las diferentes opciones según los requerimientos del usuario en el menú historia académica
                        try: # control de errores, intenta crear la tabla de historia academica
                            self.modulo_historia_academica.crearTablaHistoriaAcademica(con)
                            MiHistoriaAcademica = self.modulo_historia_academica.leerInfoHistoriaAcademica(con)
                            self.modulo_historia_academica.CrearNuevaHistoriaAcademica(con, MiHistoriaAcademica)
                        except Error: # presentación de error en caso que que la creación falle por inexistencia de las demás tablas 
                            self.__error_tabla(3, 'creación de historia academica')
                    elif self.__opc_historia_academica == '2':
                        try: # control de errores, intenta consultar la información de la tabla del modulo
                            self.modulo_historia_academica.consultarInformacion(con)
                        except Error: # presentación de error en caso que la consulta falle
                            self.__error_tabla(4, 'consulta de informacion de historia academica')
                    elif self.__opc_historia_academica == '3':
                        try: # control de errores, intenta ejecutar el borrado en la tabla del modulo
                            idBorrar = input("Identificación del estudiante: ")
                            materiaBorrar = input("Codigo de la materia a borrar: ")
                            self.modulo_historia_academica.BorrarMateria(con, materiaBorrar, idBorrar)
                        except Error: # presentación de error en caso que la ejecución del borrado falle
                            self.__error_tabla(4, 'borrar materia de historia academica')
                    elif self.__opc_historia_academica == '4':
                        try: # control de errores, intenta ejecutar la actualización en la tabla del modulo
                            idActualizar = input("Identificación del estudiante: ")
                            materiaAct = input("Codigo de la materia a actualizar: ")
                            self.modulo_historia_academica.actualizarNota(con, materiaAct, idActualizar)  #Llamamos las funciones determinadas según lo solicitado por el usuario y la opción seleccionada y creamos la variables necesarias.
                        except Error: # presentación de error en caso que la actualización falle
                            self.__error_tabla(4, 'actualizar de historia academica')
                    elif self.__opc_historia_academica == '5':
                        self.__salir_historia_academica = True #Asignamos true en salir historia académica para romper el bucle con la opción 5 y regresar al menú principal

            elif self.opc_principal == '4': # opción menu clasificacion
                while not self.__salir_clasificacion: # declaración de condición para la ejecución del modulo
                    self.__opc_clasificacion = input('''
                                        Menu clasificación
                                    1. Consultar clasificación
                                    2. Salir
    ''') # opciones de menu clasificación 
                    if self.__opc_clasificacion == '1': # opción para la ejecución de consulta de clasificacion
                        try: # control de errores, intenta la creación de la tabla clasificacion, la lectura de informacion a los demás módulos y su consulta a si misma
                            self.modulo_clasificacion.crear_tabla_clasificacion(con) # función para la creación de la tabla clasificacion
                            self.modulo_clasificacion.leer_info_clasificacion(con) # función para la captura de informacion para insertar en la tabla clasificacion y ejecución de la consulta inserción
                            self.modulo_clasificacion.consultar_clasificacion(con) # # función para la presentación de la informacion almacenada en tabla clasificacion
                        except Error:
                            self.__error_tabla(5,'consultar clasificacion')    
                    elif self.__opc_clasificacion == '2':
                        self.__salir_clasificacion = True  #Asignamos true en salir estudiantes para romper el bucle con la opción 2 y regresar al menú principal


            elif self.opc_principal == '5':
                self.__salir_principal = True #Asignamos true en salir principal para romper el bucle con la opción 5 y cerrar el programa

        print('''Programa finalizado. Gracias por utilizar la aplicación''')
############################################################################################################################################
############################################################################################################################################


################################## FUNCIONES DE CONEXION Y DESCONEXIÓN DE LA BDD ##########################################
###########################################################################################################################
def conexion_a_la_bd():
    ''' función de creación y conexion a la base de datos
    Raises:
        Error: error de conexion a la base de datos
    Returns:
        Class: sqlite3 connection 
    '''
    try:
        con = sqlite3.connect('MI_BDD.db') 
        return con 
    except Error:
        print('Error when you try to create a Data Base')

def cerrar_BD(con): # arg = conexion
    ''' función de cierre de conexion a la base de datos

    Args:
        con (Class): sqlite3 connection
    '''
    con.close() # cierre de conexion
###########################################################################################################################


################################# FUNCIÓN RAÍZ PARA LA EJECUCIÓN DEL PROGRAMA #############################################
def main():
    ''' función raíz para la ejecución general de programa
    proceso:
        - crea la conexion
        - crea un objeto de menu
        - ejecuta el objeto menu_principal con menu_ejecutar
        - cierre de conexion a la base de datos
    '''
    mi_con = conexion_a_la_bd() # creamos la variable que crea la conexion 
    menu_principal = menu() # ejecutamos el menú principal para entrar al programa
    menu_principal.menu_ejecutar(mi_con)
    cerrar_BD(mi_con) # cerramos base de datos para finalizar conexion 

main()
