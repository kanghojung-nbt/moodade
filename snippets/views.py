from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet, Stock, Keyboard
from snippets.serializers import SnippetSerializer, StockSerializer, ButtonSerializer
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from mood.models import Mood

from jsonview.decorators import json_view
from jsonview.decorators import JSON
from django import http


@json_view(content_type='application/json; charset=utf-8')
def my_view(request):
    return {
        'type': 'buttons',
        'buttons': ["기분 알아보기"]
    }

# Lists all stocks or create a new one


class FriendView(APIView):
    def post(self, request):
        content = {
            'message': "SUCCESS"
        }
        return Response(content, status=status.HTTP_200_OK, content_type='application/json; charset=utf-8')

    def delete(self, request):
        content = {'message': "SUCCESS"}
        return Response(content, status=status.HTTP_200_OK, content_type='application/json; charset=utf-8')


def makeMood(msg):  # 카카오톡으로 받아온 문자열을 스페이스를 기준으로 스플릿 하고 그 단어들이 존재하는지
    list = msg.split(' ')
    print(list)
    mood = {'angry': 0, 'surprise': 0, 'boring': 0, 'happy': 0, 'sad': 0, 'disgust': 0, 'sadness': 0, 'interesting': 0}
    mymood = Mood.objects.filter(mood_Verb__in=list)  # 파싱한 문구를 대상으로 나의 기분을 DB에서 찾아보자.

    if (mymood.__len__() == 0):
        return 0

    for i in mymood:
        x = i.emotion
        mood[x] = mood[x] + i.mood_Amount
    myemotion = max(mood, key=mood.get)  # 현재 최대값 즉 나의 기분

    amount = mymood.filter(emotion=myemotion).order_by('mood_Amount')
    mymin = amount.first().mood_Amount
    mymax = amount.last().mood_Amount
    return {'min': mymin, 'max': mymax, 'category': myemotion}


class MessageView(APIView):
    def post(self, request):
        mydata = request.data['content']
        content = {}

        if mydata == '기분 알아보기':
            content = {
                "message": {
                    "text":   " 당신의 기분을 단어별로 띄어서 나타내 주세요 ex) 화남 기쁨 분노"
                }
            }
        else:
            result = makeMood(mydata)
            if result != 0:
                content = {
                    "message": {
                        "text": "당신의 오늘 감정은 " + result["category"] + " 하군요. ",
                        "message_button": {
                            "label": "반갑습니다.",
                            "url": "http://mymood.pythonanywhere.com/"
                        },
                        "keyboard": {
                            "type": "buttons",
                            "buttons": ["기분 알아보기" ]
                        }
                    }
                }
            else:
                content = {
                    "message": {
                        "text": "죄송해요 지금 당신의 기분을 알 수가 없네요..."
                    }
                }
        return Response(content, status=status.HTTP_200_OK, content_type='application/json; charset=utf-8')


class ChatRoomView(APIView):
    def delete(self, request):
        content = {'message': "SUCCESS"}
        return Response(content, status=status.HTTP_200_OK, content_type='application/json; charset=utf-8')


# stocks/
class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# button

class ButtonList(APIView):
    def get(self, request):
        buttons = Keyboard.objects.all()
        type = "buttons"
        serializer = ButtonSerializer(buttons, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def KaKaoList(APIView):
    pass


class SnippetList(APIView):
    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    코드 조각 조회, 업데이트, 삭제
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
