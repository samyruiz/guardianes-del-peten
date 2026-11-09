"""
Módulo cocodrilo_de_pantano.py
Clase hija CocodriloDePantano que hereda de la clase abstracta Animal.
Representa a Crocodylus moreletii en los humedales lénticos de Petén.
"""

from animal import Animal

class CocodriloDePantano(Animal):
    def __init__(self, codigo: str, nombre: str, longitud_metros: float, humedal_origen: str):
        # En el reglamento (Art. 2), el cocodrilo de pantano NO está en peligro
        super().__init__(codigo=codigo, nombre=nombre, especie="cocodrilo de pantano", en_peligro=False)
        self.longitud_metros = longitud_metros    # Talla total del reptil
        self.humedal_origen = humedal_origen      # Humedal o laguna de residencia

    def describir(self) -> str:
        """
        Implementación bioecológica especializada de describir() para el Cocodrilo de Pantano:
        Dieta carnívora oportunista/piscívora, hábitat dulceacuícola y locomoción por nado ondulatorio.
        """
        collar = f"Collar [{self.collar_asignado}]" if self.collar_asignado else "Sin collar"
        return (
            f"[{self.codigo}] Cocodrilo de Pantano '{self.nombre}' (Crocodylus moreletii) | No Amenazado | {collar}\n"
            f"   • Alimentación : Carnívoro oportunista (peces de río, crustáceos, anfibios y pequeñas aves)\n"
            f"   • Hábitat      : Lagunetas lénticas, aguadas y humedales de agua dulce ('{self.humedal_origen}')\n"
            f"   • Desplazamiento: Nado ondulatorio subacuático con cola comprimida y reptación (Talla: {self.longitud_metros:.2f} m)\n"
            f"   • Bio-Rasgo    : Válvula palatina para caza subacuática y termorregulación en orillas soleadas"
        )

    def registrar_inmersion(self, profundidad_metros: float, tiempo_minutos: int) -> str:
        """Monitorea el ciclo de inmersión y termorregulación acuática en humedales."""
        return (f"Cocodrilo {self.nombre} ({self.codigo}): completó inmersión de {tiempo_minutos} minutos "
                f"a {profundidad_metros:.1f} m de profundidad en {self.humedal_origen}.")
