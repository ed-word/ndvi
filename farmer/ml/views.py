from django.shortcuts import render

# Create your views here.
def dash(request):
    var_dict = {}
    return render(request, 'index1.html', var_dict)