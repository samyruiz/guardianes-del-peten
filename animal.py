"""
Módulo base: animal.py
Define la clase abstracta Animal para el sistema Guardianes del Petén.
Aplica el módulo abc para impedir la instanciación directa de animales genéricos.
Nadie es "animal a secas": todo animal pertenece a una especie biológica concreta.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, codigo: str, nombre: str, especie: str, en_peligro: bool):
        # Atributos compartidos por todas las especies
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie.lower()
        self.en_peligro = en_peligro
        self.collar_asignado = None  # Código del collar GPS asignado o None

    # -------------------------------------------------------------------------
    # Métodos concretos compartidos (heredados sin cambios)
    # -------------------------------------------------------------------------
    def esta_monitoreado(self) -> bool:
        """Consulta si el espécimen porta un collar GPS activo."""
        return self.collar_asignado is not None

    def asignar_collar(self, codigo_collar: str):
        """Asocia un collar GPS al animal."""
        self.collar_asignado = codigo_collar

    def retirar_collar(self):
        """Desvincula el collar GPS del animal."""
        self.collar_asignado = None

    # -------------------------------------------------------------------------
    # Método abstracto (Polimorfismo puro)
    # Cada especie debe implementar describir() con sus datos bioecológicos:
    # qué come, dónde vive, cómo se mueve y sus rasgos del expediente.
    # -------------------------------------------------------------------------
    @abstractmethod
    def describir(self) -> str:
        """
        Método abstracto. Obliga a cada clase hija a implementar su propia
        descripción bioecológica especializada.
        """
        pass

    def __str__(self) -> str:
        return self.describir()
