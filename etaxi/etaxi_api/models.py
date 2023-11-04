from django.db import models

class City(models.Model):
    city = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.city
    
class Office(models.Model):
    city = models.ForeignKey(City, related_name='offices', on_delete=models.CASCADE)
    address = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.address

class Team(models.Model):
    city = models.ForeignKey(City, related_name='team', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    quote = models.TextField()

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    city = models.ForeignKey(City, related_name='cars', on_delete=models.CASCADE)
    model = models.CharField(max_length=64)
    transmission = models.CharField(max_length=64)
    engine_capacity = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.model
    

class Feedback(models.Model):
    city = models.ForeignKey(City, related_name='feedback', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self) -> str:
        return self.name
