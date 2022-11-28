from rest_framework.viewsets import ModelViewSet
from .serialziers import UploadImagesSerializer
from .models import UploadImages

class UploadImageViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class = UploadImagesSerializer