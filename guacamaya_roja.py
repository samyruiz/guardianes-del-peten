"""
Módulo guacamaya_roja.py
Clase hija GuacamayaRoja que hereda de la clase abstracta Animal.
Representa a Ara macao cyanoptera en el dosel de la Reserva de la Biosfera Maya.
"""

from animal import Animal

class GuacamayaRoja(Animal):
    def __init__(self, codigo: str, nombre: str, envergadura_alas_cm: float, arbol_anidacion: str):
        super().__init__(codigo=codigo, nombre=nombre, especie="guacamaya roja", en_peligro=True)
        self.envergadura_alas_cm = envergadura_alas_cm  # Envergadura alar en cm
        self.arbol_anidacion = arbol_anidacion          # Árbol de anidación activo

    def describir(self) -> str:
        """
        Implementación bioecológica especializada de describir() para la Guacamaya Roja:
        Dieta frugívora/granívora de semillas duras, hábitat en dosel emergente y vuelo potente.
        """
        collar = f"Collar [{self.collar_asignado}]" if self.collar_asignado else "Sin collar"
        return (
            f"[{self.codigo}] Guacamaya Roja '{self.nombre}' (Ara macao) | En Peligro | {collar}\n"
            f"   • Alimentación : Granívora/Frugívora (rompe nueces duras de cantemó, ramón y ceiba)\n"
            f"   • Hábitat      : Dosel superior maduro y cavidades de anidación (Nido: '{self.arbol_anidacion}')\n"
            f"   • Desplazamiento: Vuelo potente de largo alcance sobre el dosel (Alas: {self.envergadura_alas_cm:.1f} cm)\n"
            f"   • Bio-Rasgo    : Emparejamiento monógamo de por vida y centinela auditiva del bosque"
        )

    def registrar_vuelo_dosel(self, altitud_metros: float) -> str:
        """Monitorea la dinámica de vuelo sobre el dosel selvático de Petén."""
        estrato = "Dosel emergente superior" if altitud_metros >= 30.0 else "Vuelo medio/subdosel"
        return (f"Guacamaya {self.nombre} ({self.codigo}): vuelo registrado a {altitud_metros:.1f} m "
                f"de altura ({estrato}), monitoreando nido activo en {self.arbol_anidacion}.")
