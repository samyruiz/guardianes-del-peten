"""
Módulo que simula el Servicio Externo de Mensajes de Texto SMS.
Representa el sistema externo contratado para notificar a guardarrecursos.
"""

class ServicioSMS:
    @staticmethod
    def enviar_mensaje(destinatario: str, mensaje: str) -> bool:
        print(f"      [SISTEMA EXTERNO SMS] Mensaje enviado a {destinatario}: \"{mensaje}\"")
        return True
