# 🐍 Unidad III · Control de Flujo en Python

**Fundamentos de Programación · AED-1285 · Tecnológico Nacional de México**

> Guía de estudio de los 13 ejemplos de la unidad. Cada sección reproduce el programa original y explica qué hace, cómo lo hace y qué conviene observar al ejecutarlo.

[← Volver al README principal](../README.md)

## 🎯 Objetivo

Aplicar estructuras **secuenciales**, **selectivas** e **iterativas** para construir programas sencillos en Python, comprender su flujo de ejecución y reconocer sus condiciones de entrada y salida.

## 📚 Índice de programas

| Ejemplo | Tema | Archivo |
|---|---|---|
| 01 | 3.1 Secuencial: Saludo y edad futura | [`U3E1.py`](U3E1.py) |
| 02 | 3.1 Secuencial: Cálculo de subtotal, IVA y total | [`U3E2.py`](U3E2.py) |
| 03 | 3.2 Selectiva simple: Condicional simple: temperatura | [`U3E3.py`](U3E3.py) |
| 04 | 3.2 Selectiva doble: Condicional doble: mayoría de edad | [`U3E4.py`](U3E4.py) |
| 05 | 3.2 Selectiva múltiple: Selección múltiple: calificación básica | [`U3E5.py`](U3E5.py) |
| 06 | 3.2 Selectiva múltiple: Selección múltiple: niveles de desempeño | [`U3E6.py`](U3E6.py) |
| 07 | 3.2 Selectiva múltiple: Menú con match-case | [`U3E7.py`](U3E7.py) |
| 08 | 3.2 Selectiva doble: Acceso a torneo con condición OR | [`U3E8.py`](U3E8.py) |
| 09 | 3.3 Mientras: Ciclo while con contador | [`U3E9.py`](U3E9.py) |
| 10 | 3.3 Mientras: Acumulador con valor centinela | [`U3E10.py`](U3E10.py) |
| 11 | 3.3 Hasta (simulación): Repetir hasta acertar una clave | [`U3E11.py`](U3E11.py) |
| 12 | 3.3 Desde: Ciclos for y rangos | [`U3E12.py`](U3E12.py) |
| 13 | 3.3 Desde: Tabla de multiplicar con formato | [`U3E13.py`](U3E13.py) |

## ▶️ Cómo ejecutar los programas

1. Instala Python 3 (para `match-case`, utiliza **Python 3.10 o superior**).
2. Abre una terminal dentro de la carpeta `U3`.
3. Ejecuta, por ejemplo, `python U3E1.py` (en algunos sistemas se utiliza `python3`).
4. Introduce los datos solicitados y observa la salida.

> **Nota:** Los programas se reproducen tal como fueron entregados. Los comentarios sobre límites o validaciones son oportunidades de mejora, no cambios silenciosos al código.

---

## 01. Saludo y edad futura

**Tema:** 3.1 Secuencial · **Archivo:** [`U3E1.py`](U3E1.py)

### Código original

```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))
print(f"Hola, {nombre}")
print(f"El próximo año tendrás {edad + 1}")
```

### Explicación paso a paso

1. `input()` recibe el nombre como texto y lo guarda en `nombre`.
2. `int(input(...))` convierte la edad ingresada a entero.
3. La primera f-string inserta el nombre en el saludo.
4. `edad + 1` calcula la edad del próximo año dentro de otra f-string.

**Prueba:** nombre `Ana`, edad `18` → `Hola, Ana` y `El próximo año tendrás 19`.

**Aprendizaje:** entrada, conversión de tipos, expresiones y salida con f-strings.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 02. Cálculo de subtotal, IVA y total

**Tema:** 3.1 Secuencial · **Archivo:** [`U3E2.py`](U3E2.py)

### Código original

```python
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva
print(f"Total: ${total:.2f}")
```

### Explicación paso a paso

1. `float()` permite introducir un precio decimal; `int()` obtiene la cantidad entera.
2. `subtotal` multiplica precio por cantidad.
3. `iva` calcula el 16 % del subtotal mediante `0.16`.
4. `total` suma subtotal e IVA.
5. `:.2f` muestra exactamente dos cifras decimales.

**Prueba:** precio `100`, cantidad `2` → `Total: $232.00`.

**Aprendizaje:** operaciones aritméticas, variables intermedias y formato monetario. El programa supone IVA de 16 % y no valida valores negativos.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 03. Condicional simple: temperatura

**Tema:** 3.2 Selectiva simple · **Archivo:** [`U3E3.py`](U3E3.py)

### Código original

```python
temperatura = float(input("Temperatura: "))
if temperatura > 35:
    print("Hace mucho calor")
print("Consulta finalizada")
```

### Explicación paso a paso

1. La temperatura se convierte a `float`.
2. `if temperatura > 35:` evalúa una condición estricta: 35 no cumple, 35.1 sí.
3. El mensaje `Hace mucho calor` solo se imprime cuando la condición es verdadera.
4. `Consulta finalizada` está fuera del bloque `if`, por lo que siempre aparece.

**Prueba:** `36` → `Hace mucho calor` y `Consulta finalizada`; `30` → solo `Consulta finalizada`.

**Aprendizaje:** condicional simple, comparación e indentación.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 04. Condicional doble: mayoría de edad

**Tema:** 3.2 Selectiva doble · **Archivo:** [`U3E4.py`](U3E4.py)

### Código original

```python
edad = int(input("Edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

### Explicación paso a paso

1. Se captura una edad entera.
2. `if edad >= 18` incluye el límite de 18 años.
3. Si se cumple, imprime `Mayor de edad`; de lo contrario, `else` imprime `Menor de edad`.

**Prueba:** `18` → `Mayor de edad`; `17` → `Menor de edad`.

**Aprendizaje:** decisión de dos caminos mutuamente excluyentes. No se validan edades negativas.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 05. Selección múltiple: calificación básica

**Tema:** 3.2 Selectiva múltiple · **Archivo:** [`U3E5.py`](U3E5.py)

### Código original

```python
calificacion = int(input("Calificación: "))
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("No aprobado")
```

### Explicación paso a paso

1. Se captura una calificación entera.
2. `if` comprueba primero si es al menos 90.
3. Si no, `elif` comprueba si es al menos 70.
4. `else` cubre cualquier valor inferior a 70.

**Prueba:** `92` → `Excelente`; `80` → `Aprobado`; `65` → `No aprobado`.

**Aprendizaje:** evaluación de condiciones en orden, donde solo se ejecuta la primera rama que corresponda. **Atención:** es un esquema didáctico simplificado, no la clasificación detallada del siguiente ejercicio; tampoco valida 0–100.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 06. Selección múltiple: niveles de desempeño

**Tema:** 3.2 Selectiva múltiple · **Archivo:** [`U3E6.py`](U3E6.py)

### Código original

```python
calificacion = int(input("Calificación: "))
if calificacion < 0 or calificacion > 100:
    print("Calificación no válida")
elif calificacion >= 95:
    print("Excelente")
elif calificacion >= 85:
    print("Notable")
elif calificacion >= 75:
    print("Bueno")
elif calificacion >= 70:
    print("Suficiente")
else:
    print("Insuficiente - Competencia no alcanzada")
```

### Explicación paso a paso

1. El primer `if` rechaza calificaciones menores a 0 o mayores a 100 usando `or`.
2. Las condiciones `elif` se evalúan de mayor a menor, evitando que un 97 se clasifique como `Notable`.
3. Se asignan las etiquetas: 95–100 Excelente; 85–94 Notable; 75–84 Bueno; 70–74 Suficiente.
4. `else` clasifica de 0 a 69 como `Insuficiente - Competencia no alcanzada`.

**Prueba:** `101` → `Calificación no válida`; `88` → `Notable`; `70` → `Suficiente`.

**Aprendizaje:** validación de intervalos y selección múltiple. Este ejemplo clasifica el número introducido; por sí solo no verifica los demás requisitos institucionales de acreditación.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 07. Menú con match-case

**Tema:** 3.2 Selectiva múltiple · **Archivo:** [`U3E7.py`](U3E7.py)

### Código original

```python
opcion = input("Elige A, B o C: ").upper()
match opcion:
    case "A":
        print("Alta")
    case "B":
        print("Baja")
    case "C":
        print("Consulta")
    case _:
        print("Opción inválida")
```

### Explicación paso a paso

1. `input()` lee la opción y `.upper()` transforma letras minúsculas en mayúsculas.
2. `match opcion` compara el valor con los patrones `case`.
3. `A`, `B` y `C` producen `Alta`, `Baja` y `Consulta`.
4. `case _` funciona como alternativa para cualquier otro valor.

**Prueba:** `b` → `Baja`; `z` → `Opción inválida`.

**Aprendizaje:** selección por patrones con `match-case`. **Requiere Python 3.10 o superior.** Las opciones solo muestran mensajes; no realizan altas ni bajas reales.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 08. Acceso a torneo con condición OR

**Tema:** 3.2 Selectiva doble · **Archivo:** [`U3E8.py`](U3E8.py)

### Código original

```python
texto = "Torneo de fútbol Sub23"
print(f"{texto:=^30}")
edad = int(input("Edad: "))
permiso = input("Tiene Permiso? (s/n): ").upper()
if edad <= 23 or permiso == "S":
    print("Acceso autorizado")
else:
    print("Acceso denegado")
```

### Explicación paso a paso

1. Se muestra el título usando `{texto:=^30}`: centra el texto en un campo de ancho mínimo 30 y rellena con `=`.
2. Se solicita la edad y si tiene permiso; `.upper()` normaliza `s` a `S`.
3. `edad <= 23 or permiso == "S"` concede acceso cuando se cumple **al menos una** condición.
4. `else` deniega acceso únicamente si ambas condiciones son falsas.

**Prueba:** edad `25`, permiso `s` → `Acceso autorizado`; edad `25`, permiso `n` → `Acceso denegado`.

**Aprendizaje:** operador lógico `or` y f-strings de alineación. **Observación:** el código autoriza a mayores de 23 con permiso y también a edades negativas; es la regla programada, no necesariamente un reglamento real de torneo.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 09. Ciclo while con contador

**Tema:** 3.3 Mientras · **Archivo:** [`U3E9.py`](U3E9.py)

### Código original

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

print("Fin")
```

### Explicación paso a paso

1. `contador = 1` fija el valor inicial.
2. `while contador <= 5` repite el bloque mientras se cumpla la condición.
3. `print(contador)` muestra el número actual.
4. `contador += 1` equivale a `contador = contador + 1` y evita un ciclo infinito.
5. Al llegar a 6, el ciclo termina y se imprime `Fin`.

**Salida:** `1`, `2`, `3`, `4`, `5` (en líneas distintas) y `Fin`.

**Aprendizaje:** inicialización, condición de continuidad y actualización del contador.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 10. Acumulador con valor centinela

**Tema:** 3.3 Mientras · **Archivo:** [`U3E10.py`](U3E10.py)

### Código original

```python
suma = 0
numero = int(input("Número (0 para salir): "))
while numero != 0:
    suma += numero
    numero = int(input("Número (0 para salir): "))
print(f"Suma: {suma}")
```

### Explicación paso a paso

1. `suma = 0` inicia un acumulador.
2. Se pide el primer número antes del ciclo.
3. `while numero != 0` continúa hasta que se ingresa cero.
4. `suma += numero` agrega cada entrada a la suma.
5. Dentro del ciclo se vuelve a pedir un número para actualizar la condición.
6. El cero sirve como **centinela** y no se suma.

**Prueba:** `5`, `3`, `-2`, `0` → `Suma: 6`.

**Aprendizaje:** acumuladores y terminación mediante valor centinela.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 11. Repetir hasta acertar una clave

**Tema:** 3.3 Hasta (simulación) · **Archivo:** [`U3E11.py`](U3E11.py)

### Código original

```python
while True:
    clave = input("Escribe la clave: ")
    if clave == "python123":
        break
    print("Intenta nuevamente")

print("Acceso concedido")
```

### Explicación paso a paso

1. `while True` inicia un ciclo cuya condición es siempre verdadera.
2. Se solicita una clave en cada iteración.
3. `if clave == "python123":` compara el texto exactamente, incluyendo mayúsculas y minúsculas.
4. `break` interrumpe el ciclo cuando coincide la clave.
5. Si no coincide, aparece `Intenta nuevamente` y se repite.
6. Tras salir del ciclo se imprime `Acceso concedido`.

**Prueba:** `abc` y luego `python123` → primero `Intenta nuevamente`, después `Acceso concedido`.

**Aprendizaje:** simulación de **repetir-hasta** con `while True` y `break`. Es un ejemplo didáctico, no un sistema seguro de autenticación: la clave está escrita directamente en el código.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 12. Ciclos for y rangos

**Tema:** 3.3 Desde · **Archivo:** [`U3E12.py`](U3E12.py)

### Código original

```python
# Imprime los números del 1 al 5 
for numero in range(1, 6):
    print(numero, end=" ")
print()
print("---")
# Imprime los números pares del 2 al 10
for par in range(2, 12, 2):
    print(par, end=" ")
```

### Explicación paso a paso

1. `range(1, 6)` genera 1, 2, 3, 4, 5; el límite superior **no se incluye**.
2. `for numero in ...` recorre cada valor del rango.
3. `end=" "` evita el salto de línea después de cada número.
4. `print()` produce un salto de línea y `print("---")` separa los ejemplos.
5. `range(2, 12, 2)` comienza en 2 y avanza de dos en dos, produciendo 2, 4, 6, 8 y 10.

**Salida:** `1 2 3 4 5`, separador `---`, y `2 4 6 8 10`.

**Aprendizaje:** ciclos de cantidad controlada y los tres parámetros `range(inicio, fin, paso)`.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 13. Tabla de multiplicar con formato

**Tema:** 3.3 Desde · **Archivo:** [`U3E13.py`](U3E13.py)

### Código original

```python
numero = int(input("Tabla del: "))
for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i:2d} = {producto:2d}")
```

### Explicación paso a paso

1. Se solicita el número cuya tabla se imprimirá.
2. `range(1, 11)` recorre los multiplicadores del 1 al 10.
3. `producto = numero * i` calcula el resultado en cada iteración.
4. La f-string compone la operación. `i:2d` y `producto:2d` reservan un ancho mínimo de dos caracteres para alinear números enteros.

**Prueba:** número `3` → líneas desde `3 x  1 =  3` hasta `3 x 10 = 30`.

**Aprendizaje:** combinación de iteración, multiplicación y formato de salida.

**Para reflexionar:** ¿Qué ocurre si cambias los datos de entrada o los valores límite de este programa?

---

## 🧩 Conceptos que se practican

| Estructura | Ejemplos | Elementos clave |
|---|---|---|
| Secuencial | 1–2 | `input`, `int`, `float`, operaciones, `print`, f-strings |
| Selectiva simple | 3 | `if` e indentación |
| Selectiva doble | 4 y 8 | `if`, `else`, `or` |
| Selectiva múltiple | 5–7 | `elif`, validación, `match-case` |
| Iterativa mientras | 9–10 | `while`, contador, acumulador, centinela |
| Iterativa hasta (simulada) | 11 | `while True`, `break` |
| Iterativa desde | 12–13 | `for`, `range`, formato |

## 🧪 Retos de práctica

- Cambia el ejercicio 3 para que también informe cuando la temperatura sea de 35 °C o menos.
- Agrega validación de edad no negativa al ejercicio 4.
- Compara los resultados de los ejercicios 5 y 6 para una calificación de 92.
- Modifica el ejercicio 10 para mostrar cuántos números se sumaron.
- Cambia el ejercicio 12 para imprimir números impares del 1 al 15.
- Adapta el ejercicio 13 para mostrar las tablas del 1 al 5.

## 📌 Observaciones de programación

- `input()` devuelve texto: usa `int()` o `float()` cuando se necesiten números.
- Python utiliza **indentación** para delimitar bloques de control.
- `=` asigna un valor; `==` compara valores.
- `range()` no incluye el valor final.
- Una condición de ciclo debe poder dejar de cumplirse, o el programa debe tener una salida explícita como `break`.
- Algunos ejemplos no validan entradas no numéricas; si el usuario introduce letras donde se espera un número, puede producirse `ValueError`.

---

**Material de apoyo para la asignatura Fundamentos de Programación (AED-1285).**

[⬆ Volver al inicio](#-unidad-iii--control-de-flujo-en-python) · [🏠 Repositorio principal](../README.md)
