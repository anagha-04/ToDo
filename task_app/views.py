from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from task_app.forms import TaskForm

from task_app.models import TaskModel

class AddTaskView(View):

    def get(self,request):

        form = TaskForm()

        return render(request,"add_task.html",{"form":form})
