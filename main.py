"""
Script para procesar transacciones bancarias desde un archivo CSV y generar un reporte consolidado.

Módulos requeridos:
- csv (estándar de Python)
"""

import csv

def process_transactions(csv_file):
    """
    Procesa un archivo CSV de transacciones y genera un reporte financiero.

    Args:
        csv_filename (str): Ruta del archivo CSV con los datos de transacciones

    Returns:
        str: Reporte formateado con balance, transacción máxima y conteos

    Procesamiento:
        1. Calcula el balance final (créditos - débitos)
        2. Identifica la transacción de mayor monto
        3. Cuenta transacciones por tipo
    """
    # Inicialización de variables
    total_balance = 0.0     # Acumulador para el balance final
    credit_count = 0        # Contador de transacciones de crédito
    debit_count = 0         # Contador de transacciones de débito
    max_amount = 0.0        # Registra el monto más alto encontrado
    max_transaction = None  # Almacena los datos de la transacción máxima
    
    # Abre el archivo CSV usando context manager para manejo seguro de recursos
    with open(csv_file, mode='r',encoding='utf-8') as file:
        reader = csv.DictReader(file) # Crea un lector de CSV como diccionario
        
        # Procesa cada fila del archivo CSV
        for row in reader:
            # Convierte el monto a float para operaciones matemáticas
            amount = float(row['monto'])

            # Procesa según el tipo de transacción
            if row['tipo'] == 'Crédito':
                total_balance += amount
                credit_count += 1
            elif row['tipo'] == 'Débito':
                total_balance -= amount
                debit_count += 1
            
            # Actualiza la transacción de mayor monto
            if amount > max_amount:
                max_amount = amount
                max_transaction = row
    
    # Genera el reporte usando f-strings para formateo profesional
    report = f"""
    Reporte de Transacciones
    ---------------------------------------------
    Balance Final: {total_balance:.2f}
    Transacción de Mayor Monto: ID {max_transaction['id']} - {max_amount:.2f}
    Conteo de Transacciones: Crédito: {credit_count} Débito: {debit_count}
    """
    return report

# Ejemplo de uso (sección ejecutable)
if __name__ == "__main__":
    # Configuración
    csv_filename = 'transactions.csv'  # Nombre del archivo de entrada
    try:
        # Genera y muestra el reporte
        print(process_transactions(csv_filename))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_filename}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
