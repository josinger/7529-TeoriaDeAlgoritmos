import sys 
import contrato as c

def ordenar_contratos(contratos):
  contratos.sort(key=lambda contrato: contrato.fin)

def hallar_maximo_subconjunto_de_contratos(lista):
  mejor_encontrada = []
  for i in range(len(lista)):
    if not lista[i].es_compatible_con(lista[0]):
      lista_nueva = interval_scheduling_problem(lista, i)
      if len(lista_nueva) > len(mejor_encontrada):
        mejor_encontrada = lista_nueva
  return mejor_encontrada

def interval_scheduling_problem(lista, indice):
  lista_optima = [lista[indice]]
  tiempo_ocupado = c.Contrato(lista[indice].devolver_inicio(), lista[indice].devolver_fin(), "tiempoTotal")
  for i in range(indice+1, len(lista)):
    if lista[i].es_compatible_con(tiempo_ocupado):
      lista_optima.append(lista[i])
      tiempo_ocupado.modificar_fin(lista[i].devolver_fin())
  return lista_optima

def imprimir_contratos(lista):
  for contrato in lista:
    print(contrato.devolver_nombre())

def procesar_entrada():
  lista = []
  linea = sys.stdin.readline()
  while linea:
    nombre, inicio, fin = linea.rstrip("\n").split(",")
    actual = c.Contrato(int(inicio), int(fin), nombre)
    lista.append(actual)
    linea = sys.stdin.readline()
  return lista

def main():
  lista = procesar_entrada()
  ordenar_contratos(lista)
  solucion_optima = hallar_maximo_subconjunto_de_contratos(lista)
  imprimir_contratos(solucion_optima)

main()