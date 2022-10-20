from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image
from django.conf import settings
import os
import glob



def remove_bg(image):
	files = glob.glob(f'.{settings.MEDIA_URL}inputimage/*')
	for f in files:
		os.remove(f)
	media_url = FileSystemStorage()
	file = media_url.save("inputimage/img.png", image)
	file_url = "."+media_url.url(file)
	input_image = Image.open(file_url)
	output_image = remove(input_image)
	output_path = f".{settings.MEDIA_URL}inputimage/out_img.png"
	output_image.save(output_path)
	return output_path
