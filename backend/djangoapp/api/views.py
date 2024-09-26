from rest_framework.viewsets import ViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Medicine
from .serializers import MedicineSerializer

class MedicinePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'  
    max_page_size = 25  

class ListMedicineView(ViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    pagination_class = MedicinePagination

    def list(self, request):
        queryset = self.queryset
        
        substance = request.query_params.get('substance', None)
        cnpj = request.query_params.get('cnpj', None)
        laboratory = request.query_params.get('laboratory', None)

        if substance:
            queryset = queryset.filter(substance__icontains=substance)
        if cnpj:
            queryset = queryset.filter(cnpj=cnpj)
        if laboratory:
            queryset = queryset.filter(laboratory__icontains=laboratory)

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer.data)