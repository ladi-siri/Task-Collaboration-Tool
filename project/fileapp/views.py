from django.shortcuts import render, redirect
from.models import File
from.forms import FileForm

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

def file_detail(request, pk):
    file = File.objects.get(pk=pk)
    return render(request, 'file_detail.html', {'file': file})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})