from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PredictionModel(models.Model):
    prediction = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    result_ID = models.IntegerField(primary_key=True, unique=True)

    def __str__(self):
        return self.prediction
