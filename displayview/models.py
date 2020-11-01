from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    headline   = models.CharField(max_length=120)
    content = models.TextField()
    reporter= models.CharField(max_length=50,default="vishnu")
    pub_date=models.DateField(default=datetime.now())
    


