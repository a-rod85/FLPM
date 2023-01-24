from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

status_choices = (
    ("pending", "pending"),
    ("confirmed", "confirmed"),
    ("rejected", "rejected")
    ("expired", "expired"),
)


time_choices = (
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
)


guest_choices = (
    (1, "1 person"),
    (2, "2 person"),
    (3, "3 person"),
    (4, "4 person"),
    (5, "5 person"),
    (6, "6 person"),
)


class Customer(models.Model):

    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=260, default="")
    phone_number = PhoneNumberField(null=True)

    def __str__(self):
        return self.full_name


class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=15, default="New Table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservations(models.Model):

    reservations_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer", null=True
        )
    no_of_guests = models.IntegerField(choices=guests_chices, default=1)
    requested_data = models.DateField()
    requested_time = models.CharField(
        max_length=10, choices=time_choices, default="17:00"
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table_booked", null=True
        )
    status = models.CharField(max_length=10, choices=status_choices, default="pending")

    def __str__(self):
        return str(self.reservation_id)
