from viaje import Viaje  # Importamos la clase Viaje

class GestorViajes:
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def __init__(self):
        pass
    
    def registrar_viaje(self):
        print("\n--- Registrar Nuevo Viaje ---")
        
        # Validar ruta
        ruta = input("Ingrese la ruta del viaje: ").strip()
        while not ruta:
            print("La ruta no puede estar vacía")
            ruta = input("Ingrese la ruta del viaje: ").strip()
        
        # Validar costo
        while True:
            try:
                costo = float(input("Ingrese el costo del viaje ($): "))
                if costo > 0:
                    break
                print("El costo debe ser mayor a 0")
            except ValueError:
                print("Por favor ingrese un número válido")
        
        # Validar tiempo
        while True:
            try:
                tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))
                if tiempo > 0:
                    break
                print("El tiempo debe ser mayor a 0")
            except ValueError:
                print("Por favor ingrese un número entero válido")
        
        # Validar día de la semana
        print("\nDía en que se realizó el viaje (ingrese el número):")
        for i, dia in enumerate(self.dias_semana, 1):
            print(f"{i}. {dia}")
        
        while True:
            try:
                opcion = int(input("Seleccione el número del día: "))
                if 1 <= opcion <= len(self.dias_semana):
                    dia_semana = self.dias_semana[opcion-1]
                    break
                print("Opción no válida")
            except ValueError:
                print("Por favor ingrese un número válido")
        
        # Crear el viaje
        viaje = Viaje(ruta, costo, tiempo, dia_semana)
        print("✓ Viaje registrado exitosamente!")
        return viaje
    
    def ordenar_viajes(self):
        if not Viaje.listado:  # Ahora Viaje está definido
            print("No hay viajes para ordenar")
            return
        
        print("\n--- Ordenar Viajes ---")
        print("1. Por costo (menor a mayor)")
        print("2. Por costo (mayor a menor)")
        print("3. Por tiempo (menor a mayor)")
        print("4. Por tiempo (mayor a menor)")
        print("5. Por día de la semana")
        
        try:
            opcion = int(input("Seleccione el criterio: "))
            
            if opcion == 1:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.costo)
            elif opcion == 2:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.costo, reverse=True)
            elif opcion == 3:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.tiempo)
            elif opcion == 4:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.tiempo, reverse=True)
            elif opcion == 5:
                orden_dias = {dia: i for i, dia in enumerate(self.dias_semana)}
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: orden_dias[x.dia_semana])
            else:
                print("Opción no válida")
                return
            
            print("\n--- Viajes Ordenados ---")
            for i, viaje in enumerate(viajes_ordenados, 1):
                print(f"{i} - Ruta: {viaje.ruta} | "
                      f"Costo: ${viaje.costo:.2f} | "
                      f"Tiempo: {viaje.tiempo} min | "
                      f"Día: {viaje.dia_semana}")
                
        except ValueError:
            print("Por favor ingrese un número válido")