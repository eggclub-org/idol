from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from datetime import datetime
import os
import csv
from info_idol.models import InfoIdol

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Command(BaseCommand):
    # Show this when user type help
    help = 'Import database command'

    def handle(self, *args, **options):
        self.stdout.write('Import database...')

        data_dir = BASE_DIR[:BASE_DIR.find('web/') + 4]
        db_file_path = os.path.join(data_dir, 'import_db/data.csv')
        with open(db_file_path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%m/%d/%y')
                height = row['height']
                v1 = row['v1']
                v2 = row['v2']
                v3 = row['v3']
                list_film = row['list_film'].replace('"', '').replace(',', ', ')

                with atomic():
                    InfoIdol.objects.create(
                        name=name,
                        birthday=birthday,
                        height=height,
                        v1=v1,
                        v2=v2,
                        v3=v3,
                        list_film=list_film
                    )