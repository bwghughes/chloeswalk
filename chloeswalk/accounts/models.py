from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    contribution = models.ForeignKey("Contribution", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.username
    

class Contribution(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contributions")
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.date} - {self.description}"