from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from wapp import readDocx
import docx


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            # search word & word to be changed
            search = request.POST.get('change_word')
            change_word = request.POST.get('to')

            # file handling
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            f = os.path.join(settings.MEDIA_ROOT, filename)

            # reading the document
            # print(readDocx.getText(f))
            # print(readDocx.replace_string(f))

            doc = docx.Document(f)
            for p in doc.paragraphs:
                if search in p.text:
                    inline = p.runs
                    # loop added to work with runs (strings with same
                    # style)
                    for i in range(len(inline)):
                        if search in inline[i].text:
                            text = inline[i].text.replace(
                                search, change_word)
                            inline[i].text = text
                    print(p.text)

            doc.save(os.path.join(settings.MEDIA_ROOT, f))

            uploaded_file_url = fs.url(filename)

            return render(request, 'wapp/upload.html', {'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadFileForm()
    return render(request, 'wapp/upload.html', {'form': form})
