import sys

def orden_de_la_mejor_carta_posible(cartas):
  pos_calculadas = {}
  suma_parcial = {}
  n = len(cartas)

  for i in range(0,n):
    pos_calculadas[(i,i)] = i
    suma_parcial[(i,i)] = cartas[i]
    
  for i in range(0, n-1):
    pos_calculadas[(i,i+1)] = (i if cartas[i] > cartas[i+1] else i+1)
    suma_parcial[(i,i+1)] = max(cartas[i], cartas[i+1])
  
  for dif in range(2, n):
    for j in range(dif, n):
      i = j - dif
      seleccion_primera = cartas[i] + min(suma_parcial[(i+2,j)], suma_parcial[(i+1,j-1)])
      seleccion_ultima = cartas[j] + min(suma_parcial[(i+1,j-1)], suma_parcial[(i,j-2)])

      if(seleccion_primera > seleccion_ultima):
        pos_calculadas[(i,j)] = i
        suma_parcial[(i,j)] = seleccion_primera
      else:
        pos_calculadas[(i,j)] = j
        suma_parcial[(i,j)] = seleccion_ultima
  return pos_calculadas

def imprimir_informacion(lista1, lista2):
  print("Jugador 1:")
  print(f"Cartas elegidas: {lista1}")
  print(f"Puntos sumados: {sum(lista1)}")
  print()
  print("Jugador 2:")
  print(f"Cartas elegidas: {lista2}")
  print(f"Puntos sumados: {sum(lista2)}")

def imprimir_puntaje(jugada_optimo, cartas):
  puntos_jugador1 = 0
  puntos_jugador2 = 0
  turno_jugador_1 = True
  lista1 = []
  lista2 = []
  i = 0
  j = len(cartas)- 1
  for x in range(0, len(cartas)):
    if turno_jugador_1:
      puntos_jugador1 += cartas[jugada_optimo[(i,j)]]
      lista1 += [cartas[jugada_optimo[(i,j)]]]
    else:
      puntos_jugador2 += cartas[jugada_optimo[(i,j)]]
      lista2 += [cartas[jugada_optimo[(i,j)]]]

    if (jugada_optimo[(i,j)] == i) :
      i += 1
    else:
      j -= 1
    turno_jugador_1 = not turno_jugador_1

  imprimir_informacion(lista1,lista2)


def procesar_entrada_de_cartas():
  linea = sys.stdin.readline()
  cartas = list(map(int,linea.split(',')))
  return cartas

def main():
  cartas = procesar_entrada_de_cartas()
  jugada_optima = orden_de_la_mejor_carta_posible(cartas)
  imprimir_puntaje(jugada_optima, cartas)

main()