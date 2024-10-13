from django.urls import path
from api.views import CNJProcessView, CNJExternalServiceView

urlpatterns = [
    path('api_cnj_process/', CNJProcessView.as_view(), name='cnj-process'),
    path('api_cnj_external-service/', CNJExternalServiceView.as_view(), name='cnj-external-service'),
]