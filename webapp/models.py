from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    email = models.EmailField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname


