import os #Este import tiene la funcion de limpiar la terminal para que se vea mas limpio todo 


cursos = []
historial_acciones = []  # Pila para el historial (LIFO)
solicitudes_revision = []  # Cola para revisiones (FIFO)

# Constante para aprobación
NOTA_APROBACION = 61.0 

# --- funciones de pilas y colas ---

def registrar_accion(accion):
    historial_acciones.append(accion)


def ver_historial():
    """historial de acciones (lifo)."""
    print("\n--- Historial de Acciones (última a primera) ---")
    if not historial_acciones:
        print("No se ha realizado acciones.")
    else:
        # Imprime desde el final para mostrar la última accion de primero
        for accion in reversed(historial_acciones):
            print(f"- {accion}")
    print("-" * 50)
    registrar_accion("Se consultó el historial de acciones.")



def agregar_solicitud_revision():
    """Agrega una solicitud a la cola de revision."""
    curso = input("Curso para el que solicita revision: ")
    motivo = input("Motivo de la solicitud: ")
    solicitud = f"Curso: {curso}, Motivo: {motivo}"
    solicitudes_revision.append(solicitud)
    registrar_accion(f"Se agregó una solicitud de revision para {curso}")
    print("Solicitud de revision agregada.")

def procesar_revision():
    """Procesa la primera solicitud en la cola (FIFO)."""
    if not solicitudes_revision:
        print("No hay solicitudes de revision pendientes.")
    else:
        solicitud_procesada = solicitudes_revision.pop(0)
        print(f"Procesando: {solicitud_procesada}")
        registrar_accion(f"Se proceso la solicitud de revision: {solicitud_procesada}")


# --- FUNCION DEL CRUD DE CURSOS Y CALCULO ---

def registrar_curso():
    """(Requisito1) Agrega un nuevo curso y su nota."""
    try:
        nombre_curso = input("Ingrese el nombre del nuevo curso: ")
        # Validar que no exista ya (esto es mas opcional,pero vi muchos videos que lo recomiendan)
        for curso in cursos:
            if curso['nombre'].lower() == nombre_curso.lower():
                print("Error: Ya existe un curso con ese nombre.")
                return
        
        nota_curso = float(input(f"Ingrese la nota para {nombre_curso}: "))
        
        cursos.append({"nombre": nombre_curso, "nota": nota_curso})
        registrar_accion(f"Se registró el curso: {nombre_curso} con nota: {nota_curso}")
        print(f"¡Curso '{nombre_curso}' agregado con exito!")
    except ValueError:
        print("Error: La nota debe ser un numero.")

def mostrar_cursos():
    """(Requisit2) Muestra todos los cursos y sus notas."""
    print("\n--- Cursos Registrados ---")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for i, curso in enumerate(cursos):
            print(f"{i + 1}. {curso['nombre']} - Nota: {curso['nota']:.2f}")
    print("-" * 30)

def calcular_promedio_general():
    """(Requisito 3) Calcula el promedio de las notas de todos los cursos."""
    if not cursos:
        print("No hay cursos para calcular el promedio.")
        return
    
    total_notas = sum(curso['nota'] for curso in cursos)
    promedio = total_notas / len(cursos)
    print(f"\nEl promedio general de los {len(cursos)} cursos es: {promedio:.2f}")
    registrar_accion(f"Se calculó el promedio general: {promedio:.2f}")


def contar_cursos_aprobados():
    """(Requisito4) Cuenta cursos aprobados y reprobados."""
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    aprobados = sum(1 for curso in cursos if curso['nota'] >= NOTA_APROBACION)
    reprobados = len(cursos) - aprobados
    
    print("\n-- Resumen de Cursos --")
    print(f"Nota de aprobación: {NOTA_APROBACION}")
    print(f"Cursos Aprobados: {aprobados}")
    print(f"Cursos Reprobados: {reprobados}")
    registrar_accion("Se contaron cursos aprobados y reprobados.")

def actualizar_nota():
    """(Requisto6) Actualiza la nota de un curso específico."""
    mostrar_cursos()
    if not cursos:
        return
    try:
        idx = int(input("Ingrese el numero del curso a actualizar: ")) - 1
        if 0 <= idx < len(cursos):
            curso = cursos[idx]
            nota_anterior = curso['nota']
            nueva_nota = float(input(f"Ingrese la nueva nota para {curso['nombre']} (anterior: {nota_anterior}): "))
            curso['nota'] = nueva_nota
            
            registrar_accion(f"Se actualizó nota de {curso['nombre']}: {nota_anterior} -> {nueva_nota}")
            print("¡Nota actualizada con éxito!")
        else:
            print("Numero de curso no valido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un numero.")

def eliminar_curso():
    """(Requisito 7) Elimina un curso existente."""
    mostrar_cursos()
    if not cursos:
        return
    try:
        idx = int(input("Ingrese el numero del curso a eliminar: ")) - 1
        if 0 <= idx < len(cursos):
            curso_eliminado = cursos.pop(idx)
            registrar_accion(f"Se eliminó el curso: {curso_eliminado['nombre']}")
            print(f"¡Curso '{curso_eliminado['nombre']}' eliminado con exito!")
        else:
            print("Número de curso no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")



# --- algoritmos de ordenamientoo ---

def ordenar_cursos_por_nota_burbuja():
    """(Requisito 8) Ordena la lista de cursos por nota (descendente) usando Burbuja."""
    if not cursos:
        print("No hay cursos para ordenar.")
        return
        
    lista = cursos 
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            #comparamos la "nota" de mayor a menor
            if lista[j]['nota'] < lista[j + 1]['nota']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    print("Cursos ordenados por nota (descendente).")
    registrar_accion("Se ordenaron cursos por nota (Burbuja).")
    mostrar_cursos()

def ordenar_cursos_por_nombre_insercion():
    """(Requisito9) Ordena la lista de cursos por nombre (alfabetico) usando Insercion."""
    if not cursos:
        print("No hay cursos para ordenar.")
        return
        
    lista = cursos 
    for i in range(1, len(lista)):
        key = lista[i] #dicci com
        j = i - 1 #com nombr alfabe
        while j >= 0 and key['nombre'].lower() < lista[j]['nombre'].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        
    print("Cursos ordenados por nombre (alfabeticamente).")
    registrar_accion("Se ordenaron cursos por nombre (Insercion).")
    mostrar_cursos()


# --- ALGORITMOS DE BUSQUEDA ---

def buscar_curso_lineal():
    """(Requisito 5) Busca un curso por nombre usando busqueda lineal."""
    if not cursos:
        print("No hay cursos registrads.")
        return
        
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").lower()
    encontrado = False
    
    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscar:
            print(f"\n--- Resultado (Búsqueda Lineal) ---")
            print(f"Encontrado: {curso['nombre']} - Nota: {curso['nota']:.2f}")
            encontrado = True
            break
            
    if not encontrado:
        print("Curso no encontrado.")
        
    registrar_accion(f"Busqueda lineal de: {nombre_buscar}")

def buscar_curso_binaria():
    """(Requisito 10) Busca un curso por nombre usando busqueda binaria."""
    if not cursos:
        print("No hay cursos registrados.")
        return

    # --- REQUISITO PREVIO PARA BÚSQUEDA BINARIA ---
    print("IMPORTANTE: La busqueda binaria requiere que la lista esté ordenada por nombre.")
    opcion = input(" Desea ordenar la lista por nombre ahora? (s/n): ").lower()
    if opcion == 's':
        ordenar_cursos_por_nombre_insercion()
    else:
        print("Advertencia: La busqueda binaria puede fallar si la lista no está ordenada.")
        #fin d r

    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").lower()
    lista_ordenada = cursos #digamos que le dimos que si 
    
    l, r = 0, len(lista_ordenada) - 1
    encontrado = False
    #www
 


    while l <= r:
        mid = (l + r) // 2
        nombre_medio = lista_ordenada[mid]['nombre'].lower()

        if nombre_medio == nombre_buscar:
            print(f"\n--- Resultado (Búsqueda Binaria) ---")
            print(f"Encontrado: {lista_ordenada[mid]['nombre']} - Nota: {lista_ordenada[mid]['nota']:.2f}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscar:
            l = mid + 1
        else: # nombre_medio > nombre_buscar
            r = mid - 1

    if not encontrado:
        print("Curso no encontrad.")
        
    registrar_accion(f"Busqueda binaria de: {nombre_buscar}")


# --- FUNCION PRINCIPAL Y MENU ---
def main():
    while True:
        print("\n==GESTOR DE NOTAS ACADEMICAS==")
        print("1. Agregar Curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (B,L")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar Curso")
        print("8. Ordenar cursos por nota (Burbuja)")
        print("9. Ordenar cursos por nombre (Inserción)")
        print("10. Buscar curso por nombre (Búsqueda Binaria)")
        print("11. Agregar Solicitud de Revisión (Cola)")
        print("12. Ver Historial de Acciones")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_curso()
        elif opcion == '2':
            mostrar_cursos()
        elif opcion == '3':
            calcular_promedio_general()
        elif opcion == '4':
            contar_cursos_aprobados()
        elif opcion == '5':
            buscar_curso_lineal()
        elif opcion == '6':
            actualizar_nota()
        elif opcion == '7':
            eliminar_curso()
        elif opcion == '8':
            ordenar_cursos_por_nota_burbuja()
        elif opcion == '9':
            ordenar_cursos_por_nombre_insercion()
        elif opcion == '10':
            buscar_curso_binaria()
        elif opcion == '11':
            agregar_solicitud_revision()
        elif opcion == '12':
            ver_historial()
        elif opcion == '13':
            print("¡Adiooooos hasta pronto!")
            break
        else:
            print("Opcion no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__": 
    main()