"""
Módulo que define la clase Alerta.
Representa un aviso generado ante condiciones críticas que requieren atención.
Incorpora el atributo hora para soportar el ordenamiento temporal y prioritario (Entrega 4).
"""

class Alerta:
    def __init__(self, id_alerta: int, tipo: str, prioridad: str, detalle: str, hora: str = "00:00"):
        self.id_alerta = id_alerta
        self.tipo = tipo            # 'batería baja', 'acercamiento a comunidad', etc.
        self.prioridad = prioridad.lower()  # 'alta', 'media', 'baja'
        self.detalle = detalle
        self.hora = hora            # Formato "HH:MM" (ej. "18:30", "09:15")
        self.estado = "pendiente"   # Toda alerta nace pendiente (Art. 8)
        self.atendida_por = None    # Código de guardarrecursos

    def __str__(self):
        estado_str = f"Atendida por {self.atendida_por}" if self.estado == "atendida" else "Pendiente"
        return (f"Alerta #{self.id_alerta:02d} [{self.prioridad.upper():<5}] Hora: {self.hora} | "
                f"{self.tipo}: {self.detalle} | Estado: {estado_str}")
