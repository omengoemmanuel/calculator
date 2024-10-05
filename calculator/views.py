from django.shortcuts import render, HttpResponse, redirect
from django.urls import path

from calculator.models import fun
import math


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
        elif operands == 'product':
            result = float(fno) * float(lno)
            return render(request, 'calculate.html', {'result': result})
        elif operands == "divide":
            result = float(fno) / float(lno)
            return render(request, 'calculate.html', {'result': result})
        elif operands == 'cos':
            result = math.cos(float(fno))
            return render(request, 'calculate.html', {'result': result})

        math1 = fun(fno=fno, lno=lno, operands=operands)
        math1.save()
        return redirect('cal1')
    return redirect('cal1')
