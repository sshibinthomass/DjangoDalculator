from django.shortcuts import render

# Create your views here.
def calc(num1,num2,opr):
    if opr=="add":
        return num1+num2
    elif opr=="sub":
        return num1-num2
    elif opr=="mul":
        return num1*num2
    elif opr=="divide":
        return num1/num2
def home(request):
    return render(request,'home.html')
    
def inputs(request):
    return render(request,'inputs.html')

def result(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    opr=request.POST["operation"]
    val=calc(num1,num2,opr)
    return render(request,'result.html',{'val':val})

