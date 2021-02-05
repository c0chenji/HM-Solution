from django import forms
from django.forms import ModelForm
from .models import Camera,Channel
from django.core.exceptions import ValidationError

  
       


class CameraForm(forms.ModelForm):
  class Meta:
    model = Camera
    fields = ['rtsp_url']

class ChannelEditForm(forms.ModelForm):
  class Meta:
    model = Channel
    camera = forms.ModelMultipleChoiceField(queryset=Camera.objects.all())
    fields = ['username','password','IP','portNum','cameraNum',
                  'description','enabled','camera','coordinates','names','directions']

  def clean(self):
    cleaned_data = super(ChannelEditForm,self).clean()
    return cleaned_data




class ChannelCreateForm(forms.ModelForm):

 #username = forms.CharField(error_messages={'required': _('No user name has been entered')}, max_length=128) 
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = Channel
    camera = forms.ModelMultipleChoiceField(queryset=Camera.objects.all())
    fields = ['username','password','IP','portNum','cameraNum',
                  'description','enabled','camera']
    widget = {
               'password' : forms.PasswordInput(),
             }

  
  def clean(self):
    cleaned_data = super(ChannelCreateForm,self).clean()
    return cleaned_data


class ListForm(forms.ModelForm):
  class Meta:
    model = Channel
    fields = ['IP','description','enabled']


class ChannelUSBForm(forms.ModelForm):
  #description = forms.CharField(max_length=255)
  #enabled = forms.BooleanField()

  class Meta:
    model = Channel
    fields = ['description','enabled']

  
  def clean(self):
    cleaned_data = super(ChannelUSBForm,self).clean()
    return cleaned_data



class USBchannelEditForm(forms.ModelForm):

  class Meta:
    model = Channel
    fields = ['description','enabled']

  def clean(self):
    cleaned_data = super(USBchannelEditForm,self).clean()
    return cleaned_data

class ZoneEdit(forms.ModelForm):

  class Meta:
    model = Channel
    fields = ['coordinates']
    

  def clean(self):
    cleaned_data = super(ZoneEdit,self).clean()
    return cleaned_data

        
