from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('persons/', views.show_persons, name='persons'),
    path('add_person/', views.add_person, name='add_person'),
    path('redact_person', views.redact_person, name='redact_person'),
    path('delete/<int:person_id>/', views.delete_person, name='delete_person'),
    path('edit_person/<int:id>/', views.edit_person, name='edit'),
    path('edit_person/<int:id>',views.refactor_person, name='edit_person'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:id>', views.goods_buy, name='buy'),
    path('buy_method/', views.add_buy_method, name='buy_method'),
    path('seller/', views.seller_log, name='seller_log'),
    path('goods_create/',views.create_goods, name='create-goods'),
    path('goods_seller/', views.seller_page, name='seller_page')
]