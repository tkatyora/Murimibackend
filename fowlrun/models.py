from django.db import models

# Create your models here.
class FowlRunConditions(models.Model):
    temperature = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    date_recorded = models.DateTimeField( auto_now_add=True ,null=True)
    date_update = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        ordering = ['date_update']
        
    # def __str__(self):
    #     return self
    

    

    

