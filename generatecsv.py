import csv
import random
def generate_csv(filename, num_records=50):
    types = ['Crédito', 'Débito']
    with open(filename, 'w', newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'tipo', 'monto'])
        writer.writeheader()
        for i in range(1, num_records + 1):
            writer.writerow({
                'id': i,
                'tipo': random.choice(types),
                'monto': f"{random.uniform(10, 1000):.2f}"
            })
generate_csv('transactions.csv')