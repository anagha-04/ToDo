from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View,UpdateView

from task_app.forms import TaskForm

from task_app.models import TaskModel

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

#add task view

class AddTaskView(View):

    def get(self,request):

        form = TaskForm()

        return render(request,"add_task.html",{"form":form})
    
    def post(self,request):

        print(request.POST)

        form = TaskForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            task = form.save(commit = False)

            task.user = request.user

            task.save()

        return render(request,"add_task.html",{"form":form})
    
class TaskList(View):

    def get(self,request):

        task = TaskModel.objects.filter(user= request.user)

        return render(request,"task_list.html",{"task":task})
    
class TaskUpdate(UpdateView):

    model = TaskModel

    form_class = TaskForm

    template_name = "task_update.html"

    success_url = reverse_lazy("home")

    def get_queryset(self):
        
        return  TaskModel.objects.filter(user = self.request.user)


class TaskDelete(View):

    def get (self,request,**kwargs):

        id = kwargs.get("pk")

        task= get_object_or_404(TaskModel, id = id,user = request.user)

        task.delete()

        return redirect("home")
