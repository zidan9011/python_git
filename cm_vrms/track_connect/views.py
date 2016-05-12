# encoding: utf-8
import os
from django.http import HttpResponse,HttpResponseRedirect  
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from bootstrap_toolkit.widgets import BootstrapUneditableInput 
from django.http import JsonResponse
from .models import Workbooks
import simplejson as json
from django.http import HttpResponse
'''
def index(request):

    app_action = request.POST.get('app_action')
    posted_data = request.POST.get('json_data')

    if posted_data is not None and app_action == 'save':
        ...

    elif app_action == 'get_sheets':
        ...
  
    elif app_action == 'list':

'''
def connect_table(request):
 
    c = Context({'STATIC_URL': '/static/'})
   
    out_path = "connect_table"
    return render_to_response(out_path+'.html',context_instance=c)



def conn_table(request):
 
    c = Context({'STATIC_URL': '/static/'})
   
    out_path = "conn_table"
    return render_to_response(out_path+'.html',context_instance=c)