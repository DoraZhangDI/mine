# -*- coding: utf-8 -*-
"""
    30/08/2017,23:33,2017
    BY DoraZhang
"""
from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from json import loads, dumps
# Create your views here.

# booklist
def booklist(request):
	if request.method == 'POST':
		input_name = request.POST['username']
		input_pwd = request.POST['password']
		x = models.User.objects.filter(uname=input_name, password=input_pwd)
		if len(x) == 1:
			return redirect('../univar/')
		else:
			return render(request, "signin.html", {"msg": "用户名密码错误"})
	return render(request, 'booklist.html')

# modify
def modify(request):
	if request.method == 'POST':
		input_name = request.POST['username']
		input_pwd = request.POST['password']
		x = models.User.objects.filter(uname=input_name, password=input_pwd)
		if len(x) == 1:
			return redirect('../univar/')
		else:
			return render(request, "signin.html", {"msg": "用户名密码错误"})
	return render(request, 'modify.html')

# add a book
def add(request):
	if request.method == 'POST':
		input_name = request.POST['username']
		input_pwd = request.POST['password']
		x = models.User.objects.filter(uname=input_name, password=input_pwd)
		if len(x) == 1:
			return redirect('../univar/')
		else:
			return render(request, "signin.html", {"msg": "用户名密码错误"})
	return render(request, 'add.html')

# signin
def signin(request):
	if request.method == 'POST':
		input_name = request.POST['username']
		input_pwd = request.POST['password']
		x = models.User.objects.filter(uname=input_name, password=input_pwd)
		if len(x) == 1:
			return redirect('../univar/')
		else:
			return render(request, "signin.html", {"msg": "用户名密码错误"})
	return render(request, 'signin.html')


# signin ajax
def login(request):
	if request.method == 'POST':
		input_name = request.POST['username']
		input_pwd = request.POST['password']
		x = models.User.objects.filter(uname=input_name, password=input_pwd)
		if len(x) == 1:
			return HttpResponse(dumps({'data': 1}), content_type='application/json')
		else:
			return HttpResponse(dumps({'data': 0}), content_type='application/json')
	return HttpResponse(dumps({'data': -1}), content_type='application/json')
