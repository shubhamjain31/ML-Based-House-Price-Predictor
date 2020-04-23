from django.shortcuts import render
from django.http import HttpResponse
from HPP import House_Price_Model

# Create your views here.
#1 bhk -> bedroom, hall, and a kitchen

def index(request):
	if request.method == 'POST':
		total_sqft = float(request.POST.get('area'))
		bhk = int(request.POST.get('bhk'))
		bath = int(request.POST.get('bath'))
		location = request.POST.get('loc')
		params = House_Price_Model.predict_price(location,total_sqft,bhk,bath)
		return render (request,'index.html',{'data':params,'unit':'lakh'})
	return render (request,'index.html')