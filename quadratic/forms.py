#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label='коэффициент a')
    b = forms.FloatField(label='коэффициент b')
    c = forms.FloatField(label='коэффициент c')