from django import forms
from .models import *

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class OrdersForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ('author', 'phone',)