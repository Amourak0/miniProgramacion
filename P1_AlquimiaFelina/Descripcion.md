## Descripción

Chatito no es un gato ordinario. Mientras otros persiguen ratones o duermen al sol, Chatito, un felino de pelaje negro y ojos curiosos, practica el antiguo arte de la alquimia felina. En el ático polvoriento de su torre de mago, ha alineado en una fila N pociones que brillan con luz propia. Solo existen seis colores posibles para estas pociones: R, G, B, Y, O, P.

La fascinación de Chatito radica en la "resonancia cromática". Según sus observaciones, cuando varias pociones adyacentes tienen el mismo color, entran en un estado de armonía y forman un "grupo de resonancia". Un grupo puede estar formado por una o más pociones contiguas del mismo color. Contar estos grupos le permite a Chatito medir la "vibración" mágica de su mesa de experimentos.

Por ejemplo, si un estante tiene las pociones [R, R, G, A, A, A], Chatito puede ver 3 grupos de resonancia distintos:

El grupo [R, R] que ronronea con una energía cálida.

El grupo solitario [G].

El grupo [A, A, A] que zumba con una frecuencia baja y constante.

Para continuar su "investigación" (que principalmente consiste en golpear cosas con la pata y ver qué pasa), Chatito realiza dos acciones fundamentales:

Mirada Penetrante: Chatito se sienta, entrecierra sus ojos de gato y analiza fijamente un segmento de la fila de pociones para contar cuántos grupos de resonancia distintos hay.

Patita Traviesa: Con un toque delicado de su pata, Chatito derriba una gota de esencia en una de las pociones, cambiando su color a uno de los seis colores posibles.

Como su programador personal, tu tarea es crear un sistema que registre los resultados de sus travesuras para que él pueda concentrarse en lo importante: su próxima siesta.

## Entrada

La primera línea contiene dos enteros N y Q, el número de pociones y el número de acciones que Chatito realizará.

La segunda línea contiene una cadena de N caracteres, sin espacios, representando los colores iniciales de las pociones. Cada carácter será uno de R, G, B, Y, O, P.

Las siguientes Q líneas describen las acciones. Cada línea comienza con un entero tipo:

Si tipo es 1, es una Mirada Penetrante. Le seguirán dos enteros l y r, el inicio y el fin del rango de la consulta (inclusive).

Si tipo es 2, es una Patita Traviesa. Le seguirán un entero p y un carácter c, indicando que la pócima en la posición p cambia su color a c.

## Salida

Para cada acción de tipo 1, imprime en una nueva línea el número total de grupos de resonancia en el rango especificado.

## Ejemplo

# Entrada
5 3
RGGRP
1 1 5
2 4 G
1 1 5

-- 5 3 RGGRP 1 1 5 2 4 G 1 1 5

-- 16 9 BRBGORRBOBBOYBBB 2 15 B 1 5 15 1 14 14 2 10 P 2 15 Y 1 10 14 2 16 P 1 3 9 1 1 6

# Salida
4
3

# Explicacion
Inicialmente, la fila de pociones es [R, G, G, R, P].

Primera acción (1 1 5): Chatito mira toda la fila. Los grupos son [R], [G, G], [R], [P]. Hay 4 grupos de resonancia.

Segunda acción (2 4 G): Chatito cambia la 4ª pócima (R) a color G con su pata. La fila ahora es [R, G, G, G, P].

Tercera acción (1 1 5): Chatito vuelve a mirar toda la fila. Los grupos ahora son [R], [G, G, G], [P]. El segundo y tercer grupo se han fusionado. Ahora solo hay 3 grupos.

