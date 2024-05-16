class CuboRubik:
    def __init__(self):

        self.front = [[0] * 3 for _ in range(3)]
        self.back = [[1] * 3 for _ in range(3)]
        self.left = [[2] * 3 for _ in range(3)]
        self.right = [[3] * 3 for _ in range(3)]
        self.up = [[4] * 3 for _ in range(3)]
        self.down = [[5] * 3 for _ in range(3)]

    def rotarhorario(self, face):
        face[:] = [list(reversed(col)) for col in zip(*face)]

    def rotarAntihorario(self, face):
        face[:] = [list(col)[::-1] for col in zip(*face)]

    def rotar_U(self, direccion):
        self.rotarhorario(self.up)
        self.up, self.front, self.right, self.back = self.front, self.right, self.back, self.up

    def rotar_D(self, direccion):
        self.rotarAntihorario(self.down)
        self.down, self.back, self.right, self.front = self.back, self.right, self.front, self.down

    def rotar_F(self, direccion):
        self.rotarhorario(self.front)
        self.front, self.up, self.left, self.down = self.up, self.left, self.down, self.front

    def rotar_B(self, direccion):
        self.rotarAntihorario(self.back)
        self.back, self.down, self.left, self.up = self.down, self.left, self.up, self.back

    def rotar_L(self, direccion):
        self.rotarhorario(self.left)
        self.left, self.up, self.front, self.down = self.up, self.front, self.down, self.left

    def rotar_R(self, direccion):
        self.rotarAntihorario(self.right)
        self.right, self.down, self.back, self.up = self.down, self.back, self.up, self.right

    def imprimir_cubo(self):
        print("Blancoo:")
        for fila in self.front:
            print(" ".join(map(str, fila)))
        print("\namarillo:")
        for fila in self.back:
            print(" ".join(map(str, fila)))
        print("\nverde:")
        for fila in self.left:
            print(" ".join(map(str, fila)))
        print("\nazul:")
        for fila in self.right:
            print(" ".join(map(str, fila)))
        print("\nnaranja:")
        for fila in self.up:
            print(" ".join(map(str, fila)))
        print("\nRojo:")
        for fila in self.down:
            print(" ".join(map(str, fila)))


def imprimir_menu():
    print("Opciones:")
    print("1. Rotar blanco (U) sentido horario")
    print("2. Rotar blanco (U) sentido antihorario")
    print("3. Rotar amarillo (D) sentido horario")
    print("4. Rotar amarillo (D) sentido antihorario")
    print("5. Rotar rojo (F) sentido horario")
    print("6. Rotar rojo (F) sentido antihorario")
    print("7. Rotar azul (B) sentido horario")
    print("8. Rotar azul (B) sentido antihorario")
    print("9. Rotar verde (L) sentido horario")
    print("10. Rotar verde (L) sentido antihorario")
    print("11. Rotar naranja (R) sentido horario")
    print("12. Rotar naranja (R) sentido antihorario")
    print("13. Salir")


cubo_rubik = CuboRubik()

while True:
    cubo_rubik.imprimir_cubo()
    imprimir_menu()
    eleccion = input("Ingrese el número de la opción que desea ejecutar: ")
    if eleccion == '1':
        cubo_rubik.rotar_U('horario')
    elif eleccion == '2':
        cubo_rubik.rotar_U('antihorario')
    elif eleccion == '3':
        cubo_rubik.rotar_D('horario')
    elif eleccion == '4':
        cubo_rubik.rotar_D('antihorario')
    elif eleccion == '5':
        cubo_rubik.rotar_F('horario')
    elif eleccion == '6':
        cubo_rubik.rotar_F('antihorario')
    elif eleccion == '7':
        cubo_rubik.rotar_B('horario')
    elif eleccion == '8':
        cubo_rubik.rotar_B('antihorario')
    elif eleccion == '9':
        cubo_rubik.rotar_L('horario')
    elif eleccion == '10':
        cubo_rubik.rotar_L('antihorario')
    elif eleccion == '11':
        cubo_rubik.rotar_R('horario')
    elif eleccion == '12':
        cubo_rubik.rotar_R('antihorario')
    elif eleccion == '13':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor ingrese un número válido.")
