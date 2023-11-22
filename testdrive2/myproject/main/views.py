from django.shortcuts import render, redirect
from .models import Drive
from .forms import DriveForm


def index(request):
    tasks = Drive.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def Testdrive(request):
    error = ""
    if request.method == 'POST':
        form = DriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = DriveForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/Testdrive.html', context)
