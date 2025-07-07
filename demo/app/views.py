from rest_framework.viewsets import ModelViewSet
from app.models import CRUD
from app.serializers import CrudSerializer
class CrudVS(ModelViewSet):
    queryset = CRUD.objects.all()
    serializer_class = CrudSerializer