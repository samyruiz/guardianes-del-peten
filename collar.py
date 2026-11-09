"""
Módulo que define la clase Collar.
Representa el dispositivo GPS colocado a un animal para telemetría.
"""

class Collar:
    def __init__(self, codigo: str, bateria: int):
        self.codigo = codigo
        self.bateria = bateria  # Nivel de batería de 0 a 100
        self.animal_asignado = None  # Código del animal asignado o None

    def __str__(self):
        asignado_str = f"Asignado a: {self.animal_asignado}" if self.animal_asignado else "Libre"
        return f"Collar[{self.codigo}] Batería: {self.bateria}% | Estado: {asignado_str}"
