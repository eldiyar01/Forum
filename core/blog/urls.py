from django.urls import path

from .views import CategoryDetail,NewsView, newsdetail, search_result

app_name = 'blog'
urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('news/<int:pk>/', newsdetail, name='news_detail'),
    path('search-result/', search_result, name='search-result'),

]



# path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
# path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
# path('post/create/', PostCreate.as_view(), name='post_create'),