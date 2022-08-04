from rest_framework import serializers
from .models import Vacancy, Company


class CountsSerializer(serializers.Serializer):
    vacancy_count = serializers.IntegerField()
    company_count = serializers.IntegerField()
    user_count = serializers.IntegerField()

    class Meta:
        fields = (
            'vacancy_count',
            'company_count',
            'user_count',
        )


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.CharField(max_length=255)

    class Meta:
        fields = (
            'title',
            'price'
        )