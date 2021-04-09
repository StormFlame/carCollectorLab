from django.forms import ModelForm
from .models import Driven

class DrivenForm(ModelForm):
  class Meta:
    model = Driven
    fields = ['date', 'day_time', 'miles']