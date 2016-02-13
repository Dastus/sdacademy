#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import math

def quadratic_results(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    a_err = ''
    b_err = ''
    c_err = ''
    discriminant = ''
    final_res = ''
    a_err = validator_first(a, a_err)
    b_err = validator_other(b, b_err)
    c_err = validator_other(c, c_err)
    if  a_err == '' and b_err == '' and c_err == '':
        a = int(a)
        b = int(b)
        c = int(c)
        d = b * b - 4 * a * c
        discriminant = "Дискриминант: %s" %d
        if d < 0:
            final_res = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        else:
            x1 = (-b + math.pow(d, 0.5))/(2 * a)
            x2 = (-b - math.pow(d, 0.5))/(2 * a)
            final_res = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1, x2)
            if d == 0:
                final_res = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x1
        a = str(a) + a_err
        b = str(b) + b_err
        c = str(c) + c_err

    return  render(request, 'results.html', {'a': a, 'b': b, 'c': c, 'discriminant': discriminant,
                                             'final_res': final_res, 'a_err': a_err, 'b_err': b_err, 'c_err': c_err})

def validator_first(val, val_err):
    if val != '':
        try:
            val = int(val)
            if val == 0:
                val_err = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
        except ValueError:
            val_err = "коэффициент не целое число"
    else:
        val_err = "коэффициент не определен"
    return val_err

def validator_other(val, val_err):
    if val != '':
        try:
            val = int(val)
        except ValueError:
            val_err = "коэффициент не целое число"
    else:
        val_err = "коэффициент не определен"
    return val_err