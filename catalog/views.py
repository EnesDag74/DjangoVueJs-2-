from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def public(request):
		return HttpResponse("you dont need to be authenticated to see this")

@api_view(['GET'])
def private(request):
		return HttpResponse("You should not to see this message if not authenticated")