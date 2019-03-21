# NLTK_test
Pruebas de concepto con NLTK (Procesamiento de lenguaje natural) en Python

El análisis de frecuencias de términos en textos permite obtener una "firma" característica del autor de los mismos,
ya que no hay dos personas que usen el lenguaje de la misma forma. Python, mediante NLTK proporciona un conjunto de herramientas específicas y fáciles de utilizar que nos permiten hacer pruebas de concepto de forma rápida y sin complicaciones.

He escrito "al vuelo" -es decir, el código es francamente mejorable :) - una prueba de concepto para obtener la firma
de dos textos de Philip K. Dick (si te gustan los autores de ciencia ficción que cuestionan la realidad en cada obra, éste es tu hombre) en forma de gráfica.

Algunas notas :

En el eje y de la gráfica podemos ver las frecuencias relativas de las palabras usadas en cada texto.
En el eje x las longitudes ordenadas de las palabras usadas en los textos.

Hay que tener en cuenta que ambos textos no tienen por qué usar palabras de la misma longitud, es decir, en el primero podemos tener algún vocablo de longitud 23 y en el segundo no. Para una comparación precisa hay que descartar todas las longitudes que no sean comunes. Así mismo, al tener las obras diferentes longitudes, uso frecuencias relativas para poder comparar.

Obviamente el código necesita mucha revisión, ya que se ha "hardcodeado" el uso de dos archivos, repitiendo muchas líneas y probablemente hay conversiones de tipos innecesarias, pero ¡hey!, es tan solo una prueba de concepto :D
