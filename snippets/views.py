from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import  APIView
from rest_framework.response import Response
from snippets.models import Snippet,Stock
from snippets.serializers import SnippetSerializer,StockSerializer
from django.views.decorators.csrf import csrf_exempt

# Lists all stocks or create a new one

#stocks/
class StockList(APIView):
    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    def post(self):
        pass

def KaKaoList(APIView):
    pass

@api_view(['GET'])
def snippet_list(request):
    """
       전체 코드 조각 리스트 조회
    """
    try:
        snippet = Snippet.objects.all()
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

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

