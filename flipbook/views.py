# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from flipbook.models import PdfFlipbook
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def flipbook(request):
    documents = PdfFlipbook.objects.all()
    print(documents)

    return render(
        request,
        'index.html',
        {'documents': documents}
    )
