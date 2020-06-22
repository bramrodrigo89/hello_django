from django.shortcuts import render

# Create your views here.

def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
    HttpResponse('<h1>Hello!</h1><p>This is information</p>')