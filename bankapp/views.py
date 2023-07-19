from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as userLogin,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm




def home(request):
    return render(request, 'home.html')

def login(request):
    if(request.method =='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            userLogin(request,user)
            return redirect('/entry')
        else:
            messages.info(request,'wrong credentials')

    context={}
    return render (request,"login.html")


def registerPage(request):
    print("running register",request.method)
    form=CreateUserForm()
    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            print("issss validdd")
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'created user'+user)
            return redirect('/login')
        else:
            print("not valid bro")

    context={'form':form}
    return render(request,'register.html',context)

def logOutUser(request):
    logout(request)
    return redirect('/login')

def entry(request):
    return render(request,'entry.html')

# def form(request):
#     return render(request,'form.html')

def submit(request):
    return render(request, 'submit.html')

# def form(request):
#     selected_district = None  # Initialize selected_district to None
#     branch_options = []  # Initialize branch_options as an empty list
    
#     if request.method == 'POST':
#         selected_district = request.POST.get('district')
#         # Populate branch_options based on the selected district
#         if selected_district == 'Ernakulam':
#             branch_options = ['Aluva', 'Edapally', 'Sub Area 1', 'Sub Area 2']
#         elif selected_district == 'Thrissur':
#             branch_options = ['Sub Area 3', 'Sub Area 4', 'Sub Area 5']

#     return render(request, 'form.html', {'selected_district': selected_district, 'branch_options': branch_options})

def form(request):
    return render(request, 'form.html')



