from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .models import Women
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .serializers import WomenSerializer



class WomenAPIListPagination(PageNumberPagination):
    page_size =2
    page_size_query_param='page_size'
    max_page_size = 1000

class WomenAPIList(generics.ListCreateAPIView):
    """
    API для получения списка объектов и создания нового объекта Women.
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = WomenAPIListPagination

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API для получения объекта по ID и его обновления.
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated,]


class WomenAPIDestroyView(generics.RetrieveDestroyAPIView):
    """
    API для получения объекта по ID и его удаления.
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
