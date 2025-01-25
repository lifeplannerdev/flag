from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=250)
    mail = models.EmailField()
    contact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name