
# app_name = 'backend'
# urlpatterns = [
#  #path('', views.api_home, name='api_home'),
# ]

from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from backend import views
from .views import *
#import stripeServer.views as stripeViews




urlpatterns = [

    # Landing Page URLs
    path('', views.home_page),
    path('not-auth/', views.filter_spam),
    path('home/', views.landing_page),
    path('home/aboutbodega/', views.about_us),
    path('home/contact-us/', views.contact_us),











    #Stripe Integration Endpoints

    #Create a new Stripe Express Account 
    path('bodegaCreators/createStripeAccount/', views.createStripeAccount),
    #Authenticate Stripe AccountLink
    path('bodegaCreators/authenticateStripeAccount/', views.authenticateStripeAccount),

    #Retreive Stripe Account IDs
    path('bodegaCreators/fetchStripeAccount/', views.retreiveStripeAccount),

    #Retreive Stripe Account Info on Bodega 
    path('bodegaCreators/stripeAccount/', views.StripeAccountInfoList.as_view()),
    path('bodegaCreators/stripeAccount/<int:pk>/', views.StripeAccountInfoDetail.as_view()),

    #Create Fund Transfer to Eligible Stripe Account
    path('bodegaCreators/createPayoutTransfer/', views.payoutStripeAccount),

    path('bodegaCreators/stripeTransfer/', views.StripeAccountTransferList.as_view()),
    path('bodegaCreators/stripeTransfer/<int:pk>/', views.StripeAccountTransferDetail.as_view()),

    #Stripe Endpoint to list all transfers
    path('bodegaCreators/allStripeTransfers/', views.allStripeTransfers),

    #Stripe Endpoint for Refunding funds
    path('bodegaCreators/reverseFunds/', views.reverseFunds),

    #Stripe Endpoint for retrieving our Stripe Balance.
    path('bodegaCreators/stripeBalance/', views.retrieveStripeBalance),

    #Create Stripe Charge
    path('bodegaCreators/createCharge/', views.createCharge),

    #List all Charges and manipulate them 
    path('bodegaCreators/allCharges/', views.StripeChargesList.as_view()),
    path('bodegaCreators/allCharges/<int:pk>/', views.StripeChargesDetail.as_view()),

    #Create Stripe Customer Objects
    path('bodegaCreators/createCustomer/', views.createStripeCustomer),

    path('bodegaCreators/allCustomers/', views.bodegaCustomerList.as_view()),
    path('bodegaCreators/allCustomers/<int:pk>/', views.bodegaCustomerDetail.as_view()),

    #Create Subscription Product and Price it - For Creators
    path('bodegaCreators/createSubscription/', views.createStripeSubscriptionProduct),

    #For Customers to subscribe to Creator's subscription
    path('bodegaCreators/subscribe/', views.subscribe),

    #All Stripe Creator SubscriptionsList
    path('bodegaCreators/allSubscriptions/', views.creatorSubscriptionList.as_view()),
    path('bodegaCreators/allSubscriptions/<int:pk>/', views.creatorSubscriptionDetail.as_view()),













    # SOLOMON API ENDPOINTS
    path('bodega-api/solomon/', views.solomon_list),
    path('bodega-api/solomon/<int:pk>/', views.solomon_detail),

    # METAUSER API ENDPOINTS
    path('bodega-api/metauser/', views.metauser_list),
    path('bodega-api/metauser/<int:pk>/', views.metauser_detail),


    # Level API Endpoints
    path('bodega-api/level/', views.level_list),
    path('bodega-api/level/<int:pk>/', views.level_detail),

    # BLA Score Endpoints
    path('bodega-api/blascore/', views.blascore_list),
    path('bodega-api/blascore/<int:pk>/', views.blascore_detail),

    # Sentino Item Proximity Endpoints
    path('bodega-api/sentino_item_proximity/', views.sentino_item_proximity_list),
    path('bodega-api/sentino_item_proximity/<int:pk>/', views.sentino_item_proximity_detail),

    # Sentino Item Projection Endpoints
    path('bodega-api/sentino_item_projection/',
         views.sentino_item_projection_list),
    path('bodega-api/sentino_item_projection/<int:pk>/',
         views.sentino_item_projection_detail),

    # Sentino Item Classification Endpoints
    path('bodega-api/sentino_item_classification/',
         views.sentino_item_classification_list),
    path('bodega-api/sentino_item_classification/<int:pk>/',
         views.sentino_item_classification_detail),

    # Sentino Description Endpoints
    path('bodega-api/sentino_description/', views.sentino_description_list),
    path('bodega-api/sentino_description/<int:pk>/',
         views.sentino_description_detail),

    # Sentino Inventory Endpoints
    path('bodega-api/sentino_profile/', views.sentino_profile_list),
    path('bodega-api/sentino_profile/<int:pk>/', views.sentino_profile_detail),

    # Sentino Profile Endpoints
    path('bodega-api/sentino_inventory/', views.sentino_inventory_list),
    path('bodega-api/sentino_inventory/<int:pk>/',
         views.sentino_inventory_detail),

    # Bodega Vision Endpoints
    path('bodega-api/bodega_face/', views.bodega_face_list),
    path('bodega-api/bodega_face/<int:pk>/', views.bodega_face_detail),

    # Bodega Personalizer Endpoints
    path('bodega-api/bodega_personalizer/', views.bodega_personalizer_list),
    path('bodega-api/bodega_personalizer/<int:pk>/', views.bodega_personalizer_detail),

    # Bodega Cognitive Item Endpoints
    path('bodega-api/bodega_item/', views.bodega_item_list),
    path('bodega-api/bodega_item/<int:pk>/', views.bodega_item_detail),

    # Bodega Cognitive Inventory Endpoints
    path('bodega-api/bodega_inventory/', views.bodega_inventory_list),
    path('bodega-api/bodega_inventory/<int:pk>/', views.bodega_inventory_detail),

    # Bodega Cognitive Person Endpoints
    path('bodega-api/bodega_person/', views.bodega_person_list),
    path('bodega-api/bodega_person/<int:pk>/', views.bodega_person_detail),

    # Bodega Department Endpoints
    path('bodega-api/bodega_dept/', views.bodega_dept_list),
    path('bodega-api/bodega_dept/<int:pk>/', views.bodega_dept_detail),

    # User Address Endpoint by user_ID
    path('bodega-api/metauser_address/', views.address_list),
    path('bodega-api/metauser_address/<int:pk>/', views.address_detail),

    # User Address endpoint by User_AddressID
    path('bodega-api/metauser_address/child_id=<int:pk>/',
         views.child_address_detail),

    # User Payment Endpoint by user_ID
    path('bodega-api/metauser_payment/', views.user_payment_list),
    path('bodega-api/metauser_payment/<int:pk>/', views.user_payment_detail),

    # User Address endpoint by User_AddressID
    path('bodega-api/metauser_payment/child_id=<int:pk>/', views.child_payment_detail),


    # METAUSER API ENDPOINTS
    path('bodega-api/metauser/', views.MetaUserList.as_view()),
    path('bodega-api/metauser/<int:pk>/', views.MetaUserDetail.as_view()),


    
    #METAUSER API ENDPOINTS via passcode=pk
    path('bodega-api/metauserauth/<str:pk>/', views.metauserauth),
    #KILL SWITCH API
    path('bodega-api/killswitch/', views.killswitch),

    path('bodega-api/cartbymetauser/<int:pk>/', views.cartbymetauser),

    path('bodega-api/shopbymetauser/', views.FetchShopByMetaUserID),

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
    path('bodega-api/participant/', views.ParticipantList.as_view()),
    path('bodega-api/participant/<int:pk>/', views.ParticpiantDetail.as_view()),

    path('bodega-api/chatRoomsByMetauserID/', views.FetchParticipantByMetaUserID),
    path('bodega-api/chatRoomAuth/<int:pk>/', views.AuthenticateParticipantByRoomHashkey),

    # Message Model Endpoint by messageID
    path('bodega-api/message/', views.MessageList.as_view()),
    path('bodega-api/message/<int:pk>/', views.MessageDetail.as_view()),

    # Product Category Model Endpoint by messageID
    path('bodega-api/product_category/', views.ProductCategoryList.as_view()),
    path('bodega-api/product_category/<int:pk>/', views.ProductCategoryDetail.as_view()),

    # Boost Tags Model Endpoint by ProductID
    path('bodega-api/boostTags/', views.BoostTagsList.as_view()),
    path('bodega-api/boostTags/<int:pk>/', views.BoostTagsDetail.as_view()),

    #Searching for BoostTags by tags
    path('bodega-api/searchBoostTags/', views.searchBoostTags),

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

    path('bodega-api/searchProduct/', views.searchProductByName),


    # Product Model Endpoint by ProductID

    path('bodega-api/product/', views.ProductList.as_view()),
    path('bodega-api/product/<int:pk>/', views.ProductDetail.as_view()),

    path('bodega-api/munchiesFeed/', views.MunchiesPageList.as_view()), #Show all content from all Munchies Pages
    path('bodega-api/singleMunchiePage/<int:pk>/', views.MunchiesPageDetail.as_view()), #Shows one single Munchies Page

    path('bodega-api/singleMunchieVideo/', views.MunchiesVideoList.as_view()),
    path('bodega-api/multipleMunchieVideos/<int:pk>/', views.MunchiesVideoDetail.as_view()),

    path('bodega-api/product/', views.ProductList.as_view()),
    path('bodega-api/product/<int:pk>/', views.ProductDetail.as_view()),

    path('bodega-api/munchiesFeed/', views.MunchiesPageList.as_view()), #Show all content from all Munchies Pages
    path('bodega-api/singleMunchiePage/<int:pk>/', views.MunchiesPageDetail.as_view()), #Shows one single Munchies Page

    path('bodega-api/singleMunchieVideo/', views.MunchiesVideoList.as_view()),
    path('bodega-api/multipleMunchieVideos/<int:pk>/', views.MunchiesVideoDetail.as_view()),


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

    
    # Order Success Endpoints
    path('bodega-api/orderSuccess/', views.OrderSuccessList.as_view()),
    path('bodega-api/orderSuccess/<int:pk>/', views.OrderSuccessDetail.as_view()),

    
    # Order Success Endpoints
    path('bodega-api/orderSuccess/', views.OrderSuccessList.as_view()),
    path('bodega-api/orderSuccess/<int:pk>/', views.OrderSuccessDetail.as_view()),


    # Order failure Endpoints
    path('bodega-api/orderFailure/', views.OrderFailureList.as_view()),
    path('bodega-api/orderFailure/<int:pk>/', views.OrderFailureDetail.as_view()),

    # Order failure Endpoints
    path('bodega-api/orderFailure/', views.OrderFailureList.as_view()),
    path('bodega-api/orderFailure/<int:pk>/', views.OrderFailureDetail.as_view()),

    # SysOpsAgent Endpoints
    path('bodega-api/sysops_agent/', views.SysOpsAgentList.as_view()),
    path('bodega-api/sysops_agent/<int:pk>/', views.SysOpsAgentDetail.as_view()),


    # SysOpsAgent Repo Endpoints

    path('bodega-api/sysops_agent_repo/', views.SysOpsAgentRepoList.as_view()),
    path('bodega-api/sysops_agent_repo/<int:pk>/',views.SysOpsAgentRepoDetail.as_view()),


    # SysOps ProjectRepo Endpoints
    path('bodega-api/sysops_agent_project/', views.SysOpsAgentProjectList.as_view()),
    path('bodega-api/sysops_agent_project/<int:pk>/',views.SysOpsAgentProjectDetail.as_view()),

    # SysOps ProjectRepo Endpoints
    path('bodega-api/sysops_agent_project/', views.SysOpsAgentProjectList.as_view()),
    path('bodega-api/sysops_agent_project/<int:pk>/',views.SysOpsAgentProjectDetail.as_view()),
    # SysOps DemandNode Endpoints
    path('bodega-api/sysopsdemandnode/', views.SysOpsDemandNodeList.as_view()),
    path('bodega-api/sysopsdemandnode/<int:pk>/', views.SysOpsDemandNodeDetail.as_view()),

    # SysOps SupplyNode Endpoints

    path('bodega-api/sysopssupplynode/', views.SysOpsSupplyNodeList.as_view()),
    path('bodega-api/sysopssupplynode/<int:pk>/', views.SysOpsSupplyNodeDetail.as_view()),

    
    #Endpoints grouped by UI Views

    #Profile Page

    #Filter Products by metauserIDs
    path('bodega-api/productsByMetaUser/', views.productsByMetaUser),

    #Show MetaUserTags 
    path('bodega-api/metauserTags/', views.MetaUserTagsList.as_view()),
    path('bodega-api/metauserTags/<int:pk>/', views.MetaUserTagsDetail.as_view()),

    #Search MetaUser by MetaUserName 
    path('bodega-api/searchMetaUser/', views.searchMetaUserByName),

    #Fetch All Past Orders of the Metauser.
    path('bodega-api/metauserAllOrders/', views.FetchOrderItemsByMetaUserID),

    #Fetch all past Collaborations by metauserID
    path('bodega-api/yerrr/', views.FetchCollaborationByMetaUserID),

    #Show all notifications 
    path('bodega-api/notifications/', views.notificationsList.as_view()),
    path('bodega-api/notifications/<int:pk>/', views.notificationsDetail.as_view()),

    #Show all notifications by MetaUserID
    path('bodega-api/metauserNotifications/', views.FetchNotificationsByMetaUserID),

    #Search Chat Room by name
    path('bodega-api/searchChatRoom/', views.searchChatRoomByName),

    #Show messages by chatRoomID
    path('bodega-api/messagesChatRoom/', views.messagesByChatRoomID),


]



urlpatterns=format_suffix_patterns(urlpatterns)
