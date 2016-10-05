from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    # home page for learning learning_log
    return render(request, 'learning_logs/index.html')

def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set_order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(requests, 'learninig_logs/topic.html', context)
