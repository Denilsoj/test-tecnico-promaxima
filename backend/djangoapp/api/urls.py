from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListMedicineView

router = DefaultRouter()
router.register(r'', ListMedicineView, basename='medicine')

urlpatterns = [
    path('', include(router.urls)),
]