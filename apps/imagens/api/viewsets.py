import base64
from io import BytesIO

import cv2
from PIL import Image
from apps.imagens.models import Imagens

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
import numpy as np
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ImagensSerializer


class ImagensViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensSerializer
    queryset = Imagens.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        imagem = serializer.data.get('imagem')

        sbuf = BytesIO()
        sbuf.write(base64.b64decode(imagem))
        pimg = Image.open(sbuf)

        cv2_img = cv2.cvtColor(np.array(pimg), cv2.COLOR_BGR2GRAY)
        # cv2.imwrite("reconstructed.jpg", cv2_img)
        image_encode = cv2.imencode('.jpg', cv2_img)[1]
        image_encode = base64.b64encode(image_encode).decode('utf8')

        return Response({"imagem_cinza": image_encode}, status=status.HTTP_200_OK)
