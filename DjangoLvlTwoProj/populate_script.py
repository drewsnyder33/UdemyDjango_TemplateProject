import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoLvlTwoProj.settings')

import django
django.setup()

# Fake population script
# import random
from LvlTwoExercise.models import User
from faker import Faker

fakeGen = Faker()

def populate(N=10):

    for entry in range(N):
        fake_first = fakeGen.first_name()
        fake_last = fakeGen.last_name()
        fake_email = fakeGen.email()

        newUser = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating database...")
    populate()
    print("Population complete.")
