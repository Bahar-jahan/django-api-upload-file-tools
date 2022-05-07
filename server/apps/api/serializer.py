from rest_framework.serializers import ModelSerializer
from apps.datastorege.models import FileUploadModel


# ------------------------------------------------------------------------------------------------
# serialize model using for  both API views  :
class FileUploadCreateSerializer(ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = '__all__'
