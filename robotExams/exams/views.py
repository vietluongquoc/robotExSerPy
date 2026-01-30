from django.shortcuts import render

def exams(request):
    return render(request, 'exams.html')