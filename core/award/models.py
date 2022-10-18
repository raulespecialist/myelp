from django.db import models

# Model for business
class Business(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    stars = models.FloatField()
    review_count = models.IntegerField()
    categories = models.TextField(null=True)

    def __str__(self):
        return self.name

# Model for Users
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    yelping_since = models.DateTimeField()

    def __str__(self):
        return self.name

# Model for Reviews
class Review(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    stars = models.FloatField()
    useful = models.IntegerField()
    funny = models.IntegerField()
    cool = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user.name