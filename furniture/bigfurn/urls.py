from django.urls import path
from .views import BigFurnPage


urlpatterns = [
    path('', BigFurnPage.as_view(), name='bigfurn')
]
