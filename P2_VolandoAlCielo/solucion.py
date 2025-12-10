class meshRoot():
    hijos = []

    def __init__(self, hijos):
        self.hijos = hijos
    
    def printMesh(self):
        hijosVal = []
        for h in self.hijos:
            hijosVal.append(h.valor)
        print("Hijos: ", hijosVal)
        for h in self.hijos:
            h.printMesh()
    
    def setValor(self, nuevoValor, posicion):
        posx = posicion[0]
        posy = posicion[1]
        raiz = self.hijos[posx]
        for _ in range(posy):
            if posx != 0:
                raiz = raiz.hijos[1]
            else:
                raiz = raiz.hijos[0]
        raiz.valor = nuevoValor

    def getMinVal(self, posicion = -1):
        if posicion == -1:
            return min(h.getMinVal() for h in self.hijos)
        posx = posicion[0]
        posy = posicion[1]
        raiz = self.hijos[posx]
        for _ in range(posy):
            if posx != 0:
                raiz = raiz.hijos[1]
            else:
                raiz = raiz.hijos[0]
        if raiz.hijos == [None]:
            return raiz.valor
        return min(h.getMinVal() for h in raiz.hijos) + raiz.valor


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
    
    def getMinVal(self):
        if self.hijos == [None]:
            return self.valor
        return min(h.getMinVal() for h in self.hijos) + self.valor
        






def main():
    entradas = tomar_entradas()
    malla = constrMesh(entradas)

    valor = malla.getMinVal()

    print(valor, end="")
    

            
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
    nivel[0] = meshRoot(hijos)

    return nivel[0]




def tomar_entradas():
    linea = input().split()
    if linea == ["def"]:
        return [[2, 3], [2, 3, 4], [6, 9, 4]]
    if linea == ["def2"]:
        return [[1, 5], [2, 3, 4, 5, 8]]
    if linea == ["def3"]:
        return [[3, 3], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    linea = list(map(int, linea))
    todo = [linea]
    for i in range(int(linea[0])):
        linea = list(map(int, input().split()))
        todo.append(linea)
    return todo




if __name__ == "__main__":
    main()

   