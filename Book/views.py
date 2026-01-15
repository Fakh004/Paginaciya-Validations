from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagination


class BookListCreateAPIView(APIView):
    pagination_class = BookPagination

    def get(self, request):
        queryset = Book.objects.all()

        author = request.query_params.get('author')
        genre = request.query_params.get('genre')
        title = request.query_params.get('title')

        if author:  
            queryset = queryset.filter(author__icontains=author)

        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        if title:
            queryset = queryset.filter(title__icontains=title)

        
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        serializer = BookSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
