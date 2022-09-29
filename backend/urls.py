from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views
from .views import *
#import stripeServer.views as stripeViews
urlpatterns = [
    # Landing Page URLs
    path('oldhome/', views.home_page),
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
    path('bodegaCreators/stripeAccountInfo/', views.StripeAccountInfoList.as_view()),
    path('bodegaCreators/stripeAccountInfo/<int:pk>/', views.StripeAccountInfoDetail.as_view()),

    #Fetch stripeAccountInfoID via MetaUserID 
    path('bodegaCreators/fetchStripeAccountByMetaUserID/', views.fetchStripeAccountInfoByMetaUserID),

    #Create Fund Transfer to Eligible Stripe Account
    path('bodegaCreators/createPayoutTransfer/', views.payoutStripeAccount),
    path('bodegaCreators/stripeTransfer/', views.StripeAccountTransferList.as_view()),
    path('bodegaCreators/stripeTransfer/<int:pk>/', views.StripeAccountTransferDetail.as_view()),

    #Yerrr / Collaboration API Endpoint
    #Yerrr Payout by Commission % on Sales
    path('bodegaCreators/yerrrCommission/', views.yerrrCommissionPayout),
    path('bodegaCreators/yerrrFixed/', views.yerrrFixedPayout),
    
    path('bodegaCreators/createPayoutTransfer/', views.payoutStripeAccount),
    #Stripe Endpoint to list all transfers
    path('bodegaCreators/allStripeTransfers/', views.allStripeTransfers), #STRIPE SPECIFIC
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

    #UnSubscribe URL
    path('bodegaCreators/unsubscribe/', views.unsubscribe),

    #All Stripe Merchant SubscriptionsList
    path('bodegaCreators/allSubscriptions/', views.creatorSubscriptionList.as_view()),
    path('bodegaCreators/allSubscriptions/<int:pk>/', views.creatorSubscriptionDetail.as_view()),

    path('bodegaCreators/filterMerchantSubscriptions/', views.filterCreatorSubscriptionsByMetaUser),

    #All Stripe Customer Subscriptions
    path('bodegaCreators/customerSubscriptions/', views.subscribersList.as_view()),
    path('bodegaCreators/customerSubscriptions/<int:pk>/', views.subscribersDetail.as_view()),

    #Filter customer subscriptions by metauserID
    path('bodegaCreators/filterCustomerSubscriptions/', views.filterCustomerSubscriptionsByMetaUser),

    #URLs for Merchant / Creator Cash Flow Ledger Details 
    path('bodegaCreators/cashFlow/', views.CashFlowLedgerList.as_view()),
    path('bodegaCreators/cashFlow/<int:pk>/', views.CashFlowLedgerDetail.as_view()),

    #Fetch CashFlow via stripeAccountInfoID
    path('bodegaCreators/merchantCashFlow/', views.fetchCashFlowLedger),

    #Fetch CashFlow via bodegaCustomerID
    path('bodegaCreators/merchantCashFlowBodegaCustomer/', views.fetchCashFlowLedgerBodegaCustomer),

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
    path('bodega-api/metauser_chat_room/', views.BodegaServerList.as_view()),
    path('bodega-api/metauser_chat_room/<int:pk>/', views.BodegaServerDetail.as_view()),
    
    # Particpant Model  Endpoint by Chat Room ID
    path('bodega-api/participant/', views.ParticipantList.as_view()),
    path('bodega-api/participant/<int:pk>/', views.ParticpiantDetail.as_view()),
    path('bodega-api/BodegaServersByMetauserID/', views.FetchParticipantByMetaUserID),
    path('bodega-api/BodegaServersByChatRoomID/', views.FetchParticipantByChatRoomID),
    path('bodega-api/BodegaServerAuth/<int:pk>/', views.AuthenticateParticipantByRoomHashkey),

    #Filtering BodegaServer by metauserIDs
    path('bodega-api/filterBodegaServerByMetaUserID/', views.filterBodegaServerByMetaUserID),
    #Filtering messages by BodegaServer ID
    path('bodega-api/filterMessagesReverseLookup/', views.filterMessagesReverseLookup),

    # Message Model Endpoint by messageID
    path('bodega-api/message/', views.MessageList.as_view()),
    path('bodega-api/message/<int:pk>/', views.MessageDetail.as_view()),
    # Product Category Model Endpoint by messageID
    path('bodega-api/product_category/', views.ProductCategoryList.as_view()),
    path('bodega-api/product_category/<int:pk>/', views.ProductCategoryDetail.as_view()),

    path('bodega-api/product_inventory/', views.ProductInventoryList.as_view()),
    path('bodega-api/product_inventory/<int:pk>/', views.ProductInventoryDetail.as_view()),

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
    # Order failure Endpoints
    path('bodega-api/orderFailure/', views.OrderFailureList.as_view()),
    path('bodega-api/orderFailure/<int:pk>/', views.OrderFailureDetail.as_view()),

    #Order Ledger Endpoint
    path('bodega-api/orderLedger/', views.OrderLedgerList.as_view()),
    path('bodega-api/orderLedger/<int:pk>/', views.OrderLedgerDetail.as_view()),

    #Filtering Order Ledger by metauserID
    path('bodega-api/orderLedgerMetaUser/', views.filterOrderLedgerByMetauserID),
    path('bodega-api/orderLedgerStripeAccount/', views.filterOrderLedgerByStripeaccountID),

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
    
    #Endpoints grouped by UI Views
    #Profile Page
    #Filter Products by metauserIDs
    path('bodega-api/productsByMetaUser/', views.productsByMetaUser),
    #Show MetaUserTags 
    path('bodega-api/metauserTags/', views.MetaUserTagsList.as_view()),
    path('bodega-api/metauserTags/<int:pk>/', views.MetaUserTagsDetail.as_view()),

    path('bodega-api/filterMetaUserTags/', views.filterTagsByMetaUserID),
    
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
    path('bodega-api/searchBodegaServer/', views.searchBodegaServerByName),
    #Show messages by BodegaServerID
    path('bodega-api/messagesBodegaServer/', views.messagesByBodegaServerID),

    path('bodega-api/productsBoostTags/', views.FetchBoostTagsByProductID),

    path('bodega-api/adityaMetauser/', views.fetchMetaUserIDTest),




    path('bodega-api/metauserSocial/', views.metaUserSocialList.as_view()),
    path('bodega-api/metauserSocial/<int:pk>/', views.metaUserSocialDetail.as_view()),
    path('bodega-api/socialMetaUser/', views.fetchSocialByMetaUserID),

    #Generate Label URL 
    path('bodega-api/generateLabel/', views.generateLabel),

    #bodega Customer Support endpoint
    path('bodega-api/bodegaCustomer/', views.bodegaCustomerList.as_view()),
    path('bodega-api/bodegaCustomer/<int:pk>/', views.bodegaCustomerDetail.as_view()),


    #Website Builder APIs

    #ContentPage Endpoint
    path('bodegaCreators/contentPage/', views.contentPageList.as_view()),
    path('bodegaCreators/contentPage/<int:pk>/', views.contentPageDetail.as_view()),

    #CollectionPage Endpoint
    path('bodegaCreators/collectionPage/', views.collectionPageList.as_view()),
    path('bodegaCreators/collectionPage/<int:pk>/', views.collectionPageDetail.as_view()),

    #Text Page Endpoint
    path('bodegaCreators/textPage/', views.textPageList.as_view()),
    path('bodegaCreators/textPage/<int:pk>/', views.textPageDetail.as_view()),

    #navigationBar Endpoint
    path('bodegaCreators/navBar/', views.navigationBarList.as_view()),
    path('bodegaCreators/navBar/<int:pk>/', views.navigationBarDetail.as_view()),

    #Footerbar Endpoint
    path('bodegaCreators/footerBar/', views.footerBarList.as_view()),
    path('bodegaCreators/footerBar/<int:pk>/', views.footerBarDetail.as_view()),

    #websiteMapConfig Endpoint
    path('bodegaCreators/siteMap/', views.websiteSiteMapConfigList.as_view()),
    path('bodegaCreators/siteMap/<int:pk>/', views.websiteSiteMapConfigDetail.as_view()),

    #Filtering CollectionPage by collectionID
    path('bodegaCreators/filterCollectionPage/', views.filterCollectionPageByCollectionID),

    #Filtering websiteMapConfig by metauserIDs
    path('bodegaCreators/filterSiteMap/', views.websiteSiteMapConfigByMetaUserID),
    path('bodegaCreators/filterSiteMapByContentPageID/', views.filterSiteMapByContentPageID),

    path('bodegaCreators/filterProductCategory/', views.filterProductCategory),
    path('bodegaCreators/filterProductCollection/', views.filterProductsByCollectionID),

    #Collection APIs
    path('bodegaCreators/collections/', views.collectionList.as_view()),
    path('bodegaCreators/collections/<int:pk>/', views.collectionDetail.as_view()),


    path('bodega-api/metauserAccountStatus/', views.MetaUserAccountStatusList.as_view()),
    path('bodega-api/metauserAccountStatus/<int:pk>/', views.MetaUserAccountStatusDetail.as_view()),
    path('bodega-api/filtermetauserAccountStatus/', views.filterMetaUserAccountStatusByMetaUserID),

    path('bodega-api/yerrrByCollaborator/', views.filterYerrrByCollaborator),
    path('bodega-api/yerrrByOwner/', views.filterYerrrByOwner),

    path('bodegaCreators/filterContentPageByMetaUserID/', views.filterContentPageByMetaUserID),

    #Newsletter Endpoints
    path('bodegaCreators/newsletter/', views.NewsletterList.as_view()),
    path('bodegaCreators/newsletter/<int:pk>/', views.NewsletterDetail.as_view()),

    #Newsletter Subscriber Endpoints
    path('bodegaCreators/newsletterSubscriber/', views.NewsletterSubscribersList.as_view()),
    path('bodegaCreators/newsletterSubscriber/<int:pk>/', views.NewsletterSubscribersDetail.as_view()),

    path('bodegaCreators/filterNewsletterMetaUserID/', views.filterNewsLetterByMetaUserID),
    path('bodegaCreators/filterNewsletterSubscriberByNewsletterID/', views.filterNewsletterSubscriberByNewsletterID),
    path('bodegaCreators/filterNewsletterSubscriberByMetaUserID/', views.filterNewsletterSubscriberByMetaUserID),

    #Filtering Collection By MetaUserID
    path('bodegaCreators/filterCollectionByMetaUserID/', views.filterCollectionByMetaUserID),

    #Filtering UserAddress by metauserID
    path('bodegaCreators/filterUserAddressByMetaUserID/', views.filterUserAddressByMetaUserID),

    #Filtering Product Inventory by productID
    path('bodega-api/filterProductInventoryByProductID/', views.filterProductInventoryByProductID),


    #Search Endpoints
    path('bodega-api/productSearch/', views.searchProductName),
    path('bodega-api/metauserHashkeySearch/', views.searchMetaUserByPublicHashkey),
    path('bodega-api/boostTagsSearch/', views.searchBoostTagsByName),
    path('bodega-api/bodegaServerSearch/', views.searchBodegaServerByName),

    #filter messages by metauserIDs
    path('bodega-api/filterMessageByMetaUserID/', views.filterMessageByMetaUser),


    #Filter creator Subscriptions by priceID
    path('bodegaCreators/filterCreatorSubsByPriceID/', views.filterCreatorSubscriptionByPriceID),
    path('bodegaCreators/filterSubsByPriceID/', views.filterSubscribersByShopID),

    #Filter OrderDetail by Order_ID
    path('bodega-api/filterOrderDetail/', views.filterOrderItemsByOrderID),

    #Filter customer payment by metauserIDs
    path('bodegaCreators/filterCustomerPayment/', views.filterCustomerPaymentByMetaUserID),

    #BodegaCreditCardLedger URLs
    path('bodegaCreditCardLedger/', views.BodegaCreditCardLedgerList.as_view()),
    path('bodegaCreditCardLedger/<int:pk>/', views.BodegaCreditCardLedgerDetail.as_view()),
    path('filterCreditCardLedger/', views.filterCreditCardLedgerByMetaUserID),


    #BodegaSubscriberLedger URLs
    path('bodegaSubscriberLedger/', views.BodegaSubscriberLedgerList.as_view()),
    path('bodegaSubscriberLedger/<int:pk>/', views.BodegaSubscriberLedgerDetail.as_view()),
    path('filterSubscriberLedger/', views.filterSubscriberLedgerByMetaUserID),


    #BodegaPublicURL 
    path('bodegaPublicURL/', views.BodegaPublicURLList.as_view()),
    path('bodegaPublicURL/<int:pk>/', views.BodegaPublicURLDetail.as_view()),
    path('filterPublicURL/', views.filterBodegaPublicURLByMetaUserID),

    #Memories
    path('bodegaMemories/', views.MemoriesList.as_view()),
    path('bodegaMemories/<int:pk>/', views.MemoriesDetail.as_view()),
    path('filterMemories/', views.filterMemoriesByMetaUserID),

    path('MUPA/', views.productHashkeyByMetaUser),
]
urlpatterns=format_suffix_patterns(urlpatterns)