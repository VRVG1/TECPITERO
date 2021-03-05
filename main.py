# DATOS DE ENTRADA
#   • El numero de cilindros va a ser del 0 al 199
#   • El usuario debera brindar el numero de peticiones (buffer de peticiones) Ej. 5. ←
#       - Puede ser que el usuario no brinde el numero de peticiones, entonces el limite sera   [DESCARTADO]
#         cuando el usuario ingrese un numero negativo o un "-1"                                [DESCARTADO]
#   • El usuario debera brindar los valores de las "n" peticiones que especifico
#       - Validar que los valores no sean menores a 0 ni mayores a 199
#   • El usuario proporcionara el cilindro inicial (validar)
#
# ================================================================================================
#              DATOS DEL LA INTERFAZ DE COMANDOS
#
#   ♦ Hacer un menu de seleccion para los diferentes algoritmos
#       • FCFS      [1]
#       • SSTF      [2]
#       • SCAN      [3]
#       • C-SCAN    [4]
#       • LOOK      [5]
#       • C-LOOK    [6]
#       • Salir     [7]
#
#   ♦ Mostrar la tabla de iteraciones mostrando los pasos realizados
#   ♦ Mostrar los resultados finales
#       • Desplazamiento
#       • Tiempo Promedio de Espera
#
# ================================================================================================

import FCFS
import SSTF
import SCAN
import Grenas
import VictorCLook


class Main:
    inicial = None
    isDone = False
    buffer_datos = []
    tableau = []

    def print_tableau(self, tableau):
        actual = tableau[0]
        solicitado = tableau[1]
        tiempo_espera = tableau[2]
        desplazamiento = tableau[3]

        length = len(actual)

        print("Cilindro Actual\t\tCilindro solicitado\t Tiempo de espera\tDesplazamiento")
        for i in range(length):
            print('     ', actual[i], '\t\t       ', solicitado[i], '\t\t       ', tiempo_espera[i],
                  '\t\t     ', desplazamiento[i])

        print('\nDesplazamiento Total: ', self.desplazamiento_total(desplazamiento), '\n')
        print('Tiempo promedio de espera: ', self.promedio_espera(tiempo_espera), '\n')
        print("\n==========================================================================================\n")


        pass

    def ingreso_num_peticiones(self):
        num_peticiones = None
        while (True):
            try:
                num_peticiones = int(input('Cuantas peticiones va a ingresar? : '))
                break
            except ValueError:
                print('\nEl valor que ingreso no es un numero, por favor, vuelva a intentarlo.\n')
                continue
            pass
        return num_peticiones
        pass

    def validacion_peticion(self, peticion):
        if (peticion >= 0 and peticion <= 199):
            return True
        return False
        pass

    def ingreso_peticion_inicial(self):
        while (True):
            try:
                entry_pet = int(input('Ingrese la peticion inicial : '))
            except ValueError:
                print('\nEl valor que ingreso no es un numero, por favor, vuelva a intentarlo.\n')
                continue

            if (self.validacion_peticion(entry_pet)):
                self.inicial = entry_pet
                break
            else:
                print('\nEl valor de la peticion ingresada no es valida, por favor, vuelva a ingresarlo.\n')
                continue
            pass  # pass de while
        pass

    def ingreso_peticiones(self):

        num_peticiones = self.ingreso_num_peticiones()

        print('\n\nLas peticiones deben tener valores entre 0 a 199\n\n')
        self.ingreso_peticion_inicial()

        while (num_peticiones != 0):
            try:
                entry_pet = int(input("Ingrese peticion : "))
            except ValueError:
                print('\nEl valor que ingreso no es un numero, por favor, vuelva a intentarlo.\n')
                continue
            if self.validacion_peticion(entry_pet):
                self.buffer_datos.append(entry_pet)
            else:
                print('\nEl valor de la peticion ingresada no es valida, por favor, vuelva a ingresarlo.\n')
                continue
            num_peticiones -= 1
            pass  # pass de while
        pass  # pass de la funcion

    def direccion_scan(self):
        menu_dir = """
DIRECCIONES DEL METODO SCAN
    [0] Abajo
    [1] Arriba

Entre [0-1] que direccion desea que tome el metodo SCAN? : """
        bit = -1
        while(True):
            try:
                bit = int(input(menu_dir))
                if bit == 0 or bit == 1:
                    break
                else:
                    print('\nLa opcion que ingreso no existe, por favor, vuelva a intentarlo.\n')
            except ValueError:
                print('\nEl valor que ingreso no es un numero, por favor, vuelva a intentarlo.\n')
        return bit
        pass

    def desplazamiento_total(self, desplazamiento):
        total = 0
        for i in desplazamiento:
            total += i
        return total
        pass

    def promedio_espera(self, espera):
        num_proc = len(self.buffer_datos)

        tpe = 0
        for i in espera:
            tpe += i
        tpe = tpe / float(num_proc)
        return tpe
        pass

    def metodos(self, opc):
        if opc == 1:    # FCFS
            print("\n==============================    FIRST COME FIRST SERVED   ==============================\n")
            self.tableau = FCFS.fcfs(self.buffer_datos, self.inicial)
        elif opc == 2:  # SSTF
            print("\n==============================   SHORTEST SEEK TIME FIRST   ==============================\n")
            self.tableau = SSTF.SSTF(self.buffer_datos, self.inicial)
        elif opc == 3:  # SCAN
            print("\n==============================             SCAN             ==============================\n")
            bit = self.direccion_scan()
            self.tableau = SCAN.scan(bit, self.buffer_datos, self.inicial)
        elif opc == 4:  # C-SCAN
            print("\n==============================            C-SCAN            ==============================\n")
            self.tableau = Grenas.CSCAN(self.buffer_datos, self.inicial, len(self.buffer_datos))
        elif opc == 5:  # LOOK
            print("\n==============================             LOOK             ==============================\n")
            self.tableau = Grenas.LOOK(self.buffer_datos, self.inicial, len(self.buffer_datos))
        elif opc == 6:  # C-LOOK
            print("\n==============================            C-LOOK            ==============================\n")
            self.tableau = VictorCLook.c_look(self.buffer_datos, self.inicial)
        elif opc == 7:  # Salir
            self.isDone = True

        if self.tableau and not self.isDone:
            self.print_tableau(self.tableau)
            self.tableau = []
        pass

    def menu(self):
        menu = """\n
============    MENÚ    ============


SELECCIONE UNA OPCION:
    [1] FCFS
    [2] SSTF
    [3] SCAN
    [4] C-SCAN
    [5] LOOK
    [6] C-LOOK
    [7] Salir
    
Del [1-7] que desea realizar? : """

        while not self.isDone:
            try:
                opc = int(input(menu))
            except ValueError:
                print('\nEl valor que ingreso no es un numero, por favor, vuelva a intentarlo.\n')
                continue
            if (opc not in range(1, 8)):
                print('\nLa opcion que ingreso no existe, por favor, vuelva a intentarlo.\n')
                continue
            self.metodos(opc)
            pass

        pass

    def init(self):
        self.ingreso_peticiones()
        self.menu()
        pass

    pass


main = Main()

main.init()
