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
    path('book-industry/<int:id>', views.book_industry, name='book_industry'),
    path('view-industry/<int:id>/<int:industry_id>', views.view_industry, name='view_industry'),
    path('upload-resume/<int:id>/<int:industry_id>', views.upload_resume, name='upload_resume'),
    path('delete-resume/<int:id>/<int:industry_booking_id>/<int:industry_id>', views.delete_resume, name='delete_resume'),
    path('delete-industry/<int:id>', views.delete_industry, name='delete_industry'),
    path('add-messages/<int:id>/<int:industry_id>', views.add_messages, name="add_messages"),

]
