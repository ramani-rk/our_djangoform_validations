from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)
    email=models.EmailField(default='hai@gmail.com')
    confirmemail=models.EmailField(default='hai@gmail.com')

    def __str__(self):
        return self.Sname

class Webpage(models.Model):
    Sname=models.ForeignKey(School,on_delete=models.CASCADE)
    Scont=models.IntegerField()
    Sadd=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname