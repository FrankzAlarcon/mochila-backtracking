from Mochila import Mochila
from Mochila import Elemento

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

  print(mochila_optimizada.imprimir())
