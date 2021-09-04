class Contrato:
  def __init__(self, inicio, fin, nombre):
    self.inicio = inicio
    self.fin = fin
    self.nombre = nombre

  def es_compatible_con(self, aComparar):
    if self.inicio >= aComparar.inicio and self.inicio < aComparar.fin:
      return False
    elif self.inicio <= aComparar.inicio and self.fin > aComparar.inicio:
      return False
    elif self.fin > aComparar.inicio and self.fin <= aComparar.fin:
      return False
    elif aComparar.da_la_vuelta() and self.inicio < aComparar.fin:
      return False
    elif self.da_la_vuelta() and aComparar.inicio < self.fin:
      return False
    elif self.da_la_vuelta() and aComparar.da_la_vuelta():
      return False
    return True

  def modificar_fin(self, fin):
    self.fin = fin

  def da_la_vuelta(self):
    return self.inicio >= self.fin

  def devolver_inicio(self):
    return self.inicio

  def devolver_fin(self):
    return self.fin

  def devolver_nombre(self):
    return self.nombre