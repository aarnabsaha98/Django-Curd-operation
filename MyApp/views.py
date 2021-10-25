from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
# import from model databse
from .models import Employee
from .form import CreateNewList



def View(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["data"] = Employee.objects.get(id = id)   
    # return render(request, "detail_view.html", context)
    return render(request,'MyApp/detailView.html',context)
def Create(request):
    employee = Employee.objects.all()
    form = CreateNewList(request.POST)
    if form.is_valid():
    # another method  is Cleaned data
        form.save()
        # to clear up the form details 
        return HttpResponseRedirect('/curd')
    else:
        form = CreateNewList()
    return render(request,'MyApp/index.html',{ 'form' : form,'employee': employee})

def delete(request,id):
    if request.method == 'POST':
        sv = Employee.objects.get(pk=id)
        sv.delete()
    return HttpResponseRedirect('/curd')

def update(request,id):
    context = {}
    obj = get_object_or_404(Employee,id = id)
    form = CreateNewList(request.POST or None , instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/curd')
    context['form'] = form
    return render(request,'MyApp/update.html',context)




