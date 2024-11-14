from django.urls import path
from .views import my_view, profile_view, CarListView

urlpatterns = [
    # path("carlist/", my_view, name="carlist"),
    path("carlist/", CarListView.as_view(), name="carlist"),
    path("detail/<int:id>", my_view, name="detail"),
    path("brand/<str:brand>", my_view, name="marcas"),
    path("profile/<int:author_id>", profile_view, name="perfil")
]
