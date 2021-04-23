from django.urls import path
from .views import HomeView, ArticleDetails, AddCategoryView, EditCategoryView, DeleteCategoryView, AddPostView, EditPost, DeletePost, AddCommentView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/a<int:pk>/detail', ArticleDetails.as_view(), name='article-detail'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('edit_category/c<int:pk>', EditCategoryView.as_view(), name='edit-category'),
    path('delete_category/c<int:pk>', DeleteCategoryView.as_view(), name='delete-category'),
    path('categories/', views.CategoriesList, name='categories-list'),
    path('category/<str:cat>/articles', views.CategoryView, name='category-view'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('edit_post/<int:pk>/', EditPost.as_view(), name='edit-post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name='delete-post'),
    path('like_post/<int:id>', views.LikeView, name='like_post'),
    path('love_view/<int:id>/', views.LoveView, name='love_view'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),

    # test
    path('article/comment/', views.asyncComment, name='async-comment'),

    path('test/', views.test, name='test'),
]