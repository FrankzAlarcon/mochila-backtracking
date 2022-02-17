class Elemento:
  def __init__(self, peso, beneficio):
      self.peso = peso
      self.beneficio = beneficio
  
  def __eq__(self, otro_elemento):
      return self.peso == otro_elemento.peso and self.beneficio == otro_elemento.beneficio

class Mochila:
  def __init__(self, pesoMaximo):
      self.pesoMaximo = pesoMaximo
      self.elementos = []
      self.beneficio = 0
      self.peso = 0

  def anadirElemento(self, elemento: Elemento):
    if elemento not in self.elementos:
      self.elementos.append(elemento)
      self.beneficio += elemento.beneficio
      self.peso += elemento.peso

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
      print('Peso: ', self.elementos[i].peso, 'Beneficio: ', self.elementos[i].beneficio)
    print(self.peso)
    print(self.beneficio)

def llenarMochila(mochila_base: Mochila, elementos, mochila_optima:Mochila, estaLLeno):
  if estaLLeno:
    if mochila_base.beneficio > mochila_optima.beneficio:
      #si la mochila tiene mas beneficio que la mochila optima
      mochila_optima.reset()#resetea toda la mochila
      for i in range(len(mochila_base.elementos)):
        #poner todos los elementos en la mochila optima
        mochila_optima.anadirElemento(mochila_base.elementos[i])
  else:
    for i in range(len(elementos)):
      # print(mochila_base.existeElemento(elementos[i]))
      if not mochila_base.existeElemento(elementos[i]):
        if mochila_base.pesoMaximo > mochila_base.peso + elementos[i].peso:
          mochila_base.anadirElemento(elementos[i])
          llenarMochila(mochila_base, elementos, mochila_optima, False)
          mochila_base.eliminarElemento(elementos[i])
        else:
          llenarMochila(mochila_base, elementos, mochila_optima, True)


if __name__ == "__main__":
  elementos = [
    Elemento(1,1),
    Elemento(2,2),
    Elemento(4,10),
    Elemento(1,2),
    Elemento(12,4)
  ]
  mochila_base = Mochila(15)
  mochila_optimizada = Mochila(15)
  llenarMochila(mochila_base, elementos, mochila_optimizada, False)

  mochila_optimizada.imprimir()