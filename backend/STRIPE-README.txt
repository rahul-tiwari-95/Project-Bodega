This documentation lists all the required information for navigating through my complex backend <> stripe integration.


STRIPE BODEGA MERCHANT INFO.

1. Creation of Stripe Account & Fetching StripeAccountInfo data via MetaUserID
URL: /bodegaCreators/stripeAccount/
Table name: StripeAccountInfo 
Details: Lists stripeAccountID which is required to pay merchants from Bodega's Stripe Balance.This table uses MetaUserID as a foreignKey.

URL: /bodegaCreators/fetchStripeAccountByMetaUserID/ - Fetch StripeAccount By MetaUserID --> returns stripeAccountInfo Table Instance.

