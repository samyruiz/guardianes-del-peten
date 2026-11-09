"""
Módulo jaguar.py
Clase hija Jaguar que hereda de la clase abstracta Animal.
Representa a Panthera onca en la Reserva de la Biosfera Maya.
"""

from animal import Animal

class Jaguar(Animal):
    def __init__(self, codigo: str, nombre: str, patron_rosetas: str, peso_kg: float):
        super().__init__(codigo=codigo, nombre=nombre, especie="jaguar", en_peligro=True)
        self.patron_rosetas = patron_rosetas  # Huella biométrica única en el pelaje
        self.peso_kg = peso_kg                # Masa corporal en kilogramos

    def describir(self) -> str:
        """
        Implementación bioecológica especializada de describir() para el Jaguar:
        Dieta de depredador ápice, hábitat selvático y desplazamiento sigiloso.
        """
        collar = f"Collar [{self.collar_asignado}]" if self.collar_asignado else "Sin collar"
        return (
            f"[{self.codigo}] Jaguar '{self.nombre}' (Panthera onca) | En Peligro | {collar}\n"
            f"   • Alimentación : Carnívoro ápice (caza pecaríes de collar, venados cola blanca y pacas)\n"
            f"   • Hábitat      : Bosque tropical denso y zonas núcleo (Laguna del Tigre y Mirador)\n"
            f"   • Desplazamiento: Terrestre sigiloso y excelente nadador (Peso: {self.peso_kg:.1f} kg)\n"
            f"   • Bio-Rasgo    : Identificación biométrica por rosetas '{self.patron_rosetas}'"
        )

    def calcular_radio_caza(self, presas_disponibles: int) -> str:
        """Estima el territorio de caza en km² según la abundancia local de presas."""
        radio_km2 = max(25.0, 140.0 - (presas_disponibles * 2.2))
        return (f"Jaguar {self.nombre} ({self.codigo}): patrulla un territorio de caza estimado "
                f"en {radio_km2:.1f} km² con {presas_disponibles} presas registradas.")
