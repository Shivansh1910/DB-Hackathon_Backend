from secrets import choice
from unicodedata import decimal
from django.db import models

# Create your models here.

# create a model for the database of user with the following fields
# id, name, email, password, created_at, updated_at, handle, role, dob


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    dob = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Security(models.Model):
    issuer = models.CharField(max_length=200)
    isin = models.CharField(max_length=12)
    cusip = models.CharField(max_length=9)
    bond_type = models.CharField(max_length=20)
    ticker_symbol = models.CharField(max_length=3)
    coupon_rate = models.DecimalField(max_digits=3, decimal_places=2)
    maturity_date = models.DateTimeField()
    face_value = models.DecimalField(max_digits=12, decimal_places=2)
    current_price = models.DecimalField(max_digits=12, decimal_places=2)
    yield_to_maturity = models.DecimalField(max_digits=3, decimal_places=2)
    rating_choices = [
        ("AAA", "AAA"),
        ("AA", "AA"),
        ("A", "A"),
        ("BBB", "BBB"),
        ("BB", "BB"),
        ("B", "B"),
        ("CCC", "CCC"),
        ("CC", "CC"),
        ("C", "C"),
        ("D", "D")
    ]
    rating = models.CharField(max_length=3,choices=rating_choices)
    status_choices = [
    ("Completed" , "Completed"),
    ("Released" , "Released"),
    ("Canceled", "Canceled"),
    ("Project_Abandoned", "Project_Abandoned"),
    ("Defaulted", "efaulted"),
    ("Waiting_for_District_Clearance", "Waiting_for_District_Clearance"),
    ("Category_X_(TBD)", "Category_X_(TBD),"),
    ("Active", "Active"),
    ("B-Permit_in_Deficit", "B-Permit_in_Deficit"),
    ("Bond_Replaced", "Bond_Replaced")
    ]
    status = models.CharField(max_length=100, choices= status_choices)

    def __str__(self):
        return self.isin