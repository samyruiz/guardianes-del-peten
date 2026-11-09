"""
Módulo tapir.py
Clase hija Tapir que hereda de la clase abstracta Animal.
Representa a Tapirus bairdii, el gran herbívoro y arquitecto vegetal de Petén.
"""

from animal import Animal

class Tapir(Animal):
    def __init__(self, codigo: str, nombre: str, longitud_trompa_cm: float, peso_kg: float):
        super().__init__(codigo=codigo, nombre=nombre, especie="tapir", en_peligro=True)
        self.longitud_trompa_cm = longitud_trompa_cm  # Probóscide prensil
        self.peso_kg = peso_kg                        # Masa corporal en kg

    def describir(self) -> str:
        """
        Implementación bioecológica especializada de describir() para el Tapir:
        Dieta herbívora ramoneadora, hábitat de aguadas/bosque húmedo y trocha selvática.
        """
        collar = f"Collar [{self.collar_asignado}]" if self.collar_asignado else "Sin collar"
        return (
            f"[{self.codigo}] Tapir '{self.nombre}' (Tapirus bairdii) | En Peligro | {collar}\n"
            f"   • Alimentación : Herbívoro ramoneador (hojas tiernas, brotes acuáticos y frutos caídos)\n"
            f"   • Hábitat      : Bosque húmedo tropical, aguadas y corredores ribereños\n"
            f"   • Desplazamiento: Trotador pesado abridor de trochas y bañista de lodo (Peso: {self.peso_kg:.1f} kg)\n"
            f"   • Bio-Rasgo    : Probóscide prensil de {self.longitud_trompa_cm:.1f} cm para recolección selectiva"
        )

    def registrar_dispersion_semillas(self, hectareas_recorridas: float) -> str:
        """Calcula el aporte ecológico del tapir como dispersor de semillas del bosque."""
        semillas_estimadas = int(hectareas_recorridas * 42)
        return (f"Tapir {self.nombre} ({self.codigo}): sembró aproximadamente {semillas_estimadas} "
                f"semillas nativas a lo largo de {hectareas_recorridas:.1f} ha recorridas.")
