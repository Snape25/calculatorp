from django.shortcuts import render,redirect

# Create your views here.
from .forms import StudentForm




 
#Handles requests
def result(request):                                     
            return render(request,'calc/result.html')




 #Handles the form request and index view
def index(request):                    
    if request.method == "POST":  
            a = request.POST.get('height')
            b = request.POST.get('weight')
            c= int(a)*int(b)
            
            return  render(request,'calc/result.html',{'c':c})  
        
    else:  
        form = StudentForm()  
    return render(request,'calc/index.html',{'form':form})  


    