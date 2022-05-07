from django.urls import path
from .views import *

# ------------------------------------------------------------------------------
# to define the api app that has workspace :
app_name = 'api'

# ------------------------------------------------------------------------------
# set api view URLs :
urlpatterns = [
    path('add/', FileUploadListAPI.as_view(), name='add_api'),
    path('post/', FileUploadCreateAPI.as_view(), name='create_api'),
]
