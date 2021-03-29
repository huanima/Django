from django.urls import path
from mgr import customer,order
from mgr.sign_in_out import signIn, signOut

urlpatterns = [
   path('customers', customer.dispatcher),
   path('signin', signIn),
   path('signout', signOut),
   path('order', customer.dispatcher),

]