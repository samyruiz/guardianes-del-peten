"""
Módulo que define la clase Zona.
Representa una delimitación territorial dentro de la Reserva de la Biosfera Maya.
Tipos válidos según Art. 5: 'núcleo', 'amortiguamiento', 'uso múltiple'.
"""

class Zona:
    def __init__(self, nombre: str, tipo_zona: str):
        self.nombre = nombre
        self.tipo_zona = tipo_zona.lower()  # 'núcleo', 'amortiguamiento', 'uso múltiple'

    def __str__(self):
        return f"Zona: {self.nombre} (Tipo: {self.tipo_zona})"
