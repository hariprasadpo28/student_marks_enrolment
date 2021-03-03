from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import marks
from .forms import marks_form

# Create your views here.

def add_marks(request):
    if request.method == "POST":
        form  = marks_form(request.POST)

        if form.is_valid():
            redirect('add_marks')
    else:
        form  = marks_form()

    return render(request, 'add_marks.html', {'form':form})
    #return HttpResponse("Add your Marks here!")

def leader_board(request):
    return HttpResponse("Leader board will be displayed here!")