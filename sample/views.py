from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import MyForm
from .models import Employees


# Create your views here.
def index(request):
    return HttpResponse("Welcome")


class Home(View):

    def handle_uploaded_file(f):
        with open('geeks / upload/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def get(self, request):
        form = MyForm()
        objects = Employees.objects.all()
        context = {'form': form, 'objects': objects}
        return render(request, "sample/home.html", context)

    def post(self, request):
        form = MyForm(request.POST, request.FILES)
        objects = Employees.objects.all()
        if form.is_valid():
            form.save()
            return redirect('sample:home')
        context = {'form': form, 'objects': objects}
        return render(request, "sample/home.html", context)
