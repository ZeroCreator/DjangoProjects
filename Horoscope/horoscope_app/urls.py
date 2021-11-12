from django.urls import path
from . import views

# Path Converters
urlpatterns = [
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name="horoscope_name" ),
]
