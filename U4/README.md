# 🐍 Unidad IV · Estructuras de Datos en Python

**Fundamentos de Programación · AED-1285 · Tecnológico Nacional de México**

> Guía de estudio de los 8 ejemplos de la unidad. Cada sección presenta el propósito del programa, los conceptos que utiliza y aspectos que conviene observar al ejecutarlo. El código fuente se consulta mediante el enlace de cada archivo.

[**← Volver al README principal**](../README.md)

## 🎯 Objetivo

Utilizar estructuras de datos fundamentales de Python para almacenar, organizar, consultar y manipular información. Comprender las características de las **listas**, **tuplas**, **conjuntos** y **diccionarios**, así como seleccionar la estructura adecuada de acuerdo con las necesidades de una aplicación.

## 📚 Índice de programas

| Ejemplo | Tema | Archivo |
|---|---|---|
| 01 | 4.1 Listas: operaciones y métodos | [`U4E1_Lista.py`](U4E1_Lista.py) |
| 02 | 4.1 Listas: inscripción y calificaciones | [`U4E2_Lista.py`](U4E2_Lista.py) |
| 03 | 4.2 Tuplas: operaciones y características | [`U4E1_Tuplas.py`](U4E1_Tuplas.py) |
| 04 | 4.2 Tuplas: admisión de aprendices en Hogwarts | [`U4E2_Tuplas.py`](U4E2_Tuplas.py) |
| 05 | 4.3 Conjuntos: operaciones y métodos | [`U4E5_Conjuntos.py`](U4E5_Conjuntos.py) |
| 06 | 4.3 Conjuntos: análisis de conjuntos en Matemáticas Discretas | [`U4E6_Conjuntos.py`](U4E6_Conjuntos.py) |
| 07 | 4.4 Diccionarios: operaciones y métodos | [`U4E7_Diccionarios.py`](U4E7_Diccionarios.py) |
| 08 | 4.4 Diccionarios: interfaz bilingüe español/inglés | [`U4E8_Diccionarios.py`](U4E8_Diccionarios.py) |

## ▶️ Cómo ejecutar los programas

1. Instala Python 3.
2. Abre una terminal dentro de la carpeta `U4`.
3. Ejecuta el archivo que quieras revisar. Por ejemplo: `python U4E1_Lista.py` (en algunos sistemas se utiliza `python3`).
4. Introduce los datos solicitados y observa la salida.
5. Para estudiar un programa por secciones, revisa los comentarios y ejecuta el archivo desde tu editor.

> **Nota:** Los programas tienen un propósito didáctico. Las explicaciones describen el comportamiento del código incluido; las actividades de reflexión proponen posibles mejoras o extensiones.

---

## 01. Exploración de listas

**Tema:** 4.1 Estructuras de datos: listas · **Archivo:** [`U4E1_Lista.py`](U4E1_Lista.py)

### Propósito

Presenta la creación de listas, el acceso mediante índices, la modificación de elementos, los métodos para agregar y eliminar datos, el recorrido y el trabajo con listas relacionadas.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E1_Lista.py)**.

### Explicación paso a paso

1. `[]` crea una lista y permite almacenar varios elementos, incluso de distintos tipos.
2. `append()`, `extend()` e `insert()` agregan elementos de diferentes maneras.
3. `sort()` y `reverse()` modifican el orden de la lista original.
4. `remove()`, `del` y `pop()` permiten eliminar elementos.
5. `len()`, `index()` y el operador `in` ayudan a consultar la lista.
6. `for`, `range()` y `enumerate()` permiten recorrer sus elementos.
7. `zip()` permite recorrer simultáneamente listas relacionadas, como productos y precios.

**Prueba sugerida:** Observar cómo cambia la lista después de cada operación y comprobar que las posiciones de productos y precios se mantienen relacionadas.

**Aprendizaje:** Presenta la creación de listas, el acceso mediante índices, la modificación de elementos, los métodos para agregar y eliminar datos, el recorrido y el trabajo con listas relacionadas.

**Para reflexionar:** ¿Qué podría ocurrir si se agrega un producto a la lista de productos, pero no se agrega su precio en la posición correspondiente?

---


## 02. Aplicación: inscripción de estudiantes y captura de calificaciones

**Tema:** 4.1 Estructuras de datos: listas · **Archivo:** [`U4E2_Lista.py`](U4E2_Lista.py)

### Propósito

Construye un pequeño sistema que registra estudiantes en una materia, ordena sus nombres, captura calificaciones y calcula el promedio grupal.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E2_Lista.py)**.

### Explicación paso a paso

1. Una lista almacena los nombres de los estudiantes inscritos.
2. `while` permite registrar nombres hasta que se escriba `salir`.
3. `append()` agrega cada nuevo estudiante.
4. `sort()` ordena alfabéticamente la lista.
5. Una segunda lista almacena las calificaciones en el mismo orden.
6. `enumerate()` permite mostrar cada estudiante junto con la calificación ubicada en la misma posición.
7. `sum()` y `len()` permiten calcular el promedio.

**Prueba sugerida:** Registrar varios estudiantes, finalizar la captura y después introducir una calificación para cada uno. Comparar el reporte con el promedio calculado.

**Aprendizaje:** Construye un pequeño sistema que registra estudiantes en una materia, ordena sus nombres, captura calificaciones y calcula el promedio grupal.

**Para reflexionar:** ¿Por qué es importante mantener el mismo orden en las listas de estudiantes y calificaciones?

---


## 03. Exploración de tuplas

**Tema:** 4.2 Estructuras de datos: tuplas · **Archivo:** [`U4E1_Tuplas.py`](U4E1_Tuplas.py)

### Propósito

Explica cómo crear tuplas, acceder a sus elementos, obtener segmentos, consultar información y combinar tuplas. También compara las tuplas con las listas.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E1_Tuplas.py)**.

### Explicación paso a paso

1. Las tuplas se crean normalmente con paréntesis y sus elementos se separan mediante comas.
2. Una tupla de un solo elemento requiere una coma final, por ejemplo `(25,)`.
3. Los índices positivos y negativos permiten consultar elementos; el slicing obtiene segmentos.
4. `count()` cuenta apariciones e `index()` devuelve la posición de un elemento.
5. El operador `in` verifica si un elemento pertenece a la tupla.
6. `+` concatena tuplas y `*` repite sus elementos.
7. `for`, `range()` y `enumerate()` permiten recorrerlas.
8. El desempaquetado asigna los elementos de una tupla a variables.
9. `sorted()` devuelve una lista ordenada; se puede convertir nuevamente con `tuple()`.
10. La inmutabilidad impide cambiar o eliminar directamente elementos de una tupla.

**Prueba sugerida:** Ejecutar los ejemplos de consulta y recorrido. Después, descomentar por separado las instrucciones que intentan modificar o eliminar elementos para observar el error.

**Aprendizaje:** Explica cómo crear tuplas, acceder a sus elementos, obtener segmentos, consultar información y combinar tuplas. También compara las tuplas con las listas.

**Para reflexionar:** ¿En qué situaciones conviene utilizar una tupla en lugar de una lista?

---


## 04. Aplicación: sistema de admisión de Hogwarts

**Tema:** 4.2 Estructuras de datos: tuplas · **Archivo:** [`U4E2_Tuplas.py`](U4E2_Tuplas.py)

### Propósito

Simula el registro de aprendices del Colegio Hogwarts de Magia y Hechicería. Cada aprendiz se representa mediante una tupla con nombre, edad, casa y habilidad mágica; una lista reúne todos los registros.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E2_Tuplas.py)**.

### Explicación paso a paso

1. La lista `aprendices` almacena los registros capturados.
2. Cada registro es una tupla con cuatro datos: nombre, edad, casa y habilidad.
3. La tupla `casas` contiene las cuatro casas disponibles.
4. El ciclo `while` permite registrar aprendices hasta escribir `salir`.
5. `in` valida que la casa seleccionada exista en la tupla de casas.
6. `append()` agrega cada tupla a la lista de aprendices.
7. `sorted()` crea una nueva lista ordenada por el contenido de las tuplas; en este ejemplo, el nombre es el primer elemento.
8. El programa busca aprendices, calcula la edad promedio y cuenta cuántos pertenecen a cada casa.

**Prueba sugerida:** Registrar aprendices de distintas casas, generar el reporte, buscar un nombre existente y otro inexistente, y revisar las estadísticas.

**Aprendizaje:** Simula el registro de aprendices del Colegio Hogwarts de Magia y Hechicería. Cada aprendiz se representa mediante una tupla con nombre, edad, casa y habilidad mágica; una lista reúne todos los registros.

**Para reflexionar:** ¿Por qué se utiliza una lista para almacenar a todos los aprendices y una tupla para representar los datos de cada uno?

---


## 05. Exploración de conjuntos

**Tema:** 4.3 Estructuras de datos: conjuntos · **Archivo:** [`U4E5_Conjuntos.py`](U4E5_Conjuntos.py)

### Propósito

Presenta los conjuntos como colecciones sin elementos duplicados y sin posiciones definidas. Incluye operaciones para agregar, eliminar, consultar y comparar conjuntos.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E5_Conjuntos.py)**.

### Explicación paso a paso

1. `{}` con elementos crea un conjunto; `set()` crea un conjunto vacío. Las llaves vacías `{}` crean un diccionario.
2. `add()` agrega un elemento y `update()` agrega varios.
3. `remove()`, `discard()`, `pop()` y `clear()` permiten eliminar elementos con comportamientos diferentes.
4. `len()` y `in` permiten consultar cantidad y pertenencia.
5. `union()` o `|` obtiene la unión.
6. `intersection()` o `&` obtiene la intersección.
7. `difference()` o `-` obtiene la diferencia.
8. `symmetric_difference()` o `^` obtiene la diferencia simétrica.
9. `issubset()`, `issuperset()` e `isdisjoint()` permiten comprobar relaciones entre conjuntos.
10. `copy()` crea una copia y `frozenset()` crea un conjunto inmutable.
11. `sorted()` permite presentar los elementos ordenados, aunque devuelve una lista.

**Prueba sugerida:** Crear dos conjuntos con elementos repetidos y ejecutar unión, intersección, diferencia y diferencia simétrica. Comparar los resultados con las operaciones escritas en notación matemática.

**Aprendizaje:** Presenta los conjuntos como colecciones sin elementos duplicados y sin posiciones definidas. Incluye operaciones para agregar, eliminar, consultar y comparar conjuntos.

**Para reflexionar:** ¿Por qué no podemos acceder a un elemento de un conjunto mediante un índice?

---


## 06. Aplicación: análisis de conjuntos en Matemáticas Discretas

**Tema:** 4.3 Estructuras de datos: conjuntos · **Archivo:** [`U4E6_Conjuntos.py`](U4E6_Conjuntos.py)

### Propósito

Analiza los lenguajes de programación que conocen los estudiantes de un grupo. El universo contiene a todos los estudiantes y tres conjuntos representan quiénes conocen Python, Java y C++.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E6_Conjuntos.py)**.

### Explicación paso a paso

1. El conjunto `estudiantes` representa el universo de la encuesta.
2. Los conjuntos `python`, `java` y `cpp` almacenan a quienes conocen cada lenguaje.
3. El programa verifica que los nombres ingresados pertenezcan al universo registrado.
4. La unión identifica a quienes conocen al menos uno de los lenguajes.
5. La intersección identifica a quienes conocen los tres lenguajes y también permite analizar pares.
6. La diferencia permite identificar quiénes conocen solamente un lenguaje.
7. El complemento se obtiene restando del universo a quienes conocen al menos un lenguaje.
8. La diferencia simétrica identifica a quienes pertenecen a uno de dos conjuntos, pero no a ambos.
9. `len()` permite obtener la cardinalidad de los conjuntos.
10. `issubset()`, `issuperset()` e `isdisjoint()` permiten comprobar relaciones.

**Prueba sugerida:** Registrar un grupo pequeño y asignar estudiantes a los conjuntos de Python, Java y C++. Comprobar manualmente las operaciones con un diagrama de Venn.

**Aprendizaje:** Analiza los lenguajes de programación que conocen los estudiantes de un grupo. El universo contiene a todos los estudiantes y tres conjuntos representan quiénes conocen Python, Java y C++.

**Para reflexionar:** ¿Cómo se interpreta el complemento de la unión de Python, Java y C++ respecto al universo de estudiantes?

---


## 07. Exploración de diccionarios

**Tema:** 4.4 Estructuras de datos: diccionarios · **Archivo:** [`U4E7_Diccionarios.py`](U4E7_Diccionarios.py)

### Propósito

Explica cómo almacenar información mediante pares de clave y valor, consultar y modificar datos, recorrer diccionarios y organizar estructuras anidadas.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E7_Diccionarios.py)**.

### Explicación paso a paso

1. Los diccionarios se crean con llaves y almacenan pares de clave y valor.
2. Los valores se consultan mediante su clave o con `get()`.
3. La asignación permite agregar una clave nueva o modificar su valor.
4. `update()` actualiza varios pares; `setdefault()` agrega una clave solamente si no existe.
5. `in` verifica la existencia de claves; `values()` permite consultar los valores.
6. `keys()`, `values()` e `items()` permiten obtener claves, valores y pares.
7. `pop()`, `popitem()`, `del` y `clear()` permiten eliminar información.
8. `copy()` crea una copia del diccionario.
9. Los diccionarios pueden contener otros diccionarios, listas y diferentes tipos de datos.
10. Las claves deben ser únicas; si una clave se repite al crear el diccionario, prevalece el último valor asignado.

**Prueba sugerida:** Crear un diccionario, agregar y modificar datos, consultar claves existentes e inexistentes y recorrer sus pares con `items()`.

**Aprendizaje:** Explica cómo almacenar información mediante pares de clave y valor, consultar y modificar datos, recorrer diccionarios y organizar estructuras anidadas.

**Para reflexionar:** ¿Qué ventajas ofrece consultar un dato mediante una clave descriptiva en lugar de utilizar una posición numérica?

---


## 08. Aplicación: interfaz bilingüe español/inglés

**Tema:** 4.4 Estructuras de datos: diccionarios · **Archivo:** [`U4E8_Diccionarios.py`](U4E8_Diccionarios.py)

### Propósito

Construye una interfaz de consola cuyos textos cambian entre español e inglés. Los diccionarios anidados almacenan las traducciones y permiten mostrar menús, perfil, notificaciones y configuración en el idioma seleccionado.

### Código fuente

Consulta o abre el programa completo desde el siguiente enlace: **[Abrir archivo Python](U4E8_Diccionarios.py)**.

### Explicación paso a paso

1. El diccionario `idiomas` contiene dos claves principales: `es` y `en`.
2. Cada idioma contiene un diccionario interno con los textos de la interfaz.
3. El diccionario `usuario` almacena los datos del perfil.
4. La lista `notificaciones` contiene mensajes que se muestran al usuario.
5. La variable `idioma` determina qué conjunto de textos se utiliza.
6. El menú permite consultar perfil, notificaciones y configuración.
7. La opción de cambio de idioma verifica que la clave ingresada exista en `idiomas`.
8. Al cambiar la variable `idioma`, los siguientes textos del menú se muestran en el idioma seleccionado.

**Prueba sugerida:** Ejecutar la aplicación en español, cambiar a inglés, recorrer las opciones del menú y regresar a español.

**Aprendizaje:** Construye una interfaz de consola cuyos textos cambian entre español e inglés. Los diccionarios anidados almacenan las traducciones y permiten mostrar menús, perfil, notificaciones y configuración en el idioma seleccionado.

**Para reflexionar:** ¿Qué tendrías que agregar al diccionario `idiomas` para incorporar un tercer idioma sin modificar la lógica del menú?

---

## 🧩 Conceptos que se practican

| Estructura | Ejemplos | Elementos clave |
|---|---|---|
| Listas | 01–02 | Índices, slicing, `append()`, `extend()`, `insert()`, `sort()`, `remove()`, `pop()`, `zip()` |
| Tuplas | 03–04 | Inmutabilidad, índices, slicing, `count()`, `index()`, concatenación, desempaquetado |
| Conjuntos | 05–06 | Elementos únicos, pertenencia, unión, intersección, diferencia, complemento y cardinalidad |
| Diccionarios | 07–08 | Claves y valores, `get()`, `update()`, `keys()`, `values()`, `items()` y estructuras anidadas |

## 🧪 Retos de práctica

- **Listas:** agrega una opción para modificar la calificación de un estudiante y vuelve a calcular el promedio.
- **Tuplas:** incorpora un nuevo dato al registro de cada aprendiz y adapta el reporte para mostrarlo.
- **Conjuntos:** agrega un cuarto lenguaje de programación y analiza las operaciones entre los cuatro conjuntos.
- **Diccionarios:** incorpora un tercer idioma a la interfaz y traduce todos los textos del menú.
- **Comparación:** representa la misma información utilizando una lista, una tupla, un conjunto y un diccionario. Explica qué cambia y qué estructura resulta más conveniente.

## 📌 Observaciones de programación

- Las **listas** son colecciones ordenadas y mutables; permiten agregar, modificar y eliminar elementos.
- Las **tuplas** son colecciones ordenadas e inmutables; una vez creadas, no se pueden modificar directamente.
- Los **conjuntos** almacenan elementos únicos y no permiten acceder a ellos mediante índices. No debe suponerse un orden específico al recorrerlos.
- Los **diccionarios** almacenan pares de clave y valor. Las claves deben ser únicas y permiten consultar directamente la información asociada.
- `sorted()` devuelve una nueva lista ordenada; no modifica la colección original.
- `input()` devuelve texto. Cuando se necesitan números, deben utilizarse conversiones como `int()` o `float()`.
- Los métodos de modificación de listas, conjuntos y diccionarios pueden cambiar la estructura original.
- Las estructuras pueden combinarse. Por ejemplo, una lista puede almacenar tuplas y un diccionario puede contener listas u otros diccionarios.
- Los ejemplos de esta unidad se enfocan en las estructuras de datos y en su uso con los elementos de programación estudiados previamente.

---

**Material de apoyo para la asignatura Fundamentos de Programación (AED-1285).**

[**⬆ Volver al inicio**](#-unidad-iv--estructuras-de-datos-en-python) · [**🏠 Repositorio principal**](../README.md)
