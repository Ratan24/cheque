from django import forms
from .models import *
  
class chequeForm(forms.ModelForm):
  
    class Meta:
        model = cheque
        fields = ['bank_name', 'cheque_Main_Img']