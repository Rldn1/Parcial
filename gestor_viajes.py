class GestorViajes:
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def __init__(self):
        pass
    
    def registrar_viaje(self):
        """Registra un nuevo viaje con validaciones"""
        print("\n" + "="*40)
        print("REGISTRAR NUEVO VIAJE")
        print("="*40)
        
        # Validar ruta
        ruta = input("Ingrese la ruta del viaje: ").strip()
        while not ruta:
            print(" La ruta no puede estar vacía")
            ruta = input("Ingrese la ruta del viaje: ").strip()
        
        # Validar costo
        while True:
            try:
                costo = float(input("Ingrese el costo del viaje ($): "))
                if costo > 0:
                    break
                print(" El costo debe ser mayor a 0")
            except ValueError:
                print("❌Por favor ingrese un número válido")
        
        # Validar tiempo
        while True:
            try:
                tiempo = int(input("Ingrese el tiempo del viaje (minutos): "))
                if tiempo > 0:
                    break
                print("El tiempo debe ser mayor a 0")
            except ValueError:
                print(" Por favor ingrese un número entero válido")
        
        # Mostrar días de la semana
        print("\n Día de la semana utilizado:")
        for i, dia in enumerate(self.dias_semana, 1):
            print(f"   {i}. {dia}")
        
        # Validar día de la semana
        while True:
            try:
                opcion = int(input("Seleccione el número del día: "))
                if 1 <= opcion <= len(self.dias_semana):
                    dia_semana = self.dias_semana[opcion-1]
                    break
                print(f" Opción no válida. Ingrese entre 1 y {len(self.dias_semana)}")
            except ValueError:
                print(" Por favor ingrese un número válido")
        
        # Crear el viaje (importamos aquí para evitar circular imports)
        from viaje import Viaje
        nuevo_viaje = Viaje(ruta, costo, tiempo, dia_semana)
        print(f" Viaje con la ruta {ruta} registrado exitosamente!")
        return nuevo_viaje
    
    def ordenar_viajes(self):
        """Ordena y muestra viajes según criterio"""
        from viaje import Viaje
        
        if not Viaje.listado:
            print("❌ No hay viajes para ordenar")
            return
        
        print("\n" + "="*40)
        print("ORDENAR VIAJES")
        print("="*40)
        print("1. Por costo (menor a mayor)")
        print("2. Por costo (mayor a menor)")
        print("3. Por tiempo (menor a mayor)")
        print("4. Por tiempo (mayor a menor)")
        print("5. Por día de la semana")
        print("6. Por nombre de ruta (A-Z)")
        
        try:
            opcion = int(input("Seleccione el criterio de ordenamiento (1-6): "))
            
            if opcion == 1:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.costo)
                criterio = "costo (menor a mayor)"
            elif opcion == 2:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.costo, reverse=True)
                criterio = "costo (mayor a menor)"
            elif opcion == 3:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.tiempo)
                criterio = "tiempo (menor a mayor)"
            elif opcion == 4:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.tiempo, reverse=True)
                criterio = "tiempo (mayor a menor)"
            elif opcion == 5:
                orden_dias = {dia: i for i, dia in enumerate(self.dias_semana)}
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: orden_dias[x.dia_semana])
                criterio = "día de la semana"
            elif opcion == 6:
                viajes_ordenados = sorted(Viaje.listado, key=lambda x: x.ruta.lower())
                criterio = "nombre de ruta (A-Z)"
            else:
                print("❌ Opción no válida")
                return
            
            print(f"\n📋 VIAJES ORDENADOS POR {criterio.upper()}:")
            print("-" * 70)
            for i, viaje in enumerate(viajes_ordenados, 1):
                print(f"{i:2d}. Ruta: {viaje.ruta:15} | "
                      f"Costo: ${viaje.costo:6.2f} | "
                      f"Tiempo: {viaje.tiempo:3} min | "
                      f"Día: {viaje.dia_semana:10}")
                
        except ValueError:
            print("❌ Por favor ingrese un número válido")