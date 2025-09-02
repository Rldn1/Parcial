class Viaje:
    listado = []  # Lista compartida de todos los viajes
    
    def __init__(self, ruta, costo, tiempo, dia_semana):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo
        self.dia_semana = dia_semana
        Viaje.listado.append(self)
    
    @classmethod
    def mostrar_viajes(cls):
        """Muestra todos los viajes registrados"""
        print("\n" + "="*60)
        print("TODOS LOS VIAJES REGISTRADOS")
        print("="*60)
        if not cls.listado:
            print("No hay viajes registrados")
            return
        
        for i, viaje in enumerate(cls.listado, 1):
            print(f"{i}. Ruta: {viaje.ruta:15} | "
                  f"Costo: ${viaje.costo:6.2f} | "
                  f"Tiempo: {viaje.tiempo:3} min | "
                  f"Día: {viaje.dia_semana:10}")
    
    @classmethod
    def info_viaje(cls, ruta_buscar):
        """Busca información de una ruta específica"""
        print(f"\n--- BUSCANDO RUTA: {ruta_buscar} ---")
        encontrado = False
        
        for viaje in cls.listado:
            if viaje.ruta.lower() == ruta_buscar.lower():
                print(f"✓ Ruta encontrada:")
                print(f"  • Ruta: {viaje.ruta}")
                print(f"  • Costo: ${viaje.costo:.2f}")
                print(f"  • Tiempo: {viaje.tiempo} minutos")
                print(f"  • Día: {viaje.dia_semana}")
                encontrado = True
                break
        
        if not encontrado:
            print(f" No se encontró viaje para la ruta: {ruta_buscar}")
    
    @classmethod
    def resumen_semanal(cls):
        """Muestra resumen semanal con análisis de rutas"""
        if not cls.listado:
            print("No hay viajes registrados")
            return
        
        gasto_total = sum(viaje.costo for viaje in cls.listado)
        tiempo_total = sum(viaje.tiempo for viaje in cls.listado)
        total_viajes = len(cls.listado)
        
        # Convertir a horas y minutos
        horas = tiempo_total // 60
        minutos = tiempo_total % 60
        
        print("\n" + "="*60)
        print("RESUMEN SEMANAL COMPLETO")
        print("="*60)
        
        # Información básica
        print(f"Total de viajes: {total_viajes}")
        print(f"Gasto total: ${gasto_total:.2f}")
        print(f"Tiempo total: {horas} horas y {minutos} minutos")
        
        # Análisis por ruta
        print("\n" + "-"*60)
        print("ANÁLISIS POR RUTAS")
        print("-"*60)
        
        # Diccionario para acumular por ruta
        rutas_analisis = {}
        
        for viaje in cls.listado:
            if viaje.ruta not in rutas_analisis:
                rutas_analisis[viaje.ruta] = {
                    'gasto_total': 0,
                    'tiempo_total': 0,
                    'viajes': 0
                }
            rutas_analisis[viaje.ruta]['gasto_total'] += viaje.costo
            rutas_analisis[viaje.ruta]['tiempo_total'] += viaje.tiempo
            rutas_analisis[viaje.ruta]['viajes'] += 1
        
        # Ordenar rutas por gasto total
        if rutas_analisis:
            rutas_por_gasto = sorted(rutas_analisis.items(), 
                                   key=lambda x: x[1]['gasto_total'], 
                                   reverse=True)
            
            rutas_por_tiempo = sorted(rutas_analisis.items(), 
                                    key=lambda x: x[1]['tiempo_total'], 
                                    reverse=True)
            
            print("\n RUTAS QUE MÁS DINERO CONSUMEN:")
            for i, (ruta, datos) in enumerate(rutas_por_gasto[:3], 1):
                print(f"   {i}. {ruta}: ${datos['gasto_total']:.2f} "
                      f"({datos['viajes']} viajes)")
            
            print("\n⏱RUTAS QUE MÁS TIEMPO CONSUMEN:")
            for i, (ruta, datos) in enumerate(rutas_por_tiempo[:3], 1):
                tiempo_horas = datos['tiempo_total'] // 60
                tiempo_minutos = datos['tiempo_total'] % 60
                print(f"   {i}. {ruta}: {tiempo_horas}h {tiempo_minutos}m "
                      f"({datos['viajes']} viajes)")
            
            # Promedios
            promedio_costo = gasto_total / total_viajes
            promedio_tiempo = tiempo_total / total_viajes
            print(f"\n Promedio por viaje: ${promedio_costo:.2f} | "
                  f"{promedio_tiempo:.1f} minutos")