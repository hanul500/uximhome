from django.urls import path
from .views import (
	news_list_view,
	news_create_view,
	news_detail_view,
	news_update_view,
	news_delete_view,
	activity_list_view,
	activity_create_view,
	activity_detail_view,
	activity_update_view,
	activity_delete_view
)
from uximhome.views import(
	session_page
)



urlpatterns = [
	path('',session_page),
	
	path('news/create/',news_create_view),
	path('news/<str:slug>/edit/',news_update_view),
	path('news/<str:slug>/delete/',news_delete_view),
	path('news/<str:slug>/',news_detail_view),
	path('news/',news_list_view),

	path('activity/create/',activity_create_view),
	path('activity/<str:slug>/edit/',activity_update_view),
	path('activity/<str:slug>/delete/',activity_delete_view),
	path('activity/<str:slug>/',activity_detail_view),
	path('activity/',activity_list_view),
	]
