"""
Módulo que define la clase Guardarrecursos.
Representa al personal de campo autorizado para patrullaje y mantenimiento.
"""

class Guardarrecursos:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo  # Formato dos letras, guion, dos dígitos (ej: GR-07)
        self.nombre = nombre

    def __str__(self):
        return f"Guardarrecursos[{self.codigo}] {self.nombre}"
