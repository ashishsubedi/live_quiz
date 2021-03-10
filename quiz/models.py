from django.db import models


class Problem(models.Model):
    question = models.TextField()
    points = models.IntegerField(default = 1)

class Option(models.Model):
    option = models.CharField(max_length=255)
    is_answer = models.BooleanField()
    problem = models.ForeignKey(Problem,related_name='option',on_delete=models.CASCADE,blank=True,null=True)


    