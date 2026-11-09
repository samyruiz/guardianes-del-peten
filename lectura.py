"""
Módulo que define la clase Lectura.
Representa un registro de movimiento o avistamiento en el sistema.
"""

class Lectura:
    def __init__(self, codigo_animal: str, nombre_zona: str, hora: str, origen: str, identificador_origen: str):
        self.codigo_animal = codigo_animal
        self.nombre_zona = nombre_zona
        self.hora = hora
        self.origen = origen  # 'collar' o 'avistamiento'
        self.identificador_origen = identificador_origen  # Código de collar o guardarrecursos

    def __str__(self):
        return (f"Lectura[Animal: {self.codigo_animal} | Zona: {self.nombre_zona} | "
                f"Hora: {self.hora} | Origen: {self.origen} ({self.identificador_origen})]")
