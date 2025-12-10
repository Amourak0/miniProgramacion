


class mesh():
    valor = 0
    hijos = []

    def __init__(self, valor, hijos):
        self.valor = valor
        self.hijos = hijos

    def printMesh(self):
        if self.hijos == [None]:
            return
        print("Valor: ", self.valor)
        hijosVal = []
        for h in self.hijos:
            if h is not None:
                hijosVal.append(h.valor)
        print("Hijos: ", hijosVal)
        for h in self.hijos:
            h.printMesh()






def main():
    entradas = tomar_entradas()
    malla = constrMesh(entradas)
    print("\n\n --- Entradas ---\n", entradas)
    print()

    potencial = 0

    malla.printMesh()



    # 2 3 4
    # 6 9 4
    
    

            
def constrMesh(univ):

    cantidad_niveles = univ[0][0]
    cantidad_espacios = univ[0][1]
    niveles = cantidad_niveles-1

    nivel = [[]]
    for i in range(cantidad_niveles):
        nivel.append([None]*cantidad_espacios)

    for i in range(cantidad_espacios):
        nivel[cantidad_niveles][i] = mesh(univ[cantidad_niveles][i], [None])
    
    while niveles > 0:
        for i in range(cantidad_espacios):
            hijos = []
            if i==0:
                hijos.append(nivel[niveles+1][i])
                hijos.append(nivel[niveles+1][i+1])
            elif i==cantidad_espacios-1:
                hijos.append(nivel[niveles+1][i-1])
                hijos.append(nivel[niveles+1][i])
            else:
                hijos.append(nivel[niveles+1][i-1])
                hijos.append(nivel[niveles+1][i])
                hijos.append(nivel[niveles+1][i+1])
            nivel[niveles][i] = mesh(univ[niveles][i], hijos)
        niveles -= 1

    hijos = []
    for i in range(cantidad_espacios):
        hijos.append(nivel[1][i])
    nivel[0] = mesh(0, hijos)

    return nivel[0]




def tomar_entradas():
    # asumimos que las entradas soin validas
    linea = input().split()
    if linea == ["def"]:
        return [[2, 3], [2, 3, 4], [6, 9, 4]]
    if linea == ["def2"]:
        return [[1, 5], [2, 3, 4, 5, 8]]
    linea = list(map(int, linea))
    todo = [linea]
    for i in range(int(linea[0])):
        linea = list(map(int, input().split()))
        todo.append(linea)
    print(todo)
    return todo




if __name__ == "__main__":
    main()

   