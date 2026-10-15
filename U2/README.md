# 🐍 Fundamentos de Programación: Unidad 2 - Introducción a la Programación

¡Bienvenido al repositorio de **Fundamentos de Python**! Este proyecto contiene una colección de ejemplos prácticos y didácticos diseñados para comprender las bases del lenguaje antes de introducir sentencias de selección (`if`/`else`) o estructuras repetitivas.

---

## 🎯 Objetivos de Aprendizaje

La competencia que se pretende alcanzar es **Conoce y aplica un lenguaje de programación para la resolución de problemas.**

Para ello, tenemos estos ejemplos diseñados

1. **Salida Básica y Caracteres de Escape:** Comprender el funcionamiento de `print()`, el uso de comillas simples/dobles y secuencias de escape como `\n` y `\t`.
2. **Variables y Tipos de Datos:** Identificar la tipificación dinámica de Python (`int`, `float`, `str`, `bool`), aplicar concatenación o suma según el tipo de dato e inspeccionar tipos con `type()`.
3. **Entrada de Datos y Conversión de Tipos (*Casting*):** Leer datos desde teclado con `input()` y realizar conversiones explícitas a enteros (`int`) y flotantes (`float`).
4. **Operadores Aritméticos y Jerarquía:** Comprender la prioridad de evaluación operacional ($() \rightarrow ** \rightarrow *, /, //, \% \rightarrow +, -$), así como el comportamiento de la división entera (`//`), módulo (`%`) y repetición de cadenas (`*`).
5. **Asignación Compuesta:** Aplicar atajos sintácticos (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`) para la actualización acumulativa de variables.
6. **Manipulación de Cadenas e Inmutabilidad:** Utilizar métodos básicos (`.strip()`, `.upper()`, `.lower()`, `.title()`, `.replace()`) y comprobar que las cadenas no sufren cambios sin una reasignación explícita.
7. **Uso de Librerías Estándar (`random` y `math`):** Importar módulos mediante `import` o `from ... import` para la generación de aleatorios y resolución de cálculos matemáticos avanzados.
8. **Salidas Formateadas y Distribución de Espacios (`f-strings`):** Formatear valores numéricos (control de decimales `:.2f` y separador de miles `:,`) y maquetar tablas o tickets mediante alineaciones (`<`, `>`, `^`) y anchos fijos de campo.

---

## 📁 Estructura del Repositorio

| Archivo | Descripción / Conceptos Clave |
| :--- | :--- |
| `U2E1 - Salida en Python.py` | Uso de `print()`, comillas simples/dobles, comillas anidadas, comillas escapadas (`\"`), saltos de línea (`\n`) y tabulaciones (`\t`). |
| `U2E2 - Manejo de Variables.py` | Declaración de variables, concatenación vs. suma con `+`, cálculo de promedios, uso de booleanos e inspección de tipos con `type()`. |
| `U2E3 - Lectura desde teclado y almacenamiento en variables.py` | Captura de datos con `input()`, conversión de datos (*casting*) a `int` y `float`, y despliegue estructurado. |
| `U2E4 - Operadores Aritméticos y Jerarquía.py` | Operadores básicos (`+`, `-`, `*`, `/`, `//`, `%`, `**`), multiplicación de cadenas para separadores (`"-" * 50`) y demostración paso a paso del orden de evaluación. |
| `U2E5 - Operadores de Asignación Compuesta.py` | Modificación acumulativa de variables (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`) aplicada a la economía de un videojuego. |
| `U2E6 - Métodos sobre Cadenas STR.py` | Limpieza de texto con `.strip()`, transformaciones de caso (`.upper()`, `.lower()`, `.title()`), reemplazo con `.replace()` y demostración de la inmutabilidad de `str`. |
| `U2E7 - Uso de Random.py` | Generación de flotantes (`random()`), enteros en rango cerrado (`randint()`) y selección aleatoria sobre listas (`choice()`). Comparación entre `import random` y `from random import ...`. |
| `U2E8 - Funciones del paquete math.py` | Constantes (`pi`, `e`, `inf`), redondeo/truncamiento (`ceil`, `floor`, `trunc`), potencias, raíces, valor absoluto, trigonometría en radianes, logaritmos, factorial y MCD (`gcd`). |
| `U2E9 - Salidas con Formato.py` | Comparación entre `print` tradicional con comas y `f-strings`. Formateo monetario con dos decimales (`:.2f`), remoción de decimales (`:.0f`) y separador de miles (`:,.2f`). |
| `U2E10 - Distribución en Salida.py` | Maquetación en consola mediante `f-strings` especificando anchos de campo y alineaciones: izquierda (`<`), derecha (`>`) y centrado (`^`). |

---

## 💻 Descripción de los Módulos

### 1. Salida Básica en Python (`U2E1 - Salida en Python.py`)
Muestra la flexibilidad de la función `print()` para desplegar información en consola:
* **Comillas:** Permite usar comillas dobles `""` o simples `''`, o bien anidarlas/escaparlas (`\"`) para incluir citas dentro del texto.
* **Secuencias de escape:** Introducción a `\n` para saltos de línea y `\t` para tabular datos y crear columnas simples.

### 2. Manejo de Variables y Tipos (`U2E2 - Manejo de Variables.py`)
Explora la naturaleza dinámica de los tipos de datos en Python:
* **Diferenciación del operador `+`:** Concatenación si se utiliza entre cadenas (`str`) o adición matemática si se aplica entre números (`int`, `float`).
* **Inspección de tipos:** Uso de la función `type()` para verificar el tipo detectado por el intérprete.

### 3. Lectura desde Teclado (`U2E3 - Lectura desde teclado y almacenamiento en variables.py`)
Demuestra cómo recibir interacción del usuario a través de la consola:
* **Captura y Casting:** Dado que `input()` siempre retorna un texto (`str`), se aplican las funciones `int()` y `float()` para transformar el dato a valor numérico antes de su procesamiento.

### 4. Operadores Aritméticos y Jerarquía (`U2E4 - Operadores Aritméticos y Jerarquía.py`)
Cubre la totalidad de los operadores matemáticos de Python y detalla las reglas de evaluación:
* **Operadores especiales:** División real `/` (retorna siempre `float`), división entera `//` (descarta decimales) y módulo `%` (obtiene el residuo).
* **Jerarquía:** Expresiones comparativas que muestran el impacto directo de los paréntesis en el resultado final.

### 5. Operadores de Asignación Compuesta (`U2E5 - Operadores de Asignación Compuesta.py`)
Atajos sintácticos para modificar el valor almacenado en una variable previamente definida:
* **Operaciones directas:** Ejemplos prácticos de `+=`, `-=`, `*=`, `/=`, `//=`, `%=` aplicados al control de un inventario de puntos y monedas en un juego.

### 6. Métodos sobre Cadenas y Su Inmutabilidad (`U2E6 - Métodos sobre Cadenas STR.py`)
Procesamiento básico de cadenas de caracteres:
* **Limpieza y transformación:** Uso de `.strip()` para quitar espacios indeseados, `.title()`, `.upper()`, `.lower()` para ajuste de casos y `.replace()` para la sustitución de fragmentos.
* **Demostración de Inmutabilidad:** Muestra cómo las llamadas a métodos sobre cadenas no alteran la variable original a menos que el resultado sea reasignado.

### 7. Uso del Paquete `random` (`U2E7 - Uso de Random.py`)
Muestra la generación de valores aleatorios mediante la librería estándar:
* **Funciones principales:** Generación de decimales en $[0.0, 1.0)$ con `random()`, enteros en rango cerrado $[a, b]$ con `randint()`, y selección sobre secuencias con `choice()`.
* **Sintaxis de importación:** Análisis del uso de `import random` versus `from random import random`.

### 8. Funciones del Paquete `math` (`U2E8 - Funciones del paquete math.py`)
Uso del módulo matemático para operaciones avanzadas:
* **Herramientas de cálculo:** Uso de constantes (`pi`, `e`), funciones de redondeo (`ceil`, `floor`, `trunc`), potencias/raíces (`pow`, `sqrt`), conversión de grados a radianes (`radians`) y funciones trigonométricas.

### 9. Salidas con Formato (`U2E9 - Salidas con Formato.py`)
Evolución de la salida estándar a la presentación formateada mediante `f-strings`:
* **Sintaxis con llaves:** Inserción directa de variables y cálculos dentro de `{}`.
* **Formatos numéricos:** Control estricto de decimales (`:.2f`) y formateo de montos financieros con comas en miles (`:,.2f`).

### 10. Distribución en Salida (`U2E10 - Distribución en Salida.py`)
Técnicas de alineación y maquetación de texto en consola usando `f-strings`:
* **Alineación de columnas:** Definición de anchos fijos de campo con alineación a la izquierda (`:<15`), derecha (`:>10`) y centrado (`:^12`) para la creación de reportes estructurados.

---

## 🚀 Requisitos e Instalación

Para ejecutar cualquiera de estos scripts solo necesitas tener instalado **Python 3.6+**:

```bash
# Clonar el repositorio
git clone https://github.com/danielmaupome/Fundamentos-de-Programaci-n.git

# Entrar al directorio del proyecto
cd Fundamentos-de-Programaci-n

# Ejecutar cualquiera de los ejemplos
python "U2E1 - Salida en Python.py"
