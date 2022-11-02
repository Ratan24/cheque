from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class cheque(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True , blank = True)
    bank_name = models.CharField(max_length=50)
    cheque_Main_Img = models.ImageField(upload_to='images/')


