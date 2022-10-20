from django.shortcuts import render
from pathlib import Path
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image
from django.conf import settings
from .sources import *


# Create your views here.

def mainView(request):
	template_name = 'mainremove/mainpage.html'
	data = {}
	if request.method == 'POST':
		image = request.FILES['fimage']
		data["image"] = remove_bg(image)
	else:
		pass
	return render(request, template_name, data)


	
