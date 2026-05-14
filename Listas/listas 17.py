lista = [[1, 2], [3, 4], [5, 6]]
achatada = [item for sublista in lista for item in sublista]
print(achatada)