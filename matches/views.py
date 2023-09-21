from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def createMatch(request):
    if not request.session.test_cookie_worked() or request. request.session['user'] is None:
        return Response(status=403)
    return Response("Your login")
