from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortLink,baselink
from .serializers import ShortLinkSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django_ratelimit.decorators import ratelimit
# need redis

class ShortLinkCreate(APIView):

    def post(self, request):
        serializer = ShortLinkSerializer(data=request.data)
        if serializer.is_valid():
            short_link = serializer.save()
            return Response({'short_url': short_link.short_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortLinkRetrieve(APIView):
   
    def post(self, request):
        short_url = request.data.get('short_url')
        short_link = get_object_or_404(ShortLink, short_url=short_url)
        return Response({'original_url': short_link.original_url}, status=status.HTTP_200_OK)


class RedirectShortLink(APIView):

    def get(self, request, short_url):
        short_link = get_object_or_404(ShortLink, short_url=baselink+short_url)
        return HttpResponseRedirect(short_link.original_url)
    
def home(request):
     return render(request, 'index.html')