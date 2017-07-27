from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload_pic(request):
    if request.method == 'POST' and request.FILES['idol_pic']:
        image = request.FILES['idol_pic']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)
        return render(request, 'upload_pic/upload.html', {
            'uploaded_image_url': image_url
        })
    return render(request, 'upload_pic/upload.html')