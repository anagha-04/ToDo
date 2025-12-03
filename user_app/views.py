from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

from user_app.forms import UserregisterForm

from user_app.models import User

from django.contrib.auth import authenticate,login,logout

from task_app.models import TaskModel


# view: registration view

# methods required: get and post

class RegisterView(View):

    def get(self,request):

        form =UserregisterForm()

        return render(request,"sign_up.html",{"form":form})
    
    def post(self,request):

        print(request.POST)

        username = request.POST.get('username')

        first_name = request.POST.get('first_name')

        last_name = request.POST.get('last_name')

        password = request.POST.get('password')

        email = request.POST.get('email')

        User.objects.create_user(username = username,
                                 first_name = first_name,
                                 last_name = last_name,
                                 password = password,
                                 email = email)
        
        form = UserregisterForm()

        return render(request,'login.html',{'form':form})
    
    #loginView

    #methods used get and post


class LoginView(View):

    def get(self,request):

        return render(request,"login.html")
    

    def post(self,request):

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:

            login(request,user)

            return redirect("home")
        
        return render(request,"login.html")
    

#view: logout
#method: get

class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("home")
    


    

class BaseView(View):

    def get(self,request):
       
       if request.user.is_authenticated:

          task = TaskModel.objects.filter(user = request.user) #object

        #collection of objects (object1,object2,object3)
 

          return render(request,"home.html",{"task":task})
       
       return render(request,"home.html")