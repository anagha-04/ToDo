from django.db import models

# Create your models here.
from user_app.models import User

class TaskModel(models.Model):

    priority_choices = [('high','High'),
                        ('low','Low')]
    

    priority = models.CharField(max_length=30, choices=priority_choices)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    task_name = models.CharField(max_length=60)

    created_date =models.DateTimeField(auto_now_add=True)

    is_completed = models.BooleanField(default=False)