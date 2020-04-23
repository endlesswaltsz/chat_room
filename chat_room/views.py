from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def chat(request):
    # if request.method == 'get':
    context = {}
    return render(request, 'chat_room/index.html', context)
    