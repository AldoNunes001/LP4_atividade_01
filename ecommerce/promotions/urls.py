from django.urls import path
from . import views


app_name = "promotions"
urlpatterns = [
    path("", views.list_promotions, name='list_promotions'),
    path("<int:promotion_id>", views.detail_promotion, name='detail_promotion'),
]
