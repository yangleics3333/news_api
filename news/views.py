from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from news.models import AnalysisCommonNews
from news.serializers import NewsSerializers


def index(request):
    return HttpResponse('index')


class NewsInfoViews(GenericAPIView):
    queryset = AnalysisCommonNews.objects.all()

    def get(self, request, nid=None):
        if nid is None:
            return self.find_time(request)
        else:
            return self.find_news_id(request, nid)

    def find_news_id(self, request, nid):
        return Response(data=NewsSerializers(instance=self.queryset.get(news_id=nid)).data)

    def find_time(self, request):
        return Response(data=NewsSerializers(instance=self.queryset.filter(news_time__gt='2021-02-08 13:27:00').order_by('-news_time')[:20], many=True).data)


class NewsAddViews(GenericAPIView):
    serializer_class = NewsSerializers

    def post(self, request):
        data = NewsSerializers(data=request.data)
        if data.is_valid():
            print('True')
            print(data.validated_data)
            data.save()
            return Response({'code': 1, 'msg': 'succeed'})
        else:
            return Response({'code': 0, 'msg': data.errors})
