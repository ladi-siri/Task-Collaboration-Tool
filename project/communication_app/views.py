from django.shortcuts import render, redirect
from.models import Message
from.forms import MessageForm

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'essage_list.html', {'messages': messages})

def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'essage_detail.html', {'message': message})

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'end_message.html', {'form': form})