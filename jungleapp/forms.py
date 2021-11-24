from django import forms
from django.contrib.flatpages.models import FlatPage
from django.db.models import fields
from tinymce.widgets import TinyMCE
from jungleapp.models import comment, commentcrag, commentsector, commentroute, post, category


class CreatePost(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = post
        fields = '__all__'

class CreateCat(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '4',
    }))
    class Meta:
        model = comment
        fields = ('content',)


class CommentCragForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '4',
    }))
    class Meta:
        model = commentcrag
        fields = ('content',)


class CommentSectorForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '4',
    }))
    class Meta:
        model = commentsector
        fields = ('content',)


class CommentRouteForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '4',
    }))
    class Meta:
        model = commentroute
        fields = ('content',)