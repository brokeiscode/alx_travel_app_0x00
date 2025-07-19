from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from listings.models import Listing
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with sample listing.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data population...'))

        # Create or get User
        self.stdout.write('Creating/getting sample users...')
        host_user, created = User.objects.get_or_create(
            username='alx_travel_app',
            defaults={'email': 'alx_travel_app@example.com'}
        )
        if created:
            host_user.set_password('password')
            host_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created new host user: {host_user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Host user already exists: {host_user.username}'))

        # Create a Listings
        self.stdout.write('\nCreating/getting a sample listing...')
        titles = ['Cozy Apartment ', 'Luxury Block ','Casear Project Apt ']
        locations = ['Jones Street', 'John Blvd', 'Ogunnaike Close', 'Adeogun Avenue', 'Williams Lane']
        for _ in range(15):
            Listing.objects.get_or_create(
                title=random.choice(titles),
                host=host_user,
                description="A bright and spacious apartment in the heart of the city.",
                location=random.choice(locations),
                price_per_night=random.randint(100000,600000),
                in_service=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Seedng completed successfully!"))
