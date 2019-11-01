import csv

from django.core.management.base import BaseCommand
import datetime
import pytz
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                print(line)
                mytdate = line[4] + ' 08:15:27.10'
                mydate = datetime.datetime.strptime(mytdate, '%Y-%m-%d %H:%M:%S.%f')
                print('Date:', line[4], 'converted:', mydate, 'converted type:', type(mydate))
                # TODO: Добавьте сохранение модели
                temp_phone = Phone(phone_id=int(line[0]),
                                   phone_name=line[1],
                                   phone_image=line[2],
                                   phone_price=line[3],
                                   phone_release_date=pytz.utc.localize(mydate),
                                   phone_lte_exists=bool(line[5]))
                                   #phone_n_slug=)
                temp_phone.save()

