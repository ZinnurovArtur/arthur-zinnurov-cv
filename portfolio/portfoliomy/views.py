from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
import mimetypes

def portfolio_index(request):
    return render(request, 'bootstrap/index.html',{})

def download_file(request):
    fl_path = '/files/ZinnurovArthur.pdf'
    filename = 'ZinnurovArthur.pdf'
    fl = open(fl_path,'r')
    mime_type,_ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl,content_type=mime_type)
    response['Content-Disposition'] = "attachement; filename=%s" % filename
    return response
