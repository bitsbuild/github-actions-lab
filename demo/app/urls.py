from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import CrudVS
router = DefaultRouter()
router.register(r'crud',CrudVS,basename='crud')
urlpatterns = router.urls
