from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django import forms
from blog.models import Tiltle

class TiltleForm(forms.Form):
    tiltlename = forms.CharField(label='文章名',max_length=100)
    tiltlecontent = forms.CharField(label='文章内容',max_length=500)

def add(req):
    if req.method == 'POST':
        tf = TiltleForm(req.POST)
        # print(tf.data)
        if tf.is_valid():
            print(tf.data)
            #获得表单数据
            tiltlename = tf.cleaned_data['tiltlename']
            tiltlecontent = tf.cleaned_data['tiltlecontent']
            #添加到数据库
            Tiltle.objects.create(tiltlename= tiltlename,tiltlecontent=tiltlecontent)
            return HttpResponseRedirect('/blog')
    else:
        tf = TiltleForm()
    return render(req,'blog.html',{'tf':tf})


def showTitle(req):

    titlecontents=Tiltle.objects.all()
    # print(titlecontents)
    return render(req, 'showTitle.html', {'tc': titlecontents})

def delete(req):
    pass