<div align="center">

# 🐍 Fundamentos de Programación
### AED-1285 · Tecnológico Nacional de México

**Del pensamiento algorítmico a la solución de problemas con Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TecNM](https://img.shields.io/badge/TecNM-AED--1285-17365D?style=for-the-badge)
![Asignatura](https://img.shields.io/badge/Asignatura-Fundamentos_de_Programación-228B72?style=for-the-badge)
![Estado](https://img.shields.io/badge/Material-En_desarrollo-orange?style=for-the-badge)

**Instituto Tecnológico Superior de Pánuco · Extensión Pueblo Viejo**  
**Docente:** Ing. Daniel Arturo Maupomé Rosales

[📚 Temario](#-temario-de-la-asignatura) · [📁 Repositorio](#-estructura-del-repositorio) · [🚀 Cómo comenzar](#-cómo-comenzar) · [🎯 Objetivos](#-objetivos-de-aprendizaje)

</div>

---

## 📖 Acerca de este repositorio

Este espacio reúne ejemplos, ejercicios y prácticas de **Fundamentos de Programación (AED-1285)**, asignatura del **Tecnológico Nacional de México (TecNM)**. El objetivo es acompañar el aprendizaje desde el diseño de algoritmos hasta la construcción de programas que resuelvan problemas reales, utilizando **Python** como lenguaje de trabajo.

> 💡 **La meta no es memorizar instrucciones: es aprender a pensar, diseñar y programar soluciones.**

El temario se presenta completo como guía de estudio. **El código disponible actualmente se organiza en las carpetas `U2` y `U3`**; las demás unidades se incorporarán conforme avance el curso.

## 🎯 Objetivos de aprendizaje

- Analizar problemas y proponer soluciones mediante algoritmos.
- Representar soluciones con diagramas de flujo y pseudocódigo.
- Reconocer los elementos fundamentales de un programa en Python.
- Traducir expresiones matemáticas a instrucciones computacionales.
- Aplicar estructuras secuenciales, selectivas e iterativas.
- Organizar datos y dividir programas en componentes reutilizables.

## 📚 Temario de la asignatura

<details>
<summary><strong>Unidad 1 · Diseño Algorítmico</strong></summary>

- **1.1** Conceptos básicos.
- **1.2** Representación de algoritmos: gráfica y pseudocódigo.
- **1.3** Diseño de algoritmos.
- **1.4** Diseño de funciones.

**Enfoque:** comprender el problema antes de escribir código.

</details>

<details open>
<summary><strong>Unidad 2 · Introducción a la Programación</strong> 🟢</summary>

- **2.1** Conceptos básicos.
- **2.2** Características del lenguaje de programación.
- **2.3** Estructura básica de un programa.
- **2.4** Elementos del lenguaje: tipos de datos, literales, constantes, variables, identificadores, parámetros, operadores y salida de datos.
- **2.5** Traducción de un programa: compilación, enlace, ejecución y errores.

**En Python:** variables, entrada y salida, conversiones de tipos, operadores y expresiones aritméticas.

📂 **[Explorar carpeta U2](./U2)**

</details>

<details open>
<summary><strong>Unidad 3 · Control de Flujo</strong> 🟢</summary>

- **3.1** Estructuras secuenciales.
- **3.2** Estructuras selectivas: simple, doble y múltiple.
- **3.3** Estructuras iterativas: repetir mientras, hasta y desde.

**En Python:** secuencias de instrucciones, `if`, `elif`, `else`, `match`/`case`, `while` y `for` con `range()`. La estructura repetir-hasta se puede simular con `while True` y `break`.

📂 **[Explorar carpeta U3](./U3)**

</details>

<details>
<summary><strong>Unidad 4 · Organización de Datos</strong></summary>

- **4.1** Arreglos.
- **4.2** Unidimensionales: conceptos básicos, operaciones y aplicaciones.
- **4.3** Multidimensionales: conceptos básicos, operaciones y aplicaciones.
- **4.4** Estructuras o registros.

**En Python:** listas, estructuras anidadas y otras formas de agrupar información.

</details>

<details>
<summary><strong>Unidad 5 · Modularidad</strong></summary>

- **5.1** Declaración y uso de módulos.
- **5.2** Paso de parámetros o argumentos.
- **5.3** Implementación.

**En Python:** funciones con `def`, parámetros, valores de retorno e importación de módulos.

</details>

> Los títulos y subtemas siguen el programa de estudios AED-1285 del TecNM. Los ejemplos de Python son una propuesta didáctica para abordar esas competencias.

## 📁 Estructura del repositorio

```text
FundamentosProgramacion/
├── U2/          # Introducción a la Programación
├── U3/          # Control de Flujo
└── README.md    # Guía general de la asignatura
```

**Nota:** la estructura anterior representa las carpetas visibles en la raíz al elaborar este README. Los contenidos específicos de cada carpeta pueden seguir actualizándose.

## 🚀 Cómo comenzar

1. Instala **Python 3** desde [python.org](https://www.python.org/downloads/).
2. Descarga el repositorio o clónalo:

   ```bash
   git clone https://github.com/danielmaupome/FundamentosProgramacion.git
   cd FundamentosProgramacion
   ```

3. Abre las carpetas `U2` o `U3` y elige un archivo `.py`.
4. Ejecútalo desde la terminal:

   ```bash
   python nombre_del_archivo.py
   ```

   En algunos sistemas, el comando puede ser `python3` o `py`.

## 💻 Un vistazo a Python

**Secuencia:** calcular el volumen de un cilindro.

```python
pi = 3.14159265
radio = float(input("Radio: "))
altura = float(input("Altura: "))
volumen = pi * radio**2 * altura
print(f"Volumen: {volumen:.2f}")
```

**Selección:** determinar si una calificación es aprobatoria.

```python
calificacion = int(input("Calificación: "))
if 70 <= calificacion <= 100:
    print("Calificación aprobatoria")
elif 0 <= calificacion < 70:
    print("Calificación no aprobatoria")
else:
    print("Calificación fuera de rango")
```

**Iteración:** recorrer una secuencia de números.

```python
for numero in range(1, 6):
    print(numero)
```

*Estos fragmentos son ejemplos ilustrativos del README, no un inventario verificado de los archivos del repositorio.*

## 🧠 Recomendaciones para estudiantes

- Lee el problema y determina **entradas, proceso y salidas**.
- Escribe primero la solución en lenguaje natural o pseudocódigo.
- Respeta la indentación de Python y usa nombres descriptivos.
- Prueba tus programas con distintos valores y revisa los errores.
- Experimenta: modifica un ejemplo y explica qué cambió.

## 📎 Recursos de consulta

- [Programa oficial AED-1285 (TecNM)](https://www.iztapalapa.tecnm.mx/Carreras/ISC/PDFS-ISC/AED-1285-Fundamentos%20de%20programacion.pdf)
- [Documentación oficial de Python (español)](https://docs.python.org/es/3/)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [PEP 8: guía de estilo](https://peps.python.org/pep-0008/)

## 👨‍🏫 Créditos

**Ing. Daniel Arturo Maupomé Rosales**  
Material de apoyo académico para la asignatura **Fundamentos de Programación · AED-1285**.

Este repositorio es un recurso docente y **no constituye una publicación oficial del TecNM**.

---

<div align="center">

**🧩 Analiza · Diseña · Programa · Prueba · Mejora**

*Cada programa comienza con una buena pregunta y una solución bien pensada.*

</div>
