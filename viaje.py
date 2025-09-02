class Viaje:
    listado = []
    
    def __init__(self, ruta, costo, tiempo, dia_semana):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo
        self.dia_semana = dia_semana
        Viaje.listado.append(self)
    
    def mostrar_viajes(self):
        print("\n--- Todos los Viajes Registrados ---")
        for i, viaje in enumerate(Viaje.listado, 1):
            print(f"{i} - Ruta: {viaje.ruta} | "
                  f"Costo: ${viaje.costo:.2f} | "
                  f"Tiempo: {viaje.tiempo} min | "
                  f"Día: {viaje.dia_semana}")
    
    def info_viaje(self, ruta_buscar):
        print("\n*** Información del Viaje ***")
        for viaje in Viaje.listado:
            if viaje.ruta == ruta_buscar:
                print(f"Ruta: {viaje.ruta}\n"
                      f"Costo: ${viaje.costo:.2f}\n"
                      f"Tiempo: {viaje.tiempo} minutos\n"
                      f"Día: {viaje.dia_semana}")
                return
        print(f"No se encontró viaje para la ruta: {ruta_buscar}")
    
    def resumen_semanal(self):
        if not Viaje.listado:
            print("No hay viajes registrados")
            return
        
        gasto_total = sum(viaje.costo for viaje in Viaje.listado)
        tiempo_total = sum(viaje.tiempo for viaje in Viaje.listado)
        
        print("\n*** Resumen Semanal ***")
        print(f"Total de viajes: {len(Viaje.listado)}")
        print(f"Gasto total: ${gasto_total:.2f}")
        print(f"Tiempo total: {tiempo_total} minutos")
        
        # Convertir a horas y minutos
        horas = tiempo_total // 60
        minutos = tiempo_total % 60
        print(f"Tiempo total: {horas} horas y {minutos} minutos")
    
    def analizar_rutas(self):
        if not Viaje.listado:
            print("No hay viajes para analizar")
            return
        
        print("\n*** Análisis de Rutas ***")
        
        # Agrupar viajes por ruta
        rutas = {}
        for viaje in Viaje.listado:
            if viaje.ruta not in rutas:
                rutas[viaje.ruta] = {'costo_total': 0, 'tiempo_total': 0, 'veces_usada': 0}
            rutas[viaje.ruta]['costo_total'] += viaje.costo
            rutas[viaje.ruta]['tiempo_total'] += viaje.tiempo
            rutas[viaje.ruta]['veces_usada'] += 1
        
        # Encontrar rutas más costosas
        print("\n🔴 Rutas que consumen MÁS dinero:")
        rutas_costosas = sorted(rutas.items(), key=lambda x: x[1]['costo_total'], reverse=True)[:3]
        for i, (ruta, datos) in enumerate(rutas_costosas, 1):
            print(f"{i}. {ruta}: ${datos['costo_total']:.2f} ({datos['veces_usada']} viajes)")
        
        # Encontrar rutas que consumen más tiempo
        print("\n⏰ Rutas que consumen MÁS tiempo:")
        rutas_tiempo = sorted(rutas.items(), key=lambda x: x[1]['tiempo_total'], reverse=True)[:3]
        for i, (ruta, datos) in enumerate(rutas_tiempo, 1):
            horas = datos['tiempo_total'] // 60
            minutos = datos['tiempo_total'] % 60
            print(f"{i}. {ruta}: {horas}h {minutos}min ({datos['veces_usada']} viajes)")
        
        
        # Estadísticas adicionales
        print("\n📊 Estadísticas por ruta:")
        for ruta, datos in rutas.items():
            costo_promedio = datos['costo_total'] / datos['veces_usada']
            tiempo_promedio = datos['tiempo_total'] / datos['veces_usada']
            print(f"• {ruta}: ${costo_promedio:.2f} por viaje, {tiempo_promedio:.1f} min promedio")