from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.db import connection

# Create your views here.
def upload_pic(request):
    image_url = "https://blog.stylingandroid.com/wp-content/themes/lontano-pro/images/no-image-slide.png"
    if request.method == 'POST' and request.FILES['idol_pic']:
        image = request.FILES['idol_pic']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        idol_name = image.name[:image.name.rfind('.')]
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM info_idol_infoidol WHERE name = %s", [idol_name])
            data = cursor.fetchone()
            if(data):
                info_idol = {
                    'name': data[1],
                    'birthday': data[2],
                    'height': data[3],
                    'v1': data[4],
                    'v2': data[5],
                    'v3': data[6],
                    'list_film': data[7][1:-2]
                }
            else:
                info_idol = None

        return render(request, 'upload_pic/upload.html', {
            'image_url': image_url,
            'info_idol': info_idol,
            'idol_name': idol_name
        })
    return render(request, 'upload_pic/upload.html', {
        'image_url': image_url
    })