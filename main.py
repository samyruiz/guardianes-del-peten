"""
Programa Principal: main.py
Sistema de Monitoreo de Fauna - Guardianes del Petén
Entrega 4 — Ordenamiento por Selección y Búsqueda Binaria

Secuencia estricta de ejecución:
1. Prueba 1: Ordenamiento de alertas por prioridad y hora usando Selection Sort
   (imprime lista desordenada, ordena con ordenar_alertas() e imprime ordenada).
2. Prueba 2: Búsqueda binaria de animales por código (busca el primer código,
   el último y uno inexistente en la lista ordenada).
3. Prueba 3: Continuidad operativa de Entregas 1, 2 y 3 (ciclo polimórfico,
   captura de TypeError de clase abstracta, telemetría GPS, alertas SMS y guardas).
"""

from animal import Animal
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from mono_arana import MonoArana

from sistema_monitoreo import SistemaMonitoreo
from zona import Zona
from guardarrecursos import Guardarrecursos
from collar import Collar
from alerta import Alerta

def separador(titulo: str):
    print("\n" + "=" * 80)
    print(f" {titulo.upper()}")
    print("=" * 80)

def main():
    print("=" * 80)
    print("   UNIVERSIDAD DA VINCI DE GUATEMALA · FACULTAD DE INGENIERÍA")
    print("   FUNDAMENTOS DE PROGRAMACIÓN 2 | ENTREGA 4: ALGORITMOS DE BÚSQUEDA Y ORDENAMIENTO")
    print("   SISTEMA DE MONITOREO DE FAUNA: GUARDIANES DEL PETÉN")
    print("=" * 80)

    sistema = SistemaMonitoreo()

    # Carga de fauna en el sistema (5 especies del expediente)
    fauna = [
        Jaguar("JAG-001", "Balam", "rosetas cerradas dobles", 54.5),
        Tapir("TAP-001", "Tziquin", 18.5, 215.0),
        GuacamayaRoja("GUA-001", "K'inich", 98.5, "Cantemó (Metopium brownei)"),
        CocodriloDePantano("COC-001", "Sobek", 2.85, "Laguna del Tigre"),
        MonoArana("MON-001", "Ka'ax", 82.0, 14)
    ]
    for a in fauna:
        sistema.registrar_animal(a)

    # =========================================================================
    # PRUEBA 1: ORDENAMIENTO DE ALERTAS POR PRIORIDAD Y HORA (SELECTION SORT)
    # Requisito: Crear al menos 5 alertas en desorden (altas y medias, horas distintas),
    # imprimir lista, llamar ordenar_alertas() e imprimirla ordenada.
    # =========================================================================
    separador("Prueba 1: Ordenamiento por Selección de Alertas (Prioridad y Hora)")
    
    # Creamos 6 alertas intencionalmente desordenadas con distintas prioridades y horas
    alertas_prueba = [
        Alerta(1, "batería baja", "media", "Collar COL-02 reportó con batería al 7%", hora="14:30"),
        Alerta(2, "acercamiento a comunidad", "alta", "Jaguar Balam avistado en Uaxactún", hora="18:45"),
        Alerta(3, "batería baja", "media", "Collar COL-04 con carga al 5% en campo", hora="09:15"),
        Alerta(4, "acercamiento a comunidad", "alta", "Tropa de mono araña cerca de caserío", hora="06:20"),
        Alerta(5, "batería baja", "media", "Collar COL-01 con carga al 9%", hora="21:10"),
        Alerta(6, "acercamiento a comunidad", "alta", "Tapir desorientado en zona de uso múltiple", hora="11:50")
    ]
    sistema.alertas = alertas_prueba

    sistema.listar_alertas("1.1 Lista de Alertas Original (En Desorden)")

    print("\n>>> Ejecutando algoritmo de Ordenamiento por Selección: sistema.ordenar_alertas() <<<")
    sistema.ordenar_alertas()

    sistema.listar_alertas("1.2 Lista de Alertas Ordenada (1° Prioridad Alta -> 2° Hora más temprana)")

    # =========================================================================
    # PRUEBA 2: BÚSQUEDA BINARIA DE ANIMALES POR CÓDIGO
    # Requisito: Ordenar animales por código con selección y buscar 3 códigos:
    # 1. El primero de la lista ordenada
    # 2. El último de la lista ordenada
    # 3. Uno que no existe
    # =========================================================================
    separador("Prueba 2: Búsqueda Binaria de Animales por Código Alfanumérico")
    
    # Mostramos la lista ordenada de animales
    sistema.ordenar_animales()
    print("Colección de animales ordenada por código (Selection Sort):")
    for idx, an in enumerate(sistema.animales):
        print(f"   [{idx}] Código: {an.codigo:<8} | Nombre: {an.nombre:<10} | Especie: {an.especie.capitalize()}")

    cod_primero = sistema.animales[0].codigo               # "COC-001"
    cod_ultimo = sistema.animales[-1].codigo               # "TAP-001"
    cod_inexistente = "LEO-999"

    print("\n--- Ejecución de Búsqueda Binaria (O(log n)) con inicio, fin y medio ---")

    print(f"\n[Búsqueda 1] Buscando el PRIMER código de la lista ('{cod_primero}'):")
    res1 = sistema.buscar_animal(cod_primero)
    print(f"   Resultado: {res1.__class__.__name__} -> {res1}")

    print(f"\n[Búsqueda 2] Buscando el ÚLTIMO código de la lista ('{cod_ultimo}'):")
    res2 = sistema.buscar_animal(cod_ultimo)
    print(f"   Resultado: {res2.__class__.__name__} -> {res2}")

    print(f"\n[Búsqueda 3] Buscando un código INEXISTENTE ('{cod_inexistente}'):")
    res3 = sistema.buscar_animal(cod_inexistente)
    print(f"   Resultado: {res3}")

    # =========================================================================
    # PRUEBA 3: CONTINUIDAD OPERATIVA DE LAS ENTREGAS 1, 2 Y 3
    # =========================================================================
    separador("Prueba 3: Continuidad Operativa de las Entregas 1, 2 y 3")

    # 1. Ciclo polimórfico de la Entrega 3 (sin if ni isinstance)
    print("--- 3.1 Ciclo Polimórfico de la Entrega 3 (describir()): ---")
    for an in sistema.animales:
        print(an.describir())
        print("-" * 65)

    # 2. Intento de instanciar clase abstracta Animal (TypeError)
    print("\n--- 3.2 Comprobación de Clase Abstracta Animal (TypeError): ---")
    try:
        invalido = Animal("ANI-999", "Fantasma", "desconocido", False)
    except TypeError as te:
        print(f"   [CAPTURA TYPEERROR ESPERADA]: {te}")

    # 3. Flujo operativo de telemetría, collares y guardas de la Entrega 1
    print("\n--- 3.3 Telemetría, Alertas SMS y Guardas del Reglamento: ---")
    # Carga de zonas territoriales
    zonas = [
        Zona("Laguna del Tigre", "núcleo"),
        Zona("Mirador-Río Azul", "núcleo"),
        Zona("Biotopo San Miguel", "amortiguamiento"),
        Zona("Uaxactún", "uso múltiple")
    ]
    sistema.zonas.extend(zonas)

    # Guardarrecursos
    gr = Guardarrecursos("GR-07", "Don Mateo Chayax")
    sistema.guardarrecursos.append(gr)
    sistema.guardarrecursos_turno = gr

    # Collares
    col1 = Collar("COL-01", bateria=85)
    col2 = Collar("COL-02", bateria=6)   # Batería baja (< 10%)
    col3 = Collar("COL-04", bateria=35)  # Batería insuficiente para Art. 10 (< 50%)
    sistema.collares.extend([col1, col2, col3])

    # Asignación y guardas Art. 4 y 10
    sistema.asignar_collar("COL-01", "JAG-001")
    print("-> Intento Rechazado (Art. 10 - Batería < 50% al asignar):")
    sistema.asignar_collar("COL-04", "MON-001")

    # Reporte de posición en Uaxactún dispara Alerta Alta y SMS (Art. 6)
    sistema.reportar_posicion("COL-01", "Uaxactún", "18:40")

    # Avistamiento por don Mateo (Art. 5 y 7)
    sistema.registrar_avistamiento("GR-07", "COC-001", "Laguna del Tigre", "10:15")

    # Caso de uso escondido: Cambio de batería de collar COL-02 (Art. 9)
    sistema.cambiar_bateria("GR-07", "COL-02", nueva_bateria=100)

    # Consulta de movimientos (Anexo F)
    sistema.consultar_movimientos("JAG-001")

    print("\n" + "=" * 80)
    print("   EJECUCIÓN DE LA ENTREGA 4 FINALIZADA CON ÉXITO TOTAL")
    print("=" * 80)

if __name__ == "__main__":
    main()
