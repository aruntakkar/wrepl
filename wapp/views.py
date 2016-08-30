from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES	)
        if form.is_valid():
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'wapp/upload.html', {'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadFileForm()
    return render(request, 'wapp/upload.html', {'form': form})
