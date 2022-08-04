from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Vacancy, Company, Category, Vacant
from common.models import User
from .serializer import CountsSerializer, CategorySerializer
from rest_framework import generics
from django.db import models
from django.db.models import Count
from rest_framework import views
from rest_framework.response import Response


# Create your views here.

class CountsViewSet(views.APIView):
    def get(self, request):
        data_counts = [
            {
                "vacancy_count": Vacancy.objects.all().count(),
                "company_count": Company.objects.all().count(),
                "user_count": User.objects.all().count(),
            }
        ]
        results = CountsSerializer(data_counts, many=True).data
        return Response(results)


class CategoriesListViewSet(views.APIView):
    def get(self, request):
        data = []
        categories = Category.objects.all()
        for c in categories:
            vacants = c.vacants.all()
            min_prices = []
            max_prices = []
            for v in vacants:
                min_prices.append(v.min_price)
                max_prices.append(v.max_price)

            min_price = min(min_prices)
            max_price = max(max_prices)

            if 2*min_price < max_price:
                min_price = (min_price+(min_price+max_price)/2)/2
                max_price = ((min_price+max_price)/2+max_price)/2
                price = f'{min_price} - {max_price}'
            else:
                price = (min_price+max_price)/2

            data.append({
                'title': c.title,
                'price': price
            })
        category_data = data
        results = CategorySerializer(category_data, many=True).data
        return Response(results)