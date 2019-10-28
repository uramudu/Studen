from django.shortcuts import render
from .models import Employee
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
def index(request):
    return render(request,"index.html")


def send(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    Employee(idno=idno,name=name,salary=salary).save()
    return render(request,"home.html",{"message":"Successfull Saved"})



class Update(UpdateView):
    model = Employee
    template_name = "update.html"
    fields = ["idno","name","salary"]
    success_url = "/home/"


class Delete(DeleteView):
    model = Employee
    template_name = "Delete.html"
    fields = ["idno", "name", "salary"]
    success_url = "/home/"
