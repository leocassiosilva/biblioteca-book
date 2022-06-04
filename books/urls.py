from django.urls import path
from .views import BookList, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('', BookList.as_view(), name='list_book'),
    path('create/', BookCreate.as_view(), name='create_book'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update_book'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete_book'),
]