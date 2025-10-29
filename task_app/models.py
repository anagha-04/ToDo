from django.db import models

# Create your models here.
from user_app.models import User

class TaskModel(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

    task_name = models.CharField(max_length=20)

    priority = models.Choices("high","low")

    created_date =models.DateTimeField(auto_now_add=True)

    is_completed = models.BooleanField(default=False)