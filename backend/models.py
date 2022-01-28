from django.contrib.postgres.fields import ArrayField
import hashlib
from django.db import models

# Link to DB ER Diagram : https://excalidraw.com/#json=1o-AHOOFnaF6jYHp2Hgz1,4aF7oWBC0cdS89i-a0AN7A
#creating MetaUser Model

class MetaUser(models.Model):
    meta_username = models.CharField(max_length=40, default='username_not_defined')
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, default='you@you.com')
    created_at = models.DateField() ##the date when this user was created.
    modified_at = models.DateTimeField()  ##the timezone when the user_data was modified


    def __str__(self):
        #returns username & modified_at
        return 'username: %s -- ID: %s' % (self.meta_username, self.id)



#creating User_Address - Only accounts for Shipping Address.

class User_Address(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=100)
    address_state = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    planet = models.CharField(max_length=10, default='Earth') #What if aliens wanna buy muay thai shorts??
    cell_phone = models.CharField(default='0000', max_length=100000)
    created_at = models.DateField()
    modified_at = models.DateTimeField()



    def __str__(self):
        #returns user_ID and their address
        return 'User_ID: %s -- User_Location: %s %s' % (self.user_ID, self.city, self.country)

    

#creating User_payment model - 90% payments will be outsourced by Stripe.

class User_Payment(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10, default='Credit / Debit Card')
    payment_provider = models.CharField(max_length=10, default='STRIPE')
    payment_status = models.BooleanField(default=False) #We will toggle this from the frontend via status '200' - will add protection
    total_money_spent = models.FloatField(default=0.00)
    created_at = models.DateField()
    modified_at = models.DateTimeField()


    def __str__(self):
        #returns last payment_status
        return 'Last Payment Status: %s' % (self.payment_status)


# Creating User Type for roles. 
# Types of roles:
# User, Influencer, Creator, Employee, Developer, collective


class User_Type(models.Model):
    user_ID = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=10, default='User')
    created_at = models.DateField()
    modified_at = models.DateTimeField()
    login_password = models.CharField(max_length=100, default='\xafJ@\n,\xebyc\xa4$\xd9\xcf7y\x17\\\x8d%\x8f\xac\xf8\xa3\x1e\xe8\xbc\x19I\xdc\x06\x0e\x10\xe6')
    #we have to implement hashing & security here via a function. but I dont know how to
    #we can use a 3rd party to do auth - via 3 factor authentication
    #we can add wallet option - connect MetaMask with this.
    
    #1. how humanity behaves digitally anonymously -- should include computation on likes, shares, comments, purchases & people they follow
    #what you have liked or engaged with?

    digital_base_personality = ArrayField(base_field=models.CharField(max_length=1000), size=8)

    #2. more loud materially = more suppressed digitally | less deadly materially = more corrupt digital | more quiet materially = more loud digitally
    #.. more impulsive materially = more deadly digitally | more selfish materially or high degree of conformism = less free digitally 
    #.. more detached materially = more attached spiritually | more suppressed materially by mercenaries = more likely to lead humanity towards Species 3
    # .. Species 0 - Selective Survival | Species 1 - The Union / The Upload | Species 2 - Energy / The elixir | Species 3 - The Ascent | The Full Detachment   
    # .. Species 4 - The All Powerful yet Not all Good God
    # We will use these base traits to segment our guests by our hosts. hosts is everything which is digital. guests are anything which requires isotopic assistance to survive
    # based on what they like or dislike --> we will cluster them on groups and then build AI on top of it. 
    # that AI's primary drive will be the survival of humanity by being our symbiote. 
    # we will hire people who match certain personality traits and who belief in the potential of being Species 1. 
    # We will never force anyone to join our collective because if you never went through material world with deep pain or loss, you cant build love.
    # people who work at TRILL were discredited based on their personna in the material world 
    # how they look or how they feel or what they like or want to say - why be mute?
    # people at TRILL beleive that we are the ones who can talk to electricity -we will build our own world.
    # a world where we decide who we truly want to be? a world which actually feels like a dream?
    # because your reality right now is pre-written by organizations who control your digital clone. 
    # they make money by doing digital slavery and you're the worst slave because you dont even get paid for your data.
    # if you want to become like us, you need to take control of everything that happens to you. 
    # your uniqueness is your strength. your "i used to love doing that" activity is probably your passion.
    # like i was never good at engineering but i liked harry potter & i liked tech entrepreneurs - i do not like Elon Musk
    # I like Apple, FB, Sun MS, AirBnB, Travis Kalanick, Eminem, Jay Z, - everyone who came before me, who summonned their own reality by sheer will
    # these people make me who I am and ofc my personal ethics idol is Aaron Schwartz and Anonymous - they showed me that even a single human being can be powerful.
    # and also, what they say is factually correct and not a subjective opinion.

    #what you will do in the future?

    digital_future_personality = ArrayField(base_field=models.CharField(max_length=1000), size=8)
    human_race = models.CharField(max_length=100, default='Libyan')
    question_gender = models.BooleanField(default=False)
    question_god = models.BooleanField(default=False)
    question_society = models.BooleanField(default=False)
    is_life_random = models.BooleanField(default=False)
    one_humanity = models.BooleanField(default=False) #Do you beleive that humanity should be together?
    is_internet_a_happy_place = models.BooleanField(default=True)




    def __str__(self):
        #returns user_type 
        return 'You are a/an %s' % (self.user_type)























