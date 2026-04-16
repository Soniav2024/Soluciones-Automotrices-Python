# ====================================================================
# PROGRAMA: Sistema de Gestión de Reparaciones
# EMPRESA: Soluciones Automotrices
# LENGUAJE: Python 3
# DESCRIPCIÓN: Permite registrar, gestionar y dar seguimiento a las
#              reparaciones de vehículos en el taller mecánico.
#              Implementa operaciones CRUD básicas (Crear, Leer,
#              Actualizar, Eliminar) sobre un registro de reparaciones.
# AUTOR: Sonia Valenzuela
# FECHA: Abril 2026
# ====================================================================

import os

# ==================== CONSTANTES ====================
MAX_REPARACIONES = 50

# ==================== ESTRUCTURA DE DATOS ====================
reparaciones = []
contador_id = 1

# ==================== FUNCIONES DEL SISTEMA ====================

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "=" * 40)
    print("   TALLER SOLUCIONES AUTOMOTRICES")
    print("   Sistema de Gestion de Reparaciones")
    print("=" * 40)
    print("1. Registrar reparacion")
    print("2. Listar reparaciones")
    print("3. Buscar reparacion")
    print("4. Actualizar estado")
    print("5. Eliminar reparacion")
    print("6. Estadisticas")
    print("7. Salir")
    print("=" * 40)

def nombre_estado(estado):
    """Convierte el número de estado a su nombre correspondiente"""
    if estado == 0:
        return "PENDIENTE"
    elif estado == 1:
        return "EN PROCESO"
    elif estado == 2:
        return "TERMINADO"
    else:
        return "DESCONOCIDO"

# ==================== 1. REGISTRAR (CREAR) ====================
def registrar():
    """Registra una nueva reparación en el sistema"""
    global contador_id
    
    if len(reparaciones) >= MAX_REPARACIONES:
        print("\n[ERROR] Capacidad maxima alcanzada.")
        return
    
    print("\n--- NUEVA REPARACION ---")
    
    cliente = input("Nombre del cliente: ")
    vehiculo = input("Vehiculo (marca/modelo/placa): ")
    problema = input("Descripcion del problema: ")
    
    while True:
        try:
            costo = float(input("Costo estimado: $"))
            break
        except ValueError:
            print("[ERROR] Ingrese un valor numerico valido.")
    
    nueva = {
        'id': contador_id,
        'cliente': cliente,
        'vehiculo': vehiculo,
        'problema': problema,
        'estado': 0,
        'costo': costo
    }
    
    reparaciones.append(nueva)
    contador_id += 1
    
    print(f"\n[OK] Reparacion registrada con ID: {nueva['id']}")

# ==================== 2. LISTAR (LEER) ====================
def listar():
    """Muestra todas las reparaciones registradas"""
    if len(reparaciones) == 0:
        print("\n[INFO] No hay reparaciones registradas.")
        return
    
    print("\n=== LISTADO DE REPARACIONES ===")
    print(f"Total de registros: {len(reparaciones)}\n")
    
    for r in reparaciones:
        print("┌" + "─" * 39 + "┐")
        print(f"│ ID: {r['id']:<33} │")
        print(f"│ Cliente: {r['cliente'][:29]:<29} │")
        print(f"│ Vehiculo: {r['vehiculo'][:28]:<28} │")
        print(f"│ Problema: {r['problema'][:28]:<28} │")
        print(f"│ Estado: {nombre_estado(r['estado']):<30} │")
        print(f"│ Costo: ${r['costo']:<30.2f} │")
        print("└" + "─" * 39 + "┘")

# ==================== 3. BUSCAR ====================
def buscar():
    """Busca una reparación por su ID (búsqueda lineal O(n))"""
    try:
        id_buscado = int(input("\nID a buscar: "))
    except ValueError:
        print("\n[ERROR] Ingrese un numero valido.")
        return
    
    for r in reparaciones:
        if r['id'] == id_buscado:
            print("\n[ENCONTRADO] Reparacion localizada:")
            print(f"  ID: {r['id']}")
            print(f"  Cliente: {r['cliente']}")
            print(f"  Vehiculo: {r['vehiculo']}")
            print(f"  Problema: {r['problema']}")
            print(f"  Estado: {nombre_estado(r['estado'])}")
            print(f"  Costo: ${r['costo']:.2f}")
            return
    
    print(f"\n[ERROR] No se encontro ID: {id_buscado}")

# ==================== 4. ACTUALIZAR ESTADO ====================
def actualizar():
    """Actualiza el estado de una reparación"""
    try:
        id_buscado = int(input("\nID a actualizar: "))
    except ValueError:
        print("\n[ERROR] Ingrese un numero valido.")
        return
    
    for r in reparaciones:
        if r['id'] == id_buscado:
            print(f"\n[INFO] Estado actual: {nombre_estado(r['estado'])}")
            print("\nSeleccione nuevo estado:")
            print("  0 - PENDIENTE")
            print("  1 - EN PROCESO")
            print("  2 - TERMINADO")
            
            try:
                nuevo_estado = int(input("Opcion: "))
                if nuevo_estado in [0, 1, 2]:
                    r['estado'] = nuevo_estado
                    print(f"\n[OK] Estado actualizado a: {nombre_estado(r['estado'])}")
                else:
                    print("\n[ERROR] Opcion no valida.")
            except ValueError:
                print("\n[ERROR] Ingrese un numero valido.")
            return
    
    print(f"\n[ERROR] No se encontro ID: {id_buscado}")

# ==================== 5. ELIMINAR ====================
def eliminar():
    """Elimina una reparación del sistema"""
    try:
        id_buscado = int(input("\nID a eliminar: "))
    except ValueError:
        print("\n[ERROR] Ingrese un numero valido.")
        return
    
    for i, r in enumerate(reparaciones):
        if r['id'] == id_buscado:
            print(f"\n[ADVERTENCIA] Cliente: {r['cliente']} - Vehiculo: {r['vehiculo']}")
            confirmar = input("¿Eliminar? (s/n): ")
            
            if confirmar.lower() == 's':
                reparaciones.pop(i)
                print("\n[OK] Reparacion eliminada.")
            else:
                print("\n[INFO] Cancelado.")
            return
    
    print(f"\n[ERROR] No se encontro ID: {id_buscado}")

# ==================== 6. ESTADISTICAS ====================
def estadisticas():
    """Muestra estadísticas del taller"""
    if len(reparaciones) == 0:
        print("\n[INFO] No hay datos registrados.")
        return
    
    pendientes = 0
    en_proceso = 0
    terminados = 0
    suma_costos = 0
    
    for r in reparaciones:
        if r['estado'] == 0:
            pendientes += 1
        elif r['estado'] == 1:
            en_proceso += 1
        else:
            terminados += 1
        suma_costos += r['costo']
    
    costo_promedio = suma_costos / len(reparaciones)
    
    print("\n╔" + "═" * 38 + "╗")
    print("║{:^38}║".format("ESTADISTICAS"))
    print("╠" + "═" * 38 + "╣")
    print(f"║ Total reparaciones: {len(reparaciones):<20} ║")
    print(f"║ Pendientes: {pendientes:<26} ║")
    print(f"║ En proceso: {en_proceso:<26} ║")
    print(f"║ Terminados: {terminados:<26} ║")
    print(f"║ Costo total: ${suma_costos:<23.2f} ║")
    print(f"║ Costo promedio: ${costo_promedio:<21.2f} ║")
    print("╚" + "═" * 38 + "╝")

# ==================== FUNCIÓN PRINCIPAL ====================
def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("\n[ERROR] Opcion no valida.")
            pausar()
            continue
        
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            buscar()
        elif opcion == 4:
            actualizar()
        elif opcion == 5:
            eliminar()
        elif opcion == 6:
            estadisticas()
        elif opcion == 7:
            print("\n[INFO] Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\n[ERROR] Opcion no valida.")
        
        if opcion != 7:
            pausar()
            limpiar_pantalla()

# ==================== PUNTO DE ENTRADA ====================
if __name__ == "__main__":
    main()