## Link
https://omegaup.com/arena/problem/Volando-al-cielo/

## Descripcion

Daedalus es un famoso constructor, su más reciente construcción es el robot Icarus el cual ha sido diseñado para llegar a los cielos con sus alas de cera. Sin embargo, el sol es muy fuerte y hay peligro de que el calor de este derrita las alas de Icarus haciéndolo caer al suelo, por lo que el tiene que llegar al cielo cuidando con haber sufrido la menor cantidad de daño por el calor.
Para llegar al cielo hay N niveles, de los cuales cada uno tiene M espacios por los cuales se pueden pasar, cada uno tiene su cantidad de calor Cnm, Icarus decide en que espacio de la fila numero N, Icarus decide en que espacio de la fila numero comenzar su vuelo, si Icarus se encuentra en la posición (x,y) puede decidir volar a (x+1, y+1), (x, y+1) o (x-1, y+1) siempre y cuando existan las posiciones. 
Una vez realizado el vuelo hasta el cielo el daño total de calor que sufrió es la suma de todos los Cxy los cuales paso en su recorrido, el inicio también se cuenta.
Ayuda a Icarus a saber cual es la menor cantidad de daño con la que puede llegar al cielo. 

## Entrada

Dos números positivos N y M donde N representa el número de filas y M representa la cantidad de valores por fila. Luego se presentaran N filas con M números donde cada número indica la cantidad de calor que hay en cada posición.

## Salida

Un entero que representa la mínima cantidad de calor con la que se puede llegar.

## Ejemplo

# Entrada

2 3
2 3 4
6 9 4

# Salida

7

# Explicacion

comienza en (x=1,y=0)=3 y sigue por (x=2, y=1)=4