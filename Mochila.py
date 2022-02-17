class Elemento:
  def __init__(self, peso, beneficio):
      self.peso = peso
      self.beneficio = beneficio
  
  #comparar dos objetos Elemento
  def __eq__(self, otro_elemento):
      return self.peso == otro_elemento.peso and self.beneficio == otro_elemento.beneficio

class Mochila:
  def __init__(self, pesoMaximo):
      self.pesoMaximo = pesoMaximo
      self.elementos = []
      self.beneficio = 0
      self.peso = 0

  #Añade un elemento a la mochila
  def anadirElemento(self, elemento: Elemento):
    if elemento not in self.elementos:
      self.elementos.append(elemento)
      self.beneficio += elemento.beneficio
      self.peso += elemento.peso

  #Resetea la mochila
  def reset(self):
    self.peso = 0
    self.beneficio = 0
    self.elementos = []

  #Elimina un elmento de la mochila
  def eliminarElemento(self, elemento: Elemento):
    for i in range(len(self.elementos)):
      if self.elementos[i] == elemento:
        self.elementos.pop(i)
        self.peso -= elemento.peso
        self.beneficio -= elemento.beneficio
        break

  #Verifica si un Elemento ya está en la mochila
  def existeElemento(self,elemento: Elemento):
    return elemento in self.elementos

  #Imprime el contenido de la mochila
  def imprimir(self):
    for i in range(len(self.elementos)):
      print('Peso: ', self.elementos[i].peso, 'Beneficio: ', self.elementos[i].beneficio)
    print('Peso en mochila: ',self.peso)
    print('Beneficio en mochila: ',self.beneficio)

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
      if not mochila_base.existeElemento(elementos[i]):
        #Si el elemento no esta en la mochila
        if mochila_base.pesoMaximo > mochila_base.peso + elementos[i].peso:
          #si el peso de la mochila + el peso del elemento a ingresar
          #es menor que el peso maximo de la mochila
          mochila_base.anadirElemento(elementos[i])
          llenarMochila(mochila_base, elementos, mochila_optima, False)
          mochila_base.eliminarElemento(elementos[i])
        else:
          #Backtracking
          llenarMochila(mochila_base, elementos, mochila_optima, True)


if __name__ == "__main__":
  #Grupo 1: Frankz Alarcon, Jhonattan Amagua, Christian Pazmiño

  elementos = []
  peso_max = float(input('Ingrese el peso máximo de la mochila: '))
  mochila_base = Mochila(peso_max)
  mochila_optima = Mochila(peso_max)
  num_elementos  =  int(input('Ingrese el numero de elementos: '))
  for index in range(num_elementos):
    peso = float(input('Ingrese el peso del elemento ' + str(index + 1) + ': '))
    beneficio = float(input('Ingrese el beneficio del elemento ' + str(index + 1) + ': '))
    elementos.append(Elemento(peso, beneficio))
  print('Elementos: ')
  for elemento in elementos:
    print([elemento.peso, elemento.beneficio], end=" ")
  llenarMochila(mochila_base, elementos, mochila_optima, False)
  print()
  print('Resultados en mochila: ')
  mochila_optima.imprimir()