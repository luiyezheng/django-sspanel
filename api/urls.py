#from django.conf.urls import url
from django.urls import path, re_path
from .import views


app_name = "api"
urlpatterns = [
    path('test/', views.test, name='test'),
    path('user/data/', views.userData, name='userdata'),
    path('node/data/', views.nodeData, name='nodedata'),
    path('donate/data/', views.donateData, name='donatedata'),
    path('random/port/', views.change_ss_port, name='changessport'),
    path('gen/invitecode/', views.gen_invite_code, name='geninvitecode'),
    path('shop/', views.purchase, name='purchase'),
    path('pay/request/', views.pay_request, name='pay_request'),
    path('pay/query/', views.pay_query, name='pay_query'),
    path('traffic/query/', views.traffic_query, name='traffic_query'),
    re_path(r'^qrcode/(?P<content>.+)/$', views.get_qrcode, name='get_qrcode'),
    # 91pay支持
    path('pay/notify/', views.pay_notify, name='pay_notify'),
    path('pay/91/request/', views.pay91_request, name='pay91_request'),
    path('pay/91/query/', views.pay91_query, name='pay91_query'),    
]
