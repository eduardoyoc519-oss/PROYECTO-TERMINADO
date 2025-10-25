# Gestor de Notas Académicas
El proyecto es un Gestor de Notas Académicas implementado en Python, diseñado para simular las funcionalidades básicas de un sistema de registro de cursos y notas. 
Su principal objetivo es demostrar la aplicación práctica de diversas estructuras de datos y algoritmos fundamentales en la informática.

Estructuras de Datos Utilizadas:
· Lista de Diccionarios (cursos): Se utiliza como la estructura principal para el almacenamiento del dataset (conjunto de datos).
Cada elemento de la lista es un diccionario que representa un curso con dos campos clave: el nombre (cadena) y la nota (número real).
Esta estructura facilita el acceso, la modificación y la eliminación de registros individuales (CRUD).

·  Pila (historial_acciones): Implementada para gestionar el registro de cambios. Sigue la lógica LIFO (Último en Entrar, Primero en Salir). 
Permite al usuario consultar las acciones recientes de forma cronológica inversa, lo cual es ideal para auditar o deshacer acciones teóricas.

·  Cola (solicitudes_revision): Implementada para gestionar las peticiones de revisión de notas. Sigue la lógica FIFO (Primero en Entrar, Primero en Salir). 
Esto asegura que las solicitudes se procesen en el estricto orden en que fueron recibidas.

Algoritmos Implementados:

1.Cálculo(Suma y Promedio)
Obtener el promedio general de todas las notas registradas.

2.Búsqueda Lineal 
Permite buscar un curso por nombre de manera eficiente, pero requiere que la lista esté previamente ordenada.

3.Búsqueda Binaria
Permite buscar un curso por nombre de manera eficiente, pero requiere que la lista esté previamente ordenada.

4.Ordenamiento Burbuja
Se utiliza para ordenar los cursos por la nota de forma descendente, ideal para identificar rápidamente los cursos con mejor rendimiento.

5.Ordenamiento por Inserción
Se utiliza para ordenar los cursos por el nombre de forma alfabética (ascendente), esencial para optimizar la Búsqueda Binaria.


Reflexión sobre la Implementación:
El proyecto demuestra cómo la elección de una estructura de datos adecuada tiene un impacto directo en la eficiencia de las operaciones

La Búsqueda Lineal
es simple de implementar, pero es ineficiente (lento) para listas grandes, ya que debe revisar, en el peor de los casos, todos los elementos
La Búsqueda Binaria
es mucho más eficiente , pero requiere que la lista esté ordenada por el campo de búsqueda. Esto subraya el trade-off (compensación): la preparación (ordenamiento) cuesta tiempo, pero las búsquedas repetidas se vuelven exponencialmente más rápidas.

Gestión de Procesos:
La utilización de la Pila y la Cola separa las funciones de registro de cambios (auditoría) y la gestión de tareas (revisiones). Esto es fundamental en el diseño de software real, donde la lógica de auditoría necesita ser independiente de la lógica de procesamiento de tareas. La Pila garantiza la trazabilidad temporal (LIFO), mientras que la Cola garantiza la equidad en el servicio (FIFO).

Algoritmos de Ordenamiento:
Se eligieron los algoritmos de Burbuja e Inserción por su sencillez conceptual, a pesar de que ambos tienen una complejidad de tiempo cuadrática y no son los más rápidos. Su implementación fue crucial para demostrar la lógica interna de los métodos de ordenamiento por comparación. En un entorno productivo, se usarían algoritmos más eficientes.


==REFLEXION PERSONAL DEL PROYECTO==

¿Qué aprendí con este proyecto?
Este proyecto fue como ir al gimnasio con Python; me sirvió para darle un buen entrenamiento a lo que había aprendido en teoría.

Pilas y Colas, ¡Al Fin! Entendí de una forma súper práctica para qué se usan la Pila (LIFO) y la Cola (FIFO). Pude ver cómo la Pila me ayudó a armar un historial de acciones cabal para ver lo último que hice. Y la Cola fue perfecta para manejar las solicitudes de revisión sin hacerme bolas, procesando la más antigua primero.

Ordenar y Buscar sin Morir en el Intento: Pude meterle mano a los algoritmos de Burbuja e Inserción para ordenar los cursos por nota y por nombre. Lo más chilero fue que también implementé la Búsqueda Binaria, aprendiendo que es mucho más rápida que la búsqueda lineal, ¡pero solo si la lista está bien ordenada!

Cambiar el Chip (Estructura de Datos): La gran lección fue la adaptación. Al principio el proyecto era de estudiantes, pero tuve que darle la vuelta al código completo para que manejara solo cursos con una nota. Eso me demostró que en la vida real, uno debe ajustar la estructura de datos a lo que el jefe (o el requisito) realmente pide.

¿Qué fue lo más desafiante de resolver?
Sin duda, la parte que más me puso a romperme la cabeza fue la Búsqueda Binaria y todo lo que implica.
Para que la Binaria funcione, la lista tiene que estar ordenada por nombre sí o sí. Me costó cuadrar el código para que, antes de buscar, el sistema le recordara al usuario que debía ordenar la lista, porque si no lo hacía, el resultado iba a ser un relajo.

También fue un reto migrar los algoritmos de ordenamiento (Burbuja e Inserción) de mi código original. Antes comparaba nombres de estudiantes; ahora tuve que cambiar la lógica para comparar las claves ('nota' y 'nombre') dentro de los diccionarios de la lista principal de cursos. Al final, logré hacer el chivo.

¿Qué mejoraría si tuviera más tiempo?
Si me dieran más chance para seguir trabajando en el proyecto, me enfocaría en estas cosas:

Guardar la Info de Verdad (Persistencia): Ahora, si cierro el programa, se borra todo. Lo primero que haría sería meterle mano para que guarde los cursos y el historial en un archivo, para que la información se quede guardada y no se pierda al apagar la compu.

Validación a Prueba de Errores: Pondría validaciones más estrictas.Hacer la Cola más Funcional: Me gustaría que al seleccionar "Procesar Solicitud de Revisión" (de la Cola), el sistema fuera automáticamente a la opción de "Actualizar Nota", simulando el proceso real: si revisas una nota, lo más seguro es que tengas que actualizarla.

Y FIN
