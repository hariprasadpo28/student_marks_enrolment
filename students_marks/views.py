from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import marks
from .forms import marks_form
from django.contrib import messages

# Create your views here.

def add_marks(request):
    if request.method == "POST":
        form  = marks_form(request.POST)

        if form.is_valid():
            marks_instance = marks.objects.create(name = request.POST['name'], roll_number = int(request.POST['roll_number']), maths_marks = float(request.POST['maths_marks']), physics_marks = float(request.POST['physics_marks']), chemistry_marks = float(request.POST['chemistry_marks']) )
            marks_instance.save()
            marks_instance.total = float(request.POST['maths_marks']) + float(request.POST['physics_marks']) + float(request.POST['chemistry_marks'])
            marks_instance.percentage = round(marks_instance.total/3 , 2)
            marks_instance.save(update_fields = ['total', 'percentage'])
            #print(marks.objects.all())
            form  = marks_form()
            messages.success(request, f'Details added successfully!')
    else:
        form  = marks_form()

    return render(request, 'add_marks.html', {'form':form})
    #return HttpResponse("Add your Marks here!")

def leader_board(request):
    keyword = ""
    if request.method == "POST":
        
        if request.POST['action'] == "sort":
            qset = marks.objects.all().order_by(request.POST['sort_by'])
            if request.POST['sort_by'][0] == "-":
                order_by = request.POST['sort_by'][1:] + " " + "descending"
            else:
                order_by = request.POST['sort_by']

        else:
            qset = marks.objects.filter(name__icontains = request.POST['search']).order_by("-percentage")
            order_by = "percentage"
            keyword = request.POST['search']

    else:
        qset = marks.objects.all().order_by("-percentage")
        order_by = "percentage"

    return render(request, 'leaderboard.html', {'qset':qset,'order_by':order_by, 'keyword':keyword})
    #return HttpResponse("Leader board will be displayed here!")