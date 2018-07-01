#1
a = "An access token is an object that describes the security context of a process or thread.\n"
b = "The information in a token includes the identity and privileges of the user account associated with the process or thread.\n"
c = "access_token = 3417824385-Q0NKEsxDVUeYnSxA5667Q6X53khx8k2mv0DfXSP\n"
print(a,b,c)


#2
import socket

addr1 = socket.getaddrinfo('localhost', 8080)
print(addr1)


#3
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy

oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token,access_secret)
api = tweepy.API(oauth)
print(api.search("#sanju"))


#4
a = "A lbrary is a collection of software that IMPLEMENTS an API.\n"
b = "The 'API' is a description of the interface between an application program and a library.\n "
c = "Example: OpenGL is a 'library' and the API for it is defined in the OpenGL specification.\n"
print(a,b,c)

