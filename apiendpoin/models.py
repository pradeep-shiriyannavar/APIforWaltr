from django.db import models

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()


    def __str__(self) -> str:
        return f"{self.eid}---{self.ename}"