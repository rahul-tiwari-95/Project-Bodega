


#app_name = 'backend'
#urlpatterns = [
  #  #path('', views.api_home, name='api_home'),
#]

from django.urls import path, include
from backend import views


urlpatterns = [

  path('', views.home_page), #sends to index html
  path('not-auth/', views.filter_spam), #sends to index html
  path('home/', views.landing_page), #after True, on index.html
  path('home/aboutbodega/', views.about_us), #about us
  path('home/contact-us/', views.contact_us), #contact us

  #METAUSER API ENDPOINTS
  path('bodega-api/metauser/', views.metauser_list),
  path('bodega-api/metauser/<int:pk>/', views.metauser_detail),

  #User Address Endpoint by user_ID
  path('bodega-api/metauser_address/', views.address_list),
  path('bodega-api/metauser_address/<int:pk>/', views.address_detail),

  #User Address endpoint by User_AddressID
  path('bodega-api/metauser_address/child_id=<int:pk>/', views.child_address_detail),


    #User Payment Endpoint by user_ID
  path('bodega-api/metauser_payment/', views.user_payment_list),
  path('bodega-api/metauser_payment/<int:pk>/', views.user_payment_detail),

  #User Address endpoint by User_AddressID
  path('bodega-api/metauser_payment/child_id=<int:pk>/', views.child_payment_detail),


  #User Type Endpoint by user_ID
  path('bodega-api/metauser_type/', views.user_type_list),
  path('bodega-api/metauser_type/<int:pk>/', views.user_type_detail),

  #User Type endpoint by User_AddressID
  path('bodega-api/metauser_type/child_id=<int:pk>/', views.child_type_detail),

  #Chat Room Endpoint by Chat Room ID
  path('bodega-api/metauser_chat_room/', views.chat_room_list),
  path('bodega-api/metauser_chat_room/<int:pk>/', views.chat_room_detail),

  #Particpant Model  Endpoint by Chat Room ID
  path('bodega-api/participant/', views.participant_list),
  path('bodega-api/participant/<int:pk>/', views.participant_detail),


  #Message Model Endpoint by messageID
  path('bodega-api/message/', views.message_list),
  path('bodega-api/message/<int:pk>/', views.message_detail),


  #Product Category Model Endpoint by messageID
  path('bodega-api/product_category/', views.product_category_list),
  path('bodega-api/product_category/<int:pk>/', views.product_category_detail),


  #Product Themes Model Endpoint by ProductID
  path('bodega-api/product_theme/', views.product_theme_list),
  path('bodega-api/product_theme/<int:pk>/', views.product_theme_detail),


  #Discount Model Endpoint by DiscountID
  path('bodega-api/discount/', views.discount_list),
  path('bodega-api/discount/<int:pk>/', views.discount_detail),


  #Social Model Endpoint by DiscountID
  path('bodega-api/social/', views.social_list),
  path('bodega-api/social/<int:pk>/', views.social_detail),
  path('bodega-api/social/parent_ID=<int:pk>/', views.parent_social_detail),


  #Shop Model Endpoint by shopID
  path('bodega-api/shop/', views.shop_list),
  path('bodega-api/shop/<int:pk>/', views.shop_detail),
  
  path('bodega-api/shop/parent_ID=<int:pk>/', views.parent_shop_detail),


  #Product Model Endpoint by ProductID
  path('bodega-api/product/', views.product_list),
  path('bodega-api/product/<int:pk>/', views.product_detail),


  #collaboration Model Endpoint by collaborationID
  path('bodega-api/collaboration/', views.collaboration_list),
  path('bodega-api/collaboration/<int:pk>/', views.collaboration_detail)



]