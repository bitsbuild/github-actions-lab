from rest_framework.serializers import ModelSerializer
from app.models import CRUD
class CrudSerializer(ModelSerializer):
    class Meta:
        model = CRUD
        fields = ['id','text','created','updated']