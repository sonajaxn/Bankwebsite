from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    def __str__(self):
        return self.username

class Account(models.Model):
        name=models.CharField(max_length=250)
        Account_type=models.CharField(max_length=250)
        def __str__(self):
            return self.name