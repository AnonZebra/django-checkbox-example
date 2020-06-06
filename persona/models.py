from django.db import models


class Characteristic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Persona(models.Model):
    name = models.CharField(max_length=50)
    characteristics = models.ManyToManyField(Characteristic)

    def __str__(self):
        return self.name
