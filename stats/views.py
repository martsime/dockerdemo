from django.shortcuts import render
from .models import Case

def index(request):
	context = {
		'cases': Case.objects.all()
	}
	return render(request, 'stats/index.html', context)
