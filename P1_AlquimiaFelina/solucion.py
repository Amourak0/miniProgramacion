

def main():
    entradas = tomar_entradas()
    print("\n\n --- Entradas ---\n", entradas)
    salida = []
    fila = entradas[2]
    consultas = entradas[3:]
    for consulta in consultas:
        if consulta[0] == '1':
            l = int(consulta[1]) - 1
            r = int(consulta[2])
            subfila = list(fila[l:r])
            res = 1
            for i in range(1, len(subfila)):
                if subfila[i] != subfila[i-1]:
                    res += 1
            salida.append(res)
        elif consulta[0] == '2':
            i = int(consulta[1]) - 1
            c = consulta[2]
            fila = fila[:i] + c + fila[i+1:]
    print("\n\n --- Salida ---\n", salida)


# Funcion que nos permite tomar las entradas de forma valida
def tomar_entradas():
    todo = input("Inserte todas las entradas separadas por espacios: ").split()
    print(todo)
    # caso default
    if todo == ["def"]:
        return [5, 3, 'RGGRP', ['1', '1', '5'], ['2', '4', 'G'], ['1', '1', '5']]
    # caso default 2
    if todo == ["def2"]:
        return [16, 9, 'BRBGORRBOBBOYBBB', ['2', '15', 'B'], ['1', '5', '15'], ['1', '14', '14'], ['2', '10', 'P'], ['2', '15', 'Y'], ['1', '10', '14'], ['2', '16', 'P'], ['1', '3', '9'], ['1', '1', '6']]
    # validacion de cantidad de entradas
    if len(todo) < 2:
        print("Entradas insuficientes.")
        tomar_entradas()
        return
    if len(todo) != 3 + int(todo[1])*3:
        print("Cantidad de entradas incorrecta.")
        tomar_entradas()
        return
    
    # validacion de formato de entradas
    t = True
    
    t = t and (todo[0].isdigit())
    t = t and (todo[1].isdigit())
    t = t and (isinstance(todo[2], str))
    t = t and (p in ['R', 'G', 'B', 'Y', 'O', 'P'] for p in todo[2])
    for i in range(int(todo[1])):
        t = t and (todo[3+3*i] in ['1', '2'])
        t = t and (todo[4+3*i].isdigit() and int(todo[4+3*i]) > 0 and int(todo[4+3*i]) <= int(todo[0]))
        if todo[3+3*i] == '1':
            t = t and (todo[5+3*i].isdigit() and int(todo[5+3*i]) > 0 and int(todo[5+3*i]) <= int(todo[0]))
        if todo[3+3*i] == '2':
            t = t and (todo[5+3*i] in ['R', 'G', 'B', 'Y', 'O', 'P'])
    if t:
        print("Entradas validas.")
    else:
        print("Entradas invalidas.")
        tomar_entradas()
        return
    return good_parse(todo)

# Funcion que parsea las entradas a un formato mas comodo
def good_parse(entrada):
    parseado = []
    parseado.append(int(entrada[0]))
    parseado.append(int(entrada[1]))
    parseado.append(entrada[2])
    for i in range(int(entrada[1])):
        consultas = []
        for j in range(3):
            consultas.append(entrada[3 + 3*i + j])
        parseado.append(consultas)
    return parseado

if __name__ == "__main__":
    main()