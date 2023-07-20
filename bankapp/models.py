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
        
class Districts(models.Model):
     Pid=models.IntegerField(primary_key=True)
     Pname=models.CharField(max_length=100)
     class Meta:
          db_table="districtTable"

class Branches(models.Model):
     Itemid=models.IntegerField(primary_key=True)
     Itemname=models.CharField(max_length=100)
     Pid=models.IntegerField()
     class Meta:
          db_table="itemsTable"