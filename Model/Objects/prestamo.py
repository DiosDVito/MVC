class Prestamo:
    def __init__(self, prestamo_id, user_id, user_name=None, libro_titulo="",
                 fecha_inicio=None, fecha_fin=None, estado="ACTIVO"):
        self.prestamo_id = prestamo_id
        self.user_id = user_id
        self.user_name = user_name
        self.libro_titulo = libro_titulo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
