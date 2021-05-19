from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from .models import Credits
import json

# Create your views here.

@api_view(('GET',))
@permission_classes((AllowAny, ))
@renderer_classes([JSONRenderer])
def credits(request, format=None):
    result = filter(lambda item:item['amount']>=50000,Credits.objects.values(
        'id','amount','approved','user__first_name','user__last_name','user__profile__indicator'
    ).all())
    return Response(result)


@api_view(('POST',))
@permission_classes((AllowAny, ))
@renderer_classes([JSONRenderer])
def approve_credits(request, format=None):
    result = filter(lambda item:item['amount']>=50000,Credits.objects.values(
        'id','amount','approved','user__first_name','user__last_name','user__profile__indicator'
    ).all())
    _id = json.loads(request.body.decode('utf-8'))
    item = Credits.objects.get(pk=_id)
    item.approved = not item.approved
    return Response({'id':item.pk})