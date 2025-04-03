# Sistema de Generación y Procesamiento de Transacciones Bancarias

## Introducción
Este proyecto permite:

1. **Generar** archivos CSV con transacciones bancarias
2. **Procesar** el archivo CSV para genera el reporte financiero consolidado

Propósito principal: Automatizar el análisis de movimientos bancarios con Python.

## Instrucciones de Ejecución

### Requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- No se requieren dependencias externas

### Uso Básico

**Generar** archivo CSV inicial (opcional):

    python generatecsv.py

**Procesar** transacciones y generar reporte:

    python main.py

## Enfoque y Solución

### Generación de Transacciones (`generatecsv.py`)

Iteración:
- Usa un bucle for con `range(1, num_records + 1)` para generar N transacciones con IDs secuenciales (1, 2, 3...).

Datos Aleatorios:
- `random.choice()` selecciona aleatoriamente entre Crédito/Débito 
- `random.uniform(10, 1000)` genera montos flotantes entre 10 y 1000, redondeados a 2 decimales.

Decisiones Clave:
- Formato CSV estandarizado: Encabezados compatibles con el archivo princial (id, tipo, monto).
- Precisión monetaria: Montos con `.2f` para garantizar 2 decimales.
- Eficiencia: Escritura en bloque con `csv.DictWriter`.

### Procesamiento y Reporte (`main.py`)

Iteración:
- Recorre cada fila del CSV usando `csv.DictReader`, accediendo a los datos como diccionario (`row['tipo'], row['monto']`).

Cálculo del Balance General:
- Contadores: `credit_count` y `debit_count` se incrementan (`+= 1`) según el tipo de transacción.
- Balance: Suma créditos (`total_balance += amount`) y resta débitos (`total_balance -= amount`).
- Transacción Máxima: Compara cada monto (`float(row['amount'])`) con `max_amount`, actualizando `max_transaction` si se encuentra un valor mayor.

Decisiones Clave:
- Conversión explícita: `float(row['amount'])` evita errores de tipo.
- Eficiencia en comparación: Solo una comparación por transacción (`if amount > max_amount`).
- Formateo claro: Reporte con **f-strings** y alineación visual.

## Estructura del proyecto

    /retotecnico-cobol
    |
    ├── generatecsv.py        # Generador de CSV con valores aleatorios (opcional)
    ├── main.py               # Procesador y reporte (Archivo principal)
    ├── transactions.csv      # Datos de las transacciones (Por defecto contiene los valores descritos en el Reto Técnico)
    └── README.md             # Este archivo