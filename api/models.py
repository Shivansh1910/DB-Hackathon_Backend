from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DBUser(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserBook(models.Model):
    user = models.ForeignKey(DBUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return self.user.name + " - " + self.book.name


class CounterParty(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Security(models.Model):
    ISIN = models.CharField(max_length=200)
    CUSIP = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    coupon = models.CharField(max_length=200)
    maturityDate = models.DateField()
    faceValue = models.CharField(max_length=200)
    typeOfSecurity = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.ISIN


class Trade(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    counterparty = models.ForeignKey(CounterParty, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    options = (
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
    )
    buy_sell = models.CharField(max_length=200, choices=options, default='Buy')
    tradeDate = models.DateField()
    settlementDate = models.DateField()
    isReported = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name + " - " + self.counterparty.name + " - " + self.security.ISIN


class Notification(models.Model):
    user = models.ForeignKey(DBUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    isRead = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if (self.isRead):
            return self.user.name + " - " + self.message + " - Read"
        else:
            return self.user.name + " - " + self.message + " - Unread"


class Report(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    authority = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trade.book.name + " - " + self.authority + " - " + self.trade.security.ISIN


class Watchlist(models.Model):
    user = models.ForeignKey(DBUser, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'trade')

    def __str__(self):
        return self.user.name + " - " + self.trade.security.ISIN
