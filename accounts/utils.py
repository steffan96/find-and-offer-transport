import os
import secrets
from pathlib import Path
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent.parent

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + f_ext
    picture_path = os.path.join(BASE_DIR, 'media/profile_pics', picture_name)
    small_picture_path = os.path.join(BASE_DIR, 'media/small_profile_pics', picture_name)
    
    small_output_size = (70,61)
    i = Image.open(form_picture)
    i.thumbnail(small_output_size)
    i.save(small_picture_path)

    output_size = (125,111)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_name
