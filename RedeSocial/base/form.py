from django.forms import ModelForm
from .models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class MensageForm(ModelForm):
    class Meta:
        model = Mensage
        fields = ["body"]