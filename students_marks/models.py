from django.db import models

# Create your models here.

class marks(models.Model):
    roll_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    maths_marks = models.FloatField(null=True, blank=True)
    physics_marks = models.FloatField(null=True, blank=True)
    chemistry_marks = models.FloatField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)