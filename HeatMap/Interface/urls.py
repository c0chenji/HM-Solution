from django.urls import path
from .views import (
	                ChannelListView,
	                ChannelUpdateView,
	                ChannelDeleteView,
                    USBChannelUpdateView,
                    ZoneUpdateView,   
                               
	               )
from . import views

urlpatterns = [
    path('main/', views.generel, name='Interface-generelUi'),
    path('channel/', ChannelListView.as_view(), name='Interface-channel'),
    path('channel/<int:pk>/edit',ChannelUpdateView.as_view(), name='Interface-channel_edit'),
    path('channel/create',views.Home, name='Interface-new_channel'),
    path('channel/usb',views.createUSB, name='Interface-newUSBchannel'),
    path('channel/<int:pk>/usbedit',USBChannelUpdateView.as_view(), name='Interface-USBchanneledit'),
    path('channel/<int:pk>/delete',ChannelDeleteView.as_view(), name='Interface-channel_delete'),
    path('zone/<int:pk>/edit', ZoneUpdateView.as_view(), name='Interface-zone'),
    path('zoneedit/', views.ZoneeditData, name='Interface-zoneedit'),
    path('heatmap/', views.heatmap_page, name='Interface-heatmap'),
    path('displayLiveStream/', views.displayLiveStream, name='display-live-stream'),
    path('displayLiveStream/livestream/<int:id>/', views.liveStream_page, name='live-stream-page'),
    path('', views.Front, name='Interface-front'),
    
    # path('plivestream/', views.pauseLiveStream_page, name='pause-live-stream-page'),
    # path('pauseLivesStream/', views.pauseLiveStream, name='pause-live-stream'),

    
]


