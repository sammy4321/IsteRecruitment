from django.shortcuts import render
from iste_form.forms import Infoform
from iste_form.models import Info

# Create your views here.
def index(request):
	return render(request,'iste_form/index.html')
def data(request):
	all_registered = Info.objects.all()
	return render(request,'iste_form/data.html',{'all_registered':all_registered})
def savedata(request):
    if request.method == 'POST':  # if the form has been filled

        form = Infoform(request.POST)

          # All the data is valid
        Name = request.POST.get('exampleInputEmail1', '')
        Number = request.POST.get('exampleInputPassword1', '')
        # creating an user object containing all the data
        user_obj = Info(Name=Name, Number=Number)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'iste_form/index.html', {'user_obj': user_obj,'is_registered':True }) 

