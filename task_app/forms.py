from django import forms

from task_app.models import TaskModel

class TaskForm(forms.ModelForm):
        
    class Meta:

        model = TaskModel
                
        fields =["task_name","priority", "is_completed"]