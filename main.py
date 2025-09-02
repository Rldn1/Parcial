from viaje import Viaje
from gestor_viajes import GestorViajes

# Instancias de objetos
gestor = GestorViajes()

print("=" * 60)
print("SISTEMA DE REGISTRO DE VIAJES EN TRANSPORTE PÚBLICO")
print("=" * 60)

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar un nuevo viaje")
    print("2. Mostrar todos los viajes")
    print("3. Buscar información de una ruta")
    print("4. Mostrar resumen semanal")
    print("5. Ordenar viajes")
    print("6. Analizar rutas (más tiempo/dinero)")  # NUEVA OPCIÓN
    print("7. Salir")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            gestor.registrar_viaje()
            
        elif opcion == 2:
            if Viaje.listado:
                viaje = Viaje.listado[0]
                viaje.mostrar_viajes()
            else:
                print("No hay viajes registrados")
                
        elif opcion == 3:
            if Viaje.listado:
                ruta_buscar = input("Ingrese la ruta a buscar: ").strip()
                viaje = Viaje.listado[0]
                viaje.info_viaje(ruta_buscar)
            else:
                print("No hay viajes registrados")
                
        elif opcion == 4:
            if Viaje.listado:
                viaje = Viaje.listado[0]
                viaje.resumen_semanal()
            else:
                print("No hay viajes registrados")
                
        elif opcion == 5:
            gestor.ordenar_viajes()
            
        elif opcion == 6:  # NUEVA OPCIÓN
            if Viaje.listado:
                viaje = Viaje.listado[0]
                viaje.analizar_rutas()
            else:
                print("No hay viajes registrados")
                
        elif opcion == 7:
            print("¡Gracias por usar el sistema! ¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")
            
    except ValueError:
        print("Por favor ingrese un número válido")