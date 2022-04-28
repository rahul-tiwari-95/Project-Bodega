
# app_name = 'backend'
# urlpatterns = [
#  #path('', views.api_home, name='api_home'),
# ]

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views


urlpatterns = [

    # Landing Page URLs
    path('', views.home_page),
    path('not-auth/', views.filter_spam),
    path('home/', views.landing_page),
    path('home/aboutbodega/', views.about_us),
    path('home/contact-us/', views.contact_us),

    # METAUSER API ENDPOINTS
    path('bodega-api/metauser/', views.MetaUserList.as_view()),
    path('bodega-api/metauser/<int:pk>/', views.MetaUserDetail.as_view()),
    
    #METAUSER API ENDPOINTS via passcode=pk
    path('bodega-api/metauserauth/<str:pk>/', views.MetaUserPasscode),

    # Level API Endpoints
    path('bodega-api/level/', views.LevelList.as_view()),
    path('bodega-api/level/<int:pk>/', views.LevelDetail.as_view()),

    # BLA Score Endpoints
    path('bodega-api/blascore/', views.BLAScoreList.as_view()),
    path('bodega-api/blascore/<int:pk>/', views.BLAScoreDetail.as_view()),

    # Sentino Item Proximity Endpoints
    path('bodega-api/sentino_item_proximity/',views.SentinoItemProximityList.as_view()),
    path('bodega-api/sentino_item_proximity/<int:pk>/',views.SentinoItemProximityDetail.as_view()),

    # Sentino Item Projection Endpoints
    path('bodega-api/sentino_item_projection/',views.SentinoItemProjectionList.as_view()),
    path('bodega-api/sentino_item_projection/<int:pk>/',views.SentinoItemProjectionDetail.as_view()),

    # Sentino Item Classification Endpoints
    path('bodega-api/sentino_item_classification/',views.SentinoItemClassificationList.as_view()),
    path('bodega-api/sentino_item_classification/<int:pk>/',views.SentinoItemClassificationDetail.as_view()),

    # Sentino Description Endpoints
    path('bodega-api/sentino_description/', views.SentinoDescriptionList.as_view()),
    path('bodega-api/sentino_description/<int:pk>/',views.SentinoDescriptionDetail.as_view()),

    # Sentino Profile Endpoints
    path('bodega-api/sentino_profile/', views.SentinoProfileList.as_view()),
    path('bodega-api/sentino_profile/<int:pk>/', views.SentinoProfileDetail.as_view()),

    # Sentino Inventort Endpoints
    path('bodega-api/sentino_inventory/', views.SentinoInventoryList.as_view()),
    path('bodega-api/sentino_inventory/<int:pk>/',views.SentinoInventoryDetail.as_view()),

    # Bodega Vision Endpoints
    path('bodega-api/bodega_face/', views.BodegaFaceList.as_view()),
    path('bodega-api/bodega_face/<int:pk>/', views.BodegaFaceDetail.as_view()),

    # Bodega Personalizer Endpoints
    path('bodega-api/bodega_personalizer/', views.BodegaPersonalizerList.as_view()),
    path('bodega-api/bodega_personalizer/<int:pk>/',views.BodegaPersonalizerDetail.as_view()),

    # Bodega Cognitive Item Endpoints
    path('bodega-api/bodega_item/', views.BodegaCognitiveItemList.as_view()),
    path('bodega-api/bodega_item/<int:pk>/', views.BodegaCognitiveItemDetail.as_view()),

    # Bodega Cognitive Inventory Endpoints
    path('bodega-api/bodega_inventory/', views.BodegaCognitiveInventoryList.as_view()),
    path('bodega-api/bodega_inventory/<int:pk>/', views.BodegaCognitiveInventoryDetail.as_view()),

    # Bodega Cognitive Person Endpoints
    path('bodega-api/bodega_person/', views.BodegaCognitivePersonList.as_view()),
    path('bodega-api/bodega_person/<int:pk>/', views.BodegaCognitivePersonDetail.as_view()),

    # Bodega Department Endpoints
    path('bodega-api/bodega_dept/', views.BodegaDeptList.as_view()),
    path('bodega-api/bodega_dept/<int:pk>/', views.BodegaDeptDetail.as_view()),

    # User Address Endpoint by user_ID
    path('bodega-api/metauser_address/', views.UserAddressList.as_view()),
    path('bodega-api/metauser_address/<int:pk>/', views.UserAddressDetail.as_view()),

    # User Payment Endpoint by user_ID
    path('bodega-api/metauser_payment/', views.UserPaymentList.as_view()),
    path('bodega-api/metauser_payment/<int:pk>/', views.UserPaymentDetail.as_view()),

    # User Type Endpoint by user_ID
    path('bodega-api/metauser_type/', views.UserTypeList.as_view()),
    path('bodega-api/metauser_type/<int:pk>/', views.UserTypeDetail.as_view()),

    # Chat Room Endpoint by Chat Room ID
    path('bodega-api/metauser_chat_room/', views.ChatRoomList.as_view()),
    path('bodega-api/metauser_chat_room/<int:pk>/', views.ChatRoomDetail.as_view()),

    # Particpant Model  Endpoint by Chat Room ID
    path('bodega-api/participant/', views.ParticpantList.as_view()),
    path('bodega-api/participant/<int:pk>/', views.ParticpantDetail.as_view()),

    # Message Model Endpoint by messageID
    path('bodega-api/message/', views.MessageList.as_view()),
    path('bodega-api/message/<int:pk>/', views.MessageDetail.as_view()),

    # Product Category Model Endpoint by messageID
    path('bodega-api/product_category/', views.ProductCategoryList.as_view()),
    path('bodega-api/product_category/<int:pk>/', views.ProductCategoryDetail.as_view()),

    # Product Themes Model Endpoint by ProductID
    path('bodega-api/product_theme/', views.ProductThemesList.as_view()),
    path('bodega-api/product_theme/<int:pk>/', views.ProductThemesDetail.as_view()),

    # Discount Model Endpoint by DiscountID
    path('bodega-api/discount/', views.DiscountList.as_view()),
    path('bodega-api/discount/<int:pk>/', views.DiscountDetail.as_view()),

    # Social Model Endpoint 
    path('bodega-api/social/', views.SocialList.as_view()),
    path('bodega-api/social/<int:pk>/', views.SocialDetail.as_view()),

    # Shop Model Endpoint by shopID
    path('bodega-api/shop/', views.ShopList.as_view()),
    path('bodega-api/shop/<int:pk>/', views.ShopDetail.as_view()),

    # Product Metadata Endpoint
    path('bodega-api/product_metadata/', views.ProductMetaDataList.as_view()),
    path('bodega-api/product_metadata/<int:pk>/', views.ProductMetaDataDetail.as_view()),

    # Product Model Endpoint by ProductID
    path('bodega-api/product/', views.ProductList.as_view()),
    path('bodega-api/product/<int:pk>/', views.ProductDetail.as_view()),

    # collaboration Model Endpoint by collaborationID
    path('bodega-api/collaboration/', views.CollaborationList.as_view()),
    path('bodega-api/collaboration/<int:pk>/', views.CollaborationDetail.as_view()),

    # Shopping Session Endpoints
    path('bodega-api/shopping_session/', views.ShoppingSessionList.as_view()),
    path('bodega-api/shopping_session/<int:pk>/', views.ShoppingSessionDetail.as_view()),

    # Cart Item Endpoints
    path('bodega-api/cart_item/', views.CartItemList.as_view()),
    path('bodega-api/cart_item/<int:pk>/', views.CartItemDetail.as_view()),

    # Order Detail Endpoints
    path('bodega-api/order_detail/', views.OrderDetailList.as_view()),
    path('bodega-api/order_detail/<int:pk>/', views.OrderDetailDetail.as_view()),

    # Order Item Endpoints
    path('bodega-api/order_item/', views.OrderItemList.as_view()),
    path('bodega-api/order_item/<int:pk>/', views.OrderItemDetail.as_view()),


    # SysOpsAgent Endpoints
    path('bodega-api/sysops_agent/', views.SysOpsAgentList.as_view()),
    path('bodega-api/sysops_agent/<int:pk>/', views.SysOpsAgentDetail.as_view()),


    # SysOpsAgent Repo Endpoints
    path('bodega-api/sysops_agent_repo/', views.SysOpsAgentRepoList.as_view()),
    path('bodega-api/sysops_agent_repo/<int:pk>/',views.SysOpsAgentRepoDetail.as_view()),


    # SysOps ProjectRepo Endpoints
    path('bodega-api/sysops_agent_project/', views.SysOpsAgentProjectList.as_view()),
    path('bodega-api/sysops_agent_project/<int:pk>/',views.SysOpsAgentProjectDetail.as_view()),

    # SysOps DemandNode Endpoints
    path('bodega-api/sysopsdemandnode/', views.SysOpsDemandNodeList.as_view()),
    path('bodega-api/sysopsdemandnode/<int:pk>/', views.SysOpsDemandNodeDetail.as_view()),

    # SysOps SupplyNode Endpoints
    path('bodega-api/sysopssupplynode/', views.SysOpsSupplyNodeList.as_view()),
    path('bodega-api/sysopssupplynode/<int:pk>/', views.SysOpsSupplyNodeDetail.as_view()),
]


urlpatterns=format_suffix_patterns(urlpatterns)