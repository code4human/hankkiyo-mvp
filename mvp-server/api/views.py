from rest_framework import viewsets, permissions   # , filters
from .models import Category, Store, Order
from .serializers import (
    CategoryListSerializer, CategoryDetailSerializer,
    StoreListSerializer, StoreDetailSerializer,
    OrderSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by("id")   # .filter(active=True)
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return super(CategoryViewSet, self).get_serializer_class()


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()   # order_by("-created")   # 내림차순
    serializer_class = StoreListSerializer
    detail_serializer_class = StoreDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return super(StoreViewSet, self).get_serializer_class()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-date_ordered")
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny, )
