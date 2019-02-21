# custom actions for our chatbot
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction, EntityFormField
from rasa_core.events import SlotSet
import time
import random
import os
from os import path

root_dir = "/home/donald/Projects/Python36/rasa bots/nust_tour_guide_OLD"
map_dir = path.join(root_dir, "maps")

class ActionBuildingDirection(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [EntityFormField("building", "building")]

    def name(self):
        return "action_building_direction"

    def submit(self, dispatcher, tracker, domain):
        building_name = str(tracker.get_slot("building"))

        directions = ['Go straight and turn right. first building ', 'Face left, blue roof building is the one you are looking for', 'The building with a national flag only on top of it is the one']

        building_direction = random.choice(directions)
        building_name = building_name.replace(" ", "_")
        maps_dir = ["http://i.stack.imgur.com/aKOf1.png", "https://i.stack.imgur.com/FNUTu.png", "https://i.stack.imgur.com/tGnyQ.png",
                    "https://i.stack.imgur.com/f3iHm.png", "https://i.stack.imgur.com/imRDs.png", "https://developers.google.com/maps/documentation/android-sdk/images/utility-markercluster-simple.png"]
        building_image_map = random.choice(maps_dir)

        # utter response message and then map image
        dispatcher.utter_template("utter_response", building_directions = building_direction)
        #time.sleep(0.2)
        resp = {"image": building_image_map, "text": "You can also follow along this map."}
        dispatcher.utter_response(resp)

        ret = "[{}]: {}".format(building_name, building_direction)
        return [SlotSet('results', ret)]

'''
class ActionLecturerDirection(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("lecturer", "lecturer"),
            EntityFormField("lec_dpt", "lec_dpt")]

    def name(self):
        return "action_lecturer_direction"

    def submit(self, dispatcher, tracker, domain):
        lecturer_name = tracker.get_slot('lecturer')
        lecturer_dept = tracker.get_slot('lec_dpt')

        directions = ['Ok you can find the lecturer at Admin Block. Left wing First floor room 47',\
                      'Go to the Chemical Engineering building. Ground floor left side. First office # 01',\
                      'Heard to the faculty of Commerce building. Take the elevator to third floor (Last floor). The first office you face is the one. Door 21']
        dispatcher.utter_message(random.choice(directions))

class ActionButtons(Action):
    # utter message with custom buttons

    def name(self):
        return "action_buttons"

    def run(self, dispatcher, tracker, domain):
        # buttons is a list of tuples: [(option_name,payload)]
        custom_button = [
            {
                'title': 'Button1',
                'payload': 'button'
                },

            {
                'title': 'Button2',
                'payload': 'button'
            },

            {	'title': 'Button3',
                     'payload': 'button'
                 }
        ]

        dispatcher.utter_button_message(text="Select an option", buttons=custom_button)
'''
