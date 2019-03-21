#Copyright (C) <2019>  <John Díaz / HapticLemon>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


# Gráfica de frecuencias relativas de palabras en libros.
# La monto en base a dos libros, usando frecuencias relativas (f_abs/long_texto)
# para que puedan compararse libros con diferente número de páginas.
# Otro problema es que no todos los libros tienen palabras de la misma longitud
# Ej : uno puede tener una palabra de longitud 20 y el otro no, por lo que hay que
# hacer los cálculos para las longitudes comunes a ambos libros. Una solución fácil
# sería tomar longitudes de palabra "normales", por ejemplo de 1 a 15 y eliminar las
# demás, pero no es seguro, ya que se podría colar alguna.

# Habría que automatizar el proceso para que se le puedan pasar varios libros o que 
# al menos lo haga con funciones generales en lugar de repitiendo código.

import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys

# Abre archivo y devuelve su contenido
# nombre : nombre del archivo
def read_file(nombre):
	try:
		file_handle = open(nombre,'r')
		return file_handle.read()
	except:
		print('Error al abrir el archivo ' + nombre)
		sys.exit()

# Frecuencia relativa de una palabra en un texto.
# texto : el texto en el que se mide
# freq_palabra : frecuencia absoluta de la palabra.
def frecuencia_relativa(texto, frecuencia_absoluta):
	return frecuencia_absoluta / len(texto)

# Leemos los archivos, tokenizamos y sacamos las frecuencias de las palabras.
# He usado dos textos de Philip K. Dick : "La segunda variedad" y "El hombre variable"
# Se pueden cambiar por los que tengas disponibles :)

pkdsv = read_file('PKD_Segunda_variedad.txt')
text_sv = nltk.word_tokenize(pkdsv)
fdist_sv = FreqDist(len(palabra) for palabra in text_sv)

pkdhv = read_file('PKD_Hombre_variable.txt')
text_hv = nltk.word_tokenize(pkdhv)
fdist_hv = FreqDist(len(palabra) for palabra in text_hv)

# Ordenamos las longitudes de las palabras con sus frecuencias.
sorted_by_first_hv = sorted(fdist_hv.items(), key=lambda tup: tup[0])
sorted_by_first_sv = sorted(fdist_sv.items(), key=lambda tup: tup[0])

# Convierto las listas de tuplas en diccionarios.
dict_hv = dict(sorted_by_first_hv)
dict_sv = dict(sorted_by_first_sv)

# Monto un nuevo diccionario con los elementos comunes de ambas y los valores del primero
dict_hv_2 = {}
for key in dict_hv:
	if key in dict_sv:
		dict_hv_2.update({key:dict_hv[key]})

# Monto un nuevo diccionario con los elementos comunes de ambas y los valores del primero
dict_sv_2 = {}
for key in dict_sv:
	if key in dict_hv:
		dict_sv_2.update({key:dict_sv[key]})

# Vuelvo a convertir en lista; ahora tenemos dos pero con claves. Ahora sí que podemos 
# hacer una comparación adecuada.
hv_list = dict_hv_2.items()
sv_list = dict_sv_2.items()

# https://stackoverflow.com/questions/37266341/plotting-a-python-dict-in-order-of-key-values
# Es resultado son tuplas (), inmutables. Seguramente se puede hacer con listas sin liar
# tanto la cosa con tipos.
x_hv,y_hv = zip(*hv_list)
x_sv,y_sv = zip(*sv_list)

# Para poder comparar los dos textos hemos de usar frecuencias relativas, ya que los
# libros tienen diferente longitud y no son equiparables. Más arriba he definido las
# funciones y hago un mapeo del cálculo de la fr a cada elemento de la lista de 
# frecuencias absolutas.
y_hv_fr = [frecuencia_relativa(text_hv,x) for x in y_hv]
y_sv_fr = [frecuencia_relativa(text_sv,x) for x in y_sv]

plt.plot(y_hv_fr, color ='red')
plt.plot(y_sv_fr, color ='blue')

# Añadimos la leyenda con los títulos de los libros.
red_patch = mpatches.Patch(color='red', label='Hombre variable')
blue_patch = mpatches.Patch(color='blue', label='La segunda variedad')

plt.legend(handles=[red_patch,blue_patch])

# De este modo toma las x como etiquetas (3,1,2...) en lugar de como valores
# (lo que desordena la gráfica.
plt.xticks(range(len(y_hv_fr)), x_hv)
plt.show()

