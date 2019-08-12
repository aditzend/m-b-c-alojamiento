# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import json
from datetime import datetime
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
# Lista de parametros que el bot necesita parsear de lo que manda el ChatServer
neededParams = ['InteractionId', 'UserName', 'UserMail', 'MimeType', 'Parameters', 'user.mail', 'user.name']

class bcolors:
    HEADER = '\033[95m'
    INFO = '\033[0;37;44m INFO \033[0m'
    WARNING = '\033[0;37;43m WARNING \033[0m'
    ERROR = '\033[0;37;41m ERROR \033[0m'
    ORIGIN = '\033[3;34;40m'
    OBJECT = '\033[1;35;40m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ActionHelloWorld(Action):
#
    def name(self) -> Text:
        return "action_hello_world"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        dispatcher.utter_message("Hello World!")

        return []





class ActionParseContext(Action):
#
    def name(self) -> Text:
        return "action_parse_context"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        stringJson = (tracker.latest_message)['text'].split('>>> ')[1]
        parsedJson = json.loads(stringJson)
        res = []
        # res.append(SlotSet("InteractionId", parsedJson["InteractionId"]))
        for (k,v) in parsedJson.items():
                # print('%s : %s \n' % (k,v) )
                # instruction = 'SlotSet("%s", parsedJSON["%s"])' % (k,k)
                if k in neededParams :
                        if k == 'Parameters' :
                                for pair in parsedJson['Parameters'] :
                                        ls = pair.split('=')
                                        if ls[0] in neededParams :
                                                instruction = SlotSet(ls[0], ls[1])
                                                res.append(instruction)
                                        else : 
                                                now = datetime.now()
                                                dt_string = now.strftime("%Y-%m-%d %H:%M:%S.%f")
                                                print(dt_string + " " + bcolors.WARNING + bcolors.ORIGIN + '   ActionParseContext   ' + bcolors.OBJECT + ls[0] + bcolors.ENDC + ' received but not needed.')
                

                        else :
                                instruction = SlotSet(k, parsedJson[k])
                                res.append(instruction)
                else :
                        now = datetime.now()
                        dt_string = now.strftime("%Y-%m-%d %H:%M:%S.%f")
                        print(dt_string + " " + bcolors.WARNING + bcolors.ORIGIN + '   ActionParseContext   ' + bcolors.OBJECT + k + bcolors.ENDC + ' received but not needed.')
                
        
        # print (*res, sep = ", ")

        return res
        
        # return [
        #         SlotSet("InteractionId", parsedJson["InteractionId"]),
        #         SlotSet("UserName", parsedJson["UserName"])
        #         ]

class ActionEcho(Action):
#
    def name(self) -> Text:
        return "action_echo"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        dispatcher.utter_message("Echo")

        return []
