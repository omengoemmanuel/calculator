from django.shortcuts import render, HttpResponse, redirect
from django.urls import path

from calculator.models import fun


# Create your views here.

def cal1(request):
    return render(request, 'calculate.html')


def function(request):
    if request.method == "POST":
        fno = request.POST.get('fno')
        lno = request.POST.get('lno')
        operands = request.POST.get('operands')

        if operands == "add":
            result = float(fno) + float(lno)
            return render(request, 'calculate.html', {'result': result})
        elif operands == "subtract":
            result = float(fno) - float(lno)
            return render(request, 'calculate.html', {'result': result})

        math = fun(fno=fno, lno=lno, operands=operands)
        math.save()
        return redirect('cal1')
    return redirect('cal1')
