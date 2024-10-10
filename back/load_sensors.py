import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_city.settings')
django.setup()

from app_smart.models import Sensor

def load_sensors_from_csv(csv_file):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sensor = Sensor(
                tipo=row['tipo'],
                unidade_medida=row['unidade_medida'] if row['unidade_medida'] else None,
                latitude=float(row['latitude'].replace(',', '.')),
                longitude=float(row['longitude'].replace(',', '.')),
                localizacao=row['localizacao'],
                responsavel=row['responsavel'] if row['responsavel'] else '',
                status_operacional=True if row['status_operacional'] == 'True' else False,
                observacao=row['observacao'] if row['observacao'] else '',
                mac_address=row['mac_address'] if row['mac_address'] else None,
            )
            sensor.save()
            print("Sensor salvo com sucesso!")

if __name__ == '__main__':
    file_path = 'dados/sensores.csv'  
    load_sensors_from_csv(file_path)
    print('Sensores carregados com sucesso!')