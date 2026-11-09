"""
Módulo principal del sistema de monitoreo: SistemaMonitoreo.
Contiene la clase central que administra las listas de objetos, las guardas
de los Artículos 1 al 10 y los algoritmos de ordenamiento por selección y
búsqueda binaria (Entrega 4).
"""

import re
from animal import Animal
from collar import Collar
from zona import Zona
from guardarrecursos import Guardarrecursos
from lectura import Lectura
from alerta import Alerta
from servicio_sms import ServicioSMS

class SistemaMonitoreo:
    def __init__(self):
        # Arreglos de objetos del sistema
        self.animales = []          # Lista de objetos Animal (polimórfica)
        self.collares = []          # Lista de objetos Collar
        self.zonas = []             # Lista de objetos Zona
        self.guardarrecursos = []   # Lista de objetos Guardarrecursos
        self.lecturas = []          # Lista de objetos Lectura
        self.alertas = []           # Lista de objetos Alerta
        self._contador_alertas = 1  # Secuencial para ID de alertas
        self.guardarrecursos_turno = None # Guardarrecursos de turno activo

        # Catálogo biológico oficial de estado de conservación (Art. 2 y Art. 10)
        self.catalogo_conservacion = {
            "jaguar": True,
            "tapir": True,
            "guacamaya roja": True,
            "cocodrilo de pantano": False,
            "mono araña": True,
            "pecarí": False
        }

    # =========================================================================
    # ENTREGA 4: ALGORITMOS DE ORDENAMIENTO POR SELECCIÓN Y BÚSQUEDA BINARIA
    # Implementados desde cero sin sort(), sorted() ni bisect.
    # =========================================================================

    def ordenar_alertas(self):
        """
        Ordena la lista de alertas usando Ordenamiento por Selección (Selection Sort).
        Criterio compuesto:
          1° Nivel de prioridad: 'alta' = 1, 'media' = 2.
          2° Ante igual prioridad: hora más temprana ('HH:MM').
        En cada pasada busca el elemento menor de los que faltan y lo intercambia al frente.
        Exactamente un intercambio por pasada. Sin sort() ni sorted().
        """
        def nivel(alerta):
            if alerta.prioridad.lower() == "alta":
                return 1
            return 2

        n = len(self.alertas)
        for i in range(n):
            indice_menor = i
            for j in range(i + 1, n):
                alerta_cand = self.alertas[j]
                alerta_min = self.alertas[indice_menor]

                nivel_cand = nivel(alerta_cand)
                nivel_min = nivel(alerta_min)

                # Comparación: primero nivel numérico, desempate por hora cronológica
                if nivel_cand < nivel_min:
                    indice_menor = j
                elif nivel_cand == nivel_min:
                    if alerta_cand.hora < alerta_min.hora:
                        indice_menor = j

            # Un solo intercambio por pasada
            if indice_menor != i:
                self.alertas[i], self.alertas[indice_menor] = self.alertas[indice_menor], self.alertas[i]

        return self.alertas

    def ordenar_animales(self):
        """
        Ordena la lista de animales por su código (alfanumérico) usando Selection Sort.
        Requisito previo indispensable para la búsqueda binaria.
        Sin sort() ni sorted().
        """
        n = len(self.animales)
        for i in range(n):
            indice_menor = i
            for j in range(i + 1, n):
                if self.animales[j].codigo < self.animales[indice_menor].codigo:
                    indice_menor = j
            if indice_menor != i:
                self.animales[i], self.animales[indice_menor] = self.animales[indice_menor], self.animales[i]
        return self.animales

    def buscar_animal(self, codigo: str) -> Animal:
        """
        Busca un animal por su código utilizando Búsqueda Binaria (Binary Search).
        Divide el espacio de búsqueda a la mitad en cada iteración (inicio, fin, medio).
        Complejidad temporal: O(log n).
        Retorna el objeto Animal encontrado, o None si no existe en la lista.
        """
        if not self.animales:
            return None

        # 1. Asegurar que la colección esté ordenada por código con Selection Sort
        self.ordenar_animales()

        # 2. Algoritmo de Búsqueda Binaria
        inicio = 0
        fin = len(self.animales) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            codigo_medio = self.animales[medio].codigo

            if codigo_medio == codigo:
                return self.animales[medio]
            elif codigo < codigo_medio:
                fin = medio - 1
            else:
                inicio = medio + 1

        return None

    # =========================================================================
    # OTROS MÉTODOS DE BÚSQUEDA Y CONSULTA
    # =========================================================================
    def buscar_collar(self, codigo: str) -> Collar:
        for c in self.collares:
            if c.codigo == codigo:
                return c
        return None

    def buscar_zona(self, nombre: str) -> Zona:
        for z in self.zonas:
            if z.nombre.lower() == nombre.lower():
                return z
        return None

    def buscar_guardarrecursos(self, codigo: str) -> Guardarrecursos:
        for g in self.guardarrecursos:
            if g.codigo == codigo:
                return g
        return None

    def buscar_alerta(self, id_alerta: int) -> Alerta:
        for al in self.alertas:
            if al.id_alerta == id_alerta:
                return al
        return None

    def listar_alertas(self, titulo: str = "Lista de Alertas del Sistema"):
        """Imprime la lista actual de alertas de forma tabulada."""
        print(f"\n--- {titulo} ---")
        if not self.alertas:
            print("   (No hay alertas registradas)")
        else:
            for al in self.alertas:
                print(f"   {al}")
        print("-" * (len(titulo) + 8))

    def listar_alertas_pendientes(self):
        pendientes = [al for al in self.alertas if al.estado == "pendiente"]
        print("\n--- Alertas Pendientes de Atención ---")
        if not pendientes:
            print("   (No hay alertas pendientes)")
        else:
            for al in pendientes:
                print(f"   {al}")
        print("---------------------------------------")
        return pendientes

    # =========================================================================
    # GUARDAS Y VALIDACIONES AUXILIARES (Artículos del Reglamento)
    # =========================================================================
    def _validar_formato_codigo_animal(self, codigo: str) -> bool:
        """Guarda Art. 1: Tres letras mayúsculas, un guion y tres dígitos (JAG-001)."""
        return bool(re.match(r'^[A-Z]{3}-\d{3}$', codigo))

    def _validar_estado_conservacion(self, especie: str, en_peligro: bool) -> bool:
        """Guarda Art. 2: Coherencia con el estado biológico del programa."""
        especie_clean = especie.strip().lower()
        if especie_clean in self.catalogo_conservacion:
            return self.catalogo_conservacion[especie_clean] == en_peligro
        return True

    def _validar_codigo_guardarrecursos(self, codigo: str) -> bool:
        """Guarda Art. 7: Dos letras mayúsculas, guion y dos dígitos (GR-07) y registrado."""
        if not re.match(r'^[A-Z]{2}-\d{2}$', codigo):
            return False
        return self.buscar_guardarrecursos(codigo) is not None

    def _crear_alerta(self, tipo: str, prioridad: str, detalle: str, hora: str = "00:00") -> Alerta:
        """Crea y registra una alerta con hora y estado inicial pendiente (Art. 8)."""
        alerta = Alerta(self._contador_alertas, tipo, prioridad, detalle, hora)
        self._contador_alertas += 1
        self.alertas.append(alerta)
        return alerta

    # =========================================================================
    # CASOS DE USO (ANEXOS A - F Y CASO ESCONDIDO)
    # =========================================================================

    def registrar_animal(self, animal_o_codigo, nombre: str = None, especie: str = None, en_peligro: bool = None) -> bool:
        """Caso de uso: Registrar animal (Anexo A). Soporta polimorfismo o parámetros atómicos."""
        if isinstance(animal_o_codigo, Animal):
            animal_obj = animal_o_codigo
            codigo = animal_obj.codigo
            nombre = animal_obj.nombre
            especie = animal_obj.especie
            en_peligro = animal_obj.en_peligro
        else:
            codigo = animal_o_codigo
            animal_obj = None

        # ¿el código tiene el formato correcto? (Art. 1)
        if not self._validar_formato_codigo_animal(codigo):
            print(f"Rechazado: Código inválido '{codigo}'. Debe tener 3 letras mayúsculas, guion y 3 dígitos (ej: JAG-001). [Art. 1]")
            return False

        # ¿el código ya existe? (Art. 1)
        if self.buscar_animal(codigo) is not None:
            print(f"Rechazado: Código repetido '{codigo}'. Ya existe un animal registrado con este código. [Art. 1]")
            return False

        # Guarda Art. 2: Estado de conservación coherente
        if not self._validar_estado_conservacion(especie, en_peligro):
            estado_esperado = "en peligro" if self.catalogo_conservacion.get(especie.lower()) else "no amenazado"
            print(f"Rechazado: El estado de conservación indicado para '{especie}' no coincide con el reglamento (debe ser {estado_esperado}). [Art. 2]")
            return False

        if animal_obj is None:
            # Nota: si se pasan datos primitivos, se crea una subclase genérica o se rechaza si es abstracta
            from jaguar import Jaguar
            animal_obj = Jaguar(codigo, nombre, "patron_base", 50.0)

        self.animales.append(animal_obj)
        print(f"Animal registrado exitosamente: [{animal_obj.codigo}] {animal_obj.nombre} ({animal_obj.especie.capitalize()})")
        return True

    def asignar_collar(self, codigo_collar: str, codigo_animal: str) -> bool:
        """Caso de uso: Asignar collar (Anexo B)."""
        collar = self.buscar_collar(codigo_collar)
        animal = self.buscar_animal(codigo_animal)

        if collar is None or animal is None:
            print(f"Rechazado: No existen. Collar '{codigo_collar}': {'Existe' if collar else 'No existe'}, Animal '{codigo_animal}': {'Existe' if animal else 'No existe'}.")
            return False

        if collar.animal_asignado is not None:
            print(f"Rechazado: El collar '{codigo_collar}' ya está asignado al animal '{collar.animal_asignado}'. [Art. 4]")
            return False

        if animal.collar_asignado is not None:
            print(f"Rechazado: El animal '{codigo_animal}' ({animal.nombre}) ya lleva el collar '{animal.collar_asignado}'. [Art. 4]")
            return False

        if collar.bateria < 50:
            print(f"Rechazado: El collar '{codigo_collar}' tiene solo {collar.bateria}% de batería. Se requiere al menos 50% para asignarlo. [Art. 10]")
            return False

        collar.animal_asignado = animal.codigo
        animal.collar_asignado = collar.codigo
        print(f"Collar asignado: Collar '{codigo_collar}' vinculado exitosamente a '{animal.nombre}' ({animal.codigo}).")
        return True

    def reportar_posicion(self, codigo_collar: str, nombre_zona: str, hora: str) -> bool:
        """Caso de uso: Reportar posición (Anexo C)."""
        collar = self.buscar_collar(codigo_collar)
        if collar is None:
            print(f"Rechazada: Collar '{codigo_collar}' no existe en el registro.")
            return False

        if collar.bateria < 10:
            alerta_bateria = self._crear_alerta(
                tipo="batería baja",
                prioridad="media",
                detalle=f"Collar {collar.codigo} reportó con nivel crítico ({collar.bateria}%)",
                hora=hora
            )
            print(f"Rechazada: Lectura rechazada. Nivel de batería del collar {collar.codigo} es {collar.bateria}% (< 10%). Se generó Alerta #{alerta_bateria.id_alerta} (Media). [Art. 3]")
            return False

        zona = self.buscar_zona(nombre_zona)
        if zona is None:
            print(f"Rechazada: Lectura rechazada. La zona '{nombre_zona}' no está registrada en el sistema. [Art. 5]")
            return False

        animal = self.buscar_animal(collar.animal_asignado) if collar.animal_asignado else None
        codigo_animal = animal.codigo if animal else "SIN_ASIGNAR"
        lectura = Lectura(codigo_animal, zona.nombre, hora, "collar", collar.codigo)
        self.lecturas.append(lectura)
        print(f"Lectura registrada: {lectura}")

        if animal and animal.en_peligro and zona.tipo_zona == "uso múltiple":
            alerta_comunidad = self._crear_alerta(
                tipo="acercamiento a comunidad",
                prioridad="alta",
                detalle=f"Animal en peligro '{animal.nombre}' ({animal.codigo}, {animal.especie}) detectado en {zona.nombre} (Zona de Uso Múltiple) a las {hora}",
                hora=hora
            )
            destinatario = self.guardarrecursos_turno.codigo if self.guardarrecursos_turno else "GR-TURNO"
            ServicioSMS.enviar_mensaje(
                destinatario=f"Guardarrecursos de turno ({destinatario})",
                mensaje=f"ALERTA ALTA #{alerta_comunidad.id_alerta}: {animal.nombre} ({animal.especie}) detectado en {zona.nombre} a las {hora}."
            )

        return True

    def registrar_avistamiento(self, codigo_guardarrecursos: str, codigo_animal: str, nombre_zona: str, hora: str) -> bool:
        """Caso de uso: Registrar avistamiento (Anexo D)."""
        if not self._validar_codigo_guardarrecursos(codigo_guardarrecursos):
            print(f"Rechazado: Código de guardarrecursos '{codigo_guardarrecursos}' no es válido o no está registrado. [Art. 7]")
            return False

        animal = self.buscar_animal(codigo_animal)
        zona = self.buscar_zona(nombre_zona)
        if animal is None or zona is None:
            print(f"Rechazado: No existen. Animal '{codigo_animal}': {'Existe' if animal else 'No existe'}, Zona '{nombre_zona}': {'Existe' if zona else 'No existe'}. [Art. 5]")
            return False

        lectura = Lectura(animal.codigo, zona.nombre, hora, "avistamiento", codigo_guardarrecursos)
        self.lecturas.append(lectura)
        print(f"Avistamiento registrado exitosamente: {lectura}")
        return True

    def atender_alerta(self, id_alerta: int, codigo_guardarrecursos: str) -> bool:
        """Caso de uso: Atender alerta (Anexo E)."""
        if not self._validar_codigo_guardarrecursos(codigo_guardarrecursos):
            print(f"Rechazado: Código de guardarrecursos '{codigo_guardarrecursos}' inválido. [Art. 7]")
            return False

        alerta = self.buscar_alerta(id_alerta)
        if alerta is None:
            print(f"Rechazado: Alerta #{id_alerta} no encontrada.")
            return False

        if alerta.estado == "atendida":
            print(f"Sin cambios: La alerta #{id_alerta} ya fue atendida previamente por {alerta.atendida_por}. [Art. 8]")
            return False

        alerta.estado = "atendida"
        alerta.atendida_por = codigo_guardarrecursos
        print(f"Alerta atendida: Alerta #{id_alerta} marcada como atendida por el guardarrecursos {codigo_guardarrecursos}.")
        return True

    def consultar_movimientos(self, codigo_animal: str) -> list:
        """Caso de uso: Consultar movimientos (Anexo F)."""
        animal = self.buscar_animal(codigo_animal)
        if animal is None:
            print(f"Sin resultados: El animal con código '{codigo_animal}' no existe en el sistema.")
            return []

        movimientos = [l for l in self.lecturas if l.codigo_animal == animal.codigo]

        print(f"\n=======================================================")
        print(f" HISTORIAL DE MOVIMIENTOS: {animal.nombre} ({animal.codigo} - {animal.especie})")
        print(f"=======================================================")
        if not movimientos:
            print("   No se han registrado movimientos ni avistamientos para este animal.")
        else:
            for i, mov in enumerate(movimientos, 1):
                print(f"   {i:02d}. Zona: {mov.nombre_zona:<22} | Hora: {mov.hora:<5} | Origen: {mov.origen:<12} ({mov.identificador_origen})")
        print(f"=======================================================\n")
        return movimientos

    def cambiar_bateria(self, codigo_guardarrecursos: str, codigo_collar: str, nueva_bateria: int) -> bool:
        """Caso de uso escondido: Registrar cambio de batería (Art. 9)."""
        if not self._validar_codigo_guardarrecursos(codigo_guardarrecursos):
            print(f"Rechazado: Guardarrecursos '{codigo_guardarrecursos}' no autorizado o código inválido. [Art. 7]")
            return False

        collar = self.buscar_collar(codigo_collar)
        if collar is None:
            print(f"Rechazado: El collar '{codigo_collar}' no existe en el sistema.")
            return False

        if not (10 <= nueva_bateria <= 100):
            print(f"Rechazado: Nivel de batería {nueva_bateria}% inválido. Debe ser de al menos 10% y máximo 100% (Art. 3 y Art. 9).")
            return False

        bateria_anterior = collar.bateria
        collar.bateria = nueva_bateria
        print(f"Batería actualizada exitosamente: Collar '{codigo_collar}' renovado de {bateria_anterior}% a {nueva_bateria}% por guardarrecursos {codigo_guardarrecursos}. [Art. 9]")
        return True
