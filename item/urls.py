from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from item.views import list_item, create_item, detail_item, delete_item, update_item,\
    list_maker, detail_maker, create_maker, update_maker, delete_maker

urlpatterns = [
    path('', list_item, name='list_item'),
    path('item/create/', create_item, name='create_item'),
    path('<int:pk>/', detail_item, name='detail_item'),
    path('item/delete/<int:pk>/', delete_item, name='delete_item'),
    path('item/update/<int:pk>/', update_item, name='update_item'),
    path('maker/', list_maker, name='list_maker'),
    path('maker/<int:pk>/', detail_maker, name='detail_maker'),
    path('maker/create/', create_maker, name='create_maker'),
    path('maker/update/<int:pk>/', update_maker, name='update_maker'),
    path('maker/delete/<int:pk>/', delete_maker, name='delete_maker'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)