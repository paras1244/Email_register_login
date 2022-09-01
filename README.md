# Explanation
Created Django project test_techblic,
- "rest_framework"   (for REST API creation),
- "rest_framework_simplejwt"   (for Authenticating user),
- "django_rest_passwordreset"   (for sending token for forgot password),
- I use default database.


# I have created two application (users , user_profile)
# users
    - models: CustomeUser model
    - views: Writed APIs for ( register , login , change_password, forgot_password )
    - serializers: Writed Serializers APIs
    - admin: Register the CustomeUser model.

# user_profile
    - model: Created Profile Model
    - views: created ProfileView using "views.APIView"
    - serializers: Writed Related Serializers for ProfileView
    - admin: register the Profile Model to Database

# CustomeUser:
- I have created custome user model with only necesurry fields.
    - User_type and Email

- I have customized the code for create user and createsuperuser,
- on creation of superuser I have passed the User_type = "ADMIN_USER"

# Profile Model:
- I have created Profile model in user_profile.models file,
- I have added ForeignKey of User, to astablish the relationship of user -> Profile

### APIS ###

# user APIS
# Register user     [POST]
http://127.0.0.1:8000/user/register/
(email", "user_type", "password", "password2")

# login API         [POST]
http://127.0.0.1:8000/user/login/
(email, password)

# Change Password (IsAuthenticated)     [PUT]
http://127.0.0.1:8000/user/change_password/<PK>/
("password", "password2", "old_password")

# ( forgot password ) 1) sending-token-by-email. 2) Confirm-token-with-new-password.
# (1) sending-token-by-email=> "django_rest_passwordreset"      [POST]
- For forgoting the password I use "django_rest_passwordreset" module, and writed Signal to send the Token by email.
- for sending the Token by email I use "send_mail"  function "django.core.mail",
http://127.0.0.1:8000/user/forgot_password/     -> this will generate and Send Token on Email.
( email )

# (2) Confirm-token-with-new-password     [POST]
http://127.0.0.1:8000/user/forgot_password/confirm/
( token, Password )


# user_profile APIs
# Create Profile  (IsAuthenticated)  [POST]
http://127.0.0.1:8000/user-profile/profile/
( name, last_name, city, age, designation, exprience)


# Get Profile (IsAuthenticated)    [GET]
http://127.0.0.1:8000/user-profile/profile/

# Update Profile (IsAuthenticated)    [PUT]
http://127.0.0.1:8000/user-profile/profile/



# PostMan Collection
# https://documenter.getpostman.com/view/19442321/VUxNT8yD
Also added Exported file here: postman_doc/test_Django_techBlic.json         (with example)


# Superuser
admintest12@yopmail.com / admin
