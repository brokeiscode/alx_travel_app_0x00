from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=150)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    in_service = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'listings'

    def __str__(self):
        return f"{self.title} - {self.price_per_night}"


# TextChoice Class
class BookingStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    CANCELLED = 'cancelled', 'Cancelled'
    CONFIRMED = 'confirmed', 'Confirmed'
    COMPLETED = 'completed', 'Completed'


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'bookings'

    def __str__(self):
        return f"{self.guest.first_name}: {self.listing.title} - {self.status}"


class RatingChoices(models.IntegerChoices):
    ONE_STAR = 1, '1 Star - Terrible'
    TWO_STARS = 2, '2 Stars - Poor'
    THREE_STARS = 3, '3 Stars - Average'
    FOUR_STARS = 4, '4 Stars - Good'
    FIVE_STARS = 5, '5 Stars - Excellent'


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_reviews')
    rating = models.IntegerField(
        choices=RatingChoices.choices,
        default=RatingChoices.FIVE_STARS
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'reviews'

    def __str__(self):
        return f"{self.listing.title} - ({self.rating}/5)"
