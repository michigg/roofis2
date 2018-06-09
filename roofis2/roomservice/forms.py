from django.db import models
from .models import Favorite
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = Favorite
        fields = ['room', 'staff']
