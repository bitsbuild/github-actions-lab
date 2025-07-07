from rest_framework.serializers import ModelSerializer
from app.models import CRUD
class CRUDSerializer(ModelSerializer):
    model = CRUD
    fields = '__all__'