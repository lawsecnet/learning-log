from django.shortcuts import render

# Create your views here.

def index(request):
    # home page for learning learning_log
    return render(request, 'learning_logs/index.html')
