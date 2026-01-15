from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'published_year')

    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("The first letter of the title must be uppercase.")
        return value
    
