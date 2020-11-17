from django.db import models

class Traffic(models.Model):
    week= models.CharField(max_length=10)
    speed=models.IntegerField(max_length=5)
    
    def __str__(self):
        return self.week