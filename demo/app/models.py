from django.db.models import Model,CharField,DateTimeField,UUIDField
import uuid
class CRUD(Model):
    id = UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    text = CharField()
    created = DateTimeField(auto_now_add=True,editable=False)
    updated = DateTimeField(auto_now=True,editable=False)
