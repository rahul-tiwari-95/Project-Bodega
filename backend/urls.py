
# app_name = 'backend'
# urlpatterns = [
  #  #path('', views.api_home, name='api_home'),
# ]

from django.urls import path, include
from backend import views



urlpatterns = [

  # Landing Page URLs
  path('', views.home_page), 
  path('not-auth/', views.filter_spam), 
  path('home/', views.landing_page), 
  path('home/aboutbodega/', views.about_us), 
  path('home/contact-us/', views.contact_us),

  # SOLOMON API ENDPOINTS
  path('bodega-api/solomon/', views.solomon_list),
  path('bodega-api/solomon/<int:pk>/', views.solomon_detail),

  # METAUSER API ENDPOINTS
  path('bodega-api/metauser/', views.metauser_list),
  path('bodega-api/metauser/<int:pk>/', views.metauser_detail),

  # Level API Endpoints
  path('bodega-api/level/', views.level_list),
  path('bodega-api/level/<int:pk>/', views.level_detail),
  
  #BLA Score Endpoints
  path('bodega-api/blascore/', views.blascore_list),
  path('bodega-api/blascore/<int:pk>/', views.blascore_detail),
  
  #Sentino Item Proximity Endpoints
  path('bodega-api/sentino_item_proximity/', views.sentino_item_proximity_list),
  path('bodega-api/sentino_item_proximity/<int:pk>/', views.sentino_item_proximity_detail),
  
  #Sentino Item Projection Endpoints
  path('bodega-api/sentino_item_projection/', views.sentino_item_projection_list),
  path('bodega-api/sentino_item_projection/<int:pk>/', views.sentino_item_projection_detail),
  
  #Sentino Item Classification Endpoints
  path('bodega-api/sentino_item_classification/', views.sentino_item_classification_list),
  path('bodega-api/sentino_item_classification/<int:pk>/', views.sentino_item_classification_detail),
  
  #Sentino Description Endpoints
  path('bodega-api/sentino_description/', views.sentino_description_list),
  path('bodega-api/sentino_description/<int:pk>/', views.sentino_description_detail),
  
  #Sentino Inventory Endpoints
  path('bodega-api/sentino_profile/', views.sentino_profile_list),
  path('bodega-api/sentino_profile/<int:pk>/', views.sentino_profile_detail),
  
  #Sentino Profile Endpoints
  path('bodega-api/sentino_inventory/', views.sentino_inventory_list),
  path('bodega-api/sentino_inventory/<int:pk>/', views.sentino_inventory_detail),
  
  #Bodega Vision Endpoints
  path('bodega-api/bodega_face/', views.bodega_face_list),
  path('bodega-api/bodega_face/<int:pk>/', views.bodega_face_detail),
  
  #Bodega Personalizer Endpoints
  path('bodega-api/bodega_personalizer/', views.bodega_personalizer_list),
  path('bodega-api/bodega_personalizer/<int:pk>/', views.bodega_personalizer_detail),
  
  #Bodega Cognitive Item Endpoints
  path('bodega-api/bodega_item/', views.bodega_item_list),
  path('bodega-api/bodega_item/<int:pk>/', views.bodega_item_detail),
  
  #Bodega Cognitive Inventory Endpoints
  path('bodega-api/bodega_inventory/', views.bodega_inventory_list),
  path('bodega-api/bodega_inventory/<int:pk>/', views.bodega_inventory_detail),
  
  #Bodega Cognitive Person Endpoints
  path('bodega-api/bodega_person/', views.bodega_person_list),
  path('bodega-api/bodega_person/<int:pk>/', views.bodega_person_detail),
  
  #Bodega Department Endpoints
  path('bodega-api/bodega_dept/', views.bodega_dept_list),
  path('bodega-api/bodega_dept/<int:pk>/', views.bodega_dept_detail),
  
  # User Address Endpoint by user_ID
  path('bodega-api/metauser_address/', views.address_list),
  path('bodega-api/metauser_address/<int:pk>/', views.address_detail),

  # User Address endpoint by User_AddressID
  path('bodega-api/metauser_address/child_id=<int:pk>/', views.child_address_detail),

  # User Payment Endpoint by user_ID
  path('bodega-api/metauser_payment/', views.user_payment_list),
  path('bodega-api/metauser_payment/<int:pk>/', views.user_payment_detail),

  # User Address endpoint by User_AddressID
  path('bodega-api/metauser_payment/child_id=<int:pk>/', views.child_payment_detail),

  # User Type Endpoint by user_ID
  path('bodega-api/metauser_type/', views.user_type_list),
  path('bodega-api/metauser_type/<int:pk>/', views.user_type_detail),

  # User Type endpoint by User_AddressID
  path('bodega-api/metauser_type/child_id=<int:pk>/', views.child_type_detail),

  # Chat Room Endpoint by Chat Room ID
  path('bodega-api/metauser_chat_room/', views.chat_room_list),
  path('bodega-api/metauser_chat_room/<int:pk>/', views.chat_room_detail),

  # Particpant Model  Endpoint by Chat Room ID
  path('bodega-api/participant/', views.participant_list),
  path('bodega-api/participant/<int:pk>/', views.participant_detail),

  # Message Model Endpoint by messageID
  path('bodega-api/message/', views.message_list),
  path('bodega-api/message/<int:pk>/', views.message_detail),

  # Product Category Model Endpoint by messageID
  path('bodega-api/product_category/', views.product_category_list),
  path('bodega-api/product_category/<int:pk>/', views.product_category_detail),

  # Product Themes Model Endpoint by ProductID
  path('bodega-api/product_theme/', views.product_theme_list),
  path('bodega-api/product_theme/<int:pk>/', views.product_theme_detail),

  # Discount Model Endpoint by DiscountID
  path('bodega-api/discount/', views.discount_list),
  path('bodega-api/discount/<int:pk>/', views.discount_detail),

  # Social Model Endpoint by DiscountID
  path('bodega-api/social/', views.social_list),
  path('bodega-api/social/<int:pk>/', views.social_detail),

  # Shop Model Endpoint by shopID
  path('bodega-api/shop/', views.shop_list),
  path('bodega-api/shop/<int:pk>/', views.shop_detail),
  
  path('bodega-api/shop/parent_ID=<int:pk>/', views.parent_shop_detail),

# Product Metadata Endpoint 
  path('bodega-api/product_metadata/', views.product_metadata_list),
  path('bodega-api/product_metadata/<int:pk>/', views.product_metadata_detail),

  # Product Model Endpoint by ProductID
  path('bodega-api/product/', views.product_list),
  path('bodega-api/product/<int:pk>/', views.product_detail),

  # collaboration Model Endpoint by collaborationID
  path('bodega-api/collaboration/', views.collaboration_list),
  path('bodega-api/collaboration/<int:pk>/', views.collaboration_detail),

  #Shopping Session Endpoints
  path('bodega-api/shopping_session/', views.shopping_session_list),
  path('bodega-api/shopping_session/<int:pk>/', views.shopping_session_detail),

  #Cart Item Endpoints
  path('bodega-api/cart_item/', views.cart_item_list),
  path('bodega-api/cart_item/<int:pk>/', views.cart_item_detail),
  
  #Order Detail Endpoints
  path('bodega-api/order_detail/', views.order_detail_list),
  path('bodega-api/order_detail/<int:pk>/', views.order_detail_detail),
  
  #Order Item Endpoints
  path('bodega-api/order_item/', views.order_item_list),
  path('bodega-api/order_item/<int:pk>/', views.order_item_detail),
  
  
  #SysOpsAgent Endpoints
  path('bodega-api/sysops_agent/', views.sysops_agent_list),
  path('bodega-api/sysops_agent/<int:pk>/', views.sysops_agent_detail),
  
  
  #SysOpsAgent Repo Endpoints
  path('bodega-api/sysops_agent_repo/', views.sysops_agent_repo_list),
  path('bodega-api/sysops_agent_repo/<int:pk>/', views.sysops_agent_repo_detail),
  
  
  #SysOps ProjectRepo Endpoints
  path('bodega-api/sysops_agent_project/', views.sysops_agent_project_list),
  path('bodega-api/sysops_agent_project/<int:pk>/', views.sysops_agent_project_detail),
  
  #SysOps DemandNode Endpoints
  path('bodega-api/sysopsdemandnode/', views.sysopsdemandnode_list),
  path('bodega-api/sysopsdemandnode/<int:pk>/', views.sysopsdemandnode_detail),
  
  #SysOps SupplyNode Endpoints
  path('bodega-api/sysopssupplynode/', views.sysopssupplynode_list),
  path('bodega-api/sysopssupplynode/<int:pk>/', views.sysopssupplynode_detail),
]