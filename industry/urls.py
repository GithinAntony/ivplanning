from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('change-password', views.change_password, name='change_password'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery-delete/<int:id>', views.gallery_delete, name='gallery_delete'),
    path('iv-requests', views.iv_requests, name='iv_requests'),
    path('iv-requests-view/<int:id>', views.iv_requests_view, name='iv_requests_view'),
    path('add-messages/<int:id>', views.add_messages, name="add_messages"),
    path('view-resume/<int:id>', views.view_resume, name='view_resume'),    
]
