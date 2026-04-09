from django.shortcuts import render

def page_not_found_error(request,exception):
    return render(request,'404.html',status=404)

def internal_server_error(request):
    return render(request,'500.html',status=500)