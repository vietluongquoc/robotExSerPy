from django.shortcuts import render

def exams(request):
    if request.method == "POST":
        print(request.POST)  # Prints the POSTed data as a QueryDict
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, "exams.html")