"""
Módulo mono_arana.py
Clase hija MonoArana que hereda de la clase abstracta Animal.
Representa al mono araña centroamericano (Ateles geoffroyi), primate del dosel maya.
"""

from animal import Animal

class MonoArana(Animal):
    def __init__(self, codigo: str, nombre: str, longitud_cola_cm: float, individuos_tropa: int):
        super().__init__(codigo=codigo, nombre=nombre, especie="mono araña", en_peligro=True)
        self.longitud_cola_cm = longitud_cola_cm    # Longitud de la cola prensil
        self.individuos_tropa = individuos_tropa    # Número de individuos en su tropa social

    def describir(self) -> str:
        """
        Implementación bioecológica especializada de describir() para el Mono Araña:
        Dieta frugívora especialista, hábitat arborícola del dosel y locomoción por braquiación.
        """
        collar = f"Collar [{self.collar_asignado}]" if self.collar_asignado else "Sin collar"
        return (
            f"[{self.codigo}] Mono Araña '{self.nombre}' (Ateles geoffroyi) | En Peligro | {collar}\n"
            f"   • Alimentación : Frugívoro especialista (frutas maduras de ramón, zapote, higos y hojas tiernas)\n"
            f"   • Hábitat      : Dosel medio y superior del bosque lluvioso primario (Tropa: {self.individuos_tropa} individuos)\n"
            f"   • Desplazamiento: Braquiación ágil y suspensión arbórea continua (sin descender al suelo)\n"
            f"   • Bio-Rasgo    : Cola prensil de {self.longitud_cola_cm:.1f} cm con yema dactilar rugosa (quinta mano)"
        )

    def registrar_braquiacion(self, arboles_recorridos: int) -> str:
        """Monitorea el desplazamiento arborícola por braquiación en el dosel superior."""
        return (f"Mono araña {self.nombre} ({self.codigo}): desplazamiento por braquiación a través de "
                f"{arboles_recorridos} árboles del dosel selvático junto a su tropa ({self.individuos_tropa} individuos).")
