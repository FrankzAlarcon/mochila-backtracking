class Elemento:
  def __init__(self, peso, beneficio):
      self.peso = peso
      self.beneficio = beneficio
  
  def __eq__(self, otro_elemento):
      return self.peso == otro_elemento.peso and self.beneficio == otro_elemento.beneficio

class Mochila:
  def __init__(self, pesoMaximo, numElementos=0):
      self.pesoMaximo = pesoMaximo
      self.elementos = []
      self.beneficio = 0
      self.peso = 0

  def anadirElemento(self, elemento: Elemento):
    for i in range(len(self.elementos)):
      if self.elementos[i] == None:
        self.elementos[i] = elemento
        self.beneficio += elemento.beneficio
        self.peso += elemento.peso
        break

  def reset(self):
    self.peso = 0
    self.beneficio = 0
    self.elementos = []

  def eliminarElemento(self, elemento: Elemento):
    for i in range(len(self.elementos)):
      if self.elementos[i] == elemento:
        self.elementos.pop(i)
        self.peso -= elemento.peso
        self.beneficio -= elemento.beneficio
        break

  def existeElemento(self,elemento: Elemento):
    return elemento in self.elementos

  def imprimir(self):
    for i in range(len(self.elementos)):
      print(self.elementos[i])
    print(self.peso)
    print(self.beneficio)