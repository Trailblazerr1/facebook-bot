from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
import json, requests, random, re
from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
msgs = {
	'pushpender' :["Abhi bhi tym hai s*** k paas chala jaa",
	"Tu rahega c**** ka c*** hi",
	"Bhai, S**ha se raakhi bandhwa lena is baar"],

	'ayush' :["kutte ",
	"Abe *** ko to sid le gya to kya 3 saal ghanti baja",
	"mote hatthi"],

	'aseem' :["Honestly, Aseem tu mota hota jaa rha h",
	"Abe AB nhi mili to kya koi aur mil jayegi",
	"NSIT Delhi"],

	'abhishek' :["Abhishek mere bhai",
	"Abe, kitni ladkiyon ko frnd req bhejaga",
	"Bas chutiya bana tu, aur kuch to hona nhi tujhse"],

	'arun' :["G*** sirf teri h mere bhai",
	"Om sir ko mil kar maarange",
	"Arun b*"],

	'anurag' : ["I am loyal to my GOD"]
}

def post_facebook_message(fbid, recevied_message):
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    print("start\n")
    pprint(tokens)
    print("stop\n")
    joke_text = ''
    for token in tokens:
        if token in msgs:
            joke_text = random.choice(msgs[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send ur name bc!"

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'token'
    joke_text = 'Abe '+user_details['first_name']+'..!' + joke_text

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=token' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())
# Create your views here.
class botview(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'any no':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message) 
                    post_facebook_message(message['sender']['id'], message['message']['text'])    
        return HttpResponse()
