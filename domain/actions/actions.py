from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction, EntityFormField
from rasa_core.events import AllSlotsReset
from rasa_core.events import SlotSet
from random import choice
from uuid import uuid4
from string import punctuation

class ActionRegisterCandidate(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        # no need for candidate username and password here, we auto generate it for them. Fix it if you want
        return [
            EntityFormField("candidateName", "candidateName"),
            EntityFormField("candidateNumber", "candidateNumber"),
            EntityFormField("center_number", "center_number"),
            EntityFormField("candidateLevel", "candidateLevel"),
            EntityFormField("candidateBirth", "candidateBirth"),
            EntityFormField("gender", "gender"),
            EntityFormField("seat", "seat"),
            EntityFormField("year", "year")
        ]

    def name(self):
        return "action_register_candidate"

    def submit(self, dispatcher, tracker, domain):
        # construct and return candidate dict
        candidateDict        = CandidateRegister(tracker)
        Cusername, Cpassword = CandidateCredentials(candidateDict.get("Cname"))
        # TODO: Register candidate to database
        # TODO: Since pswd and username is auto generated, save to db too and show it to user

        debugMsg(candidateDict)

        resp = "You are now registered. Use the following details to login to your ZIMSEC portal\nUsername: {cuser}\nPassword: {pwd}".format(cuser=Cusername, pwd=Cpassword)
        dispatcher.utter_message(resp)            # show user auto generated credentials

        dispatcher.utter_template(template="utter_proceed_login")

        # reset everything on successful candidate register
        return [AllSlotsReset()]

class ActionLoginCandidate(FormAction):
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("username", "username"),
            EntityFormField("password", "password")
        ]

    def name(self):
        return "action_login_candidate"

    def submit(self, dispatcher, tracker, domain):
        # collect required data from slots
        Cusername = tracker.get_slot("username")
        Cpassword = tracker.get_slot("password")

        debugMsg(Cusername)
        debugMsg(Cpassword)

        # TODO Query database to login candidate
        results = ""
        dispatcher.utter_message("Checking for candidate with username `{username_}`..".format(username_=Cusername))

        # can either get candidate results now or create another action for candidates results
        # `ActionGetResults class` | `action_get_candidates_results`
        dispatcher.utter_message("Login successful!")

        # TODO: Get results from database, and format it to suite the channel used (FB)
        results = "English      A\nMaths        A\nHistory      B\nPhysics      A\nChemistry    B\nAccounts     C\n\nSubjects: 6. Passes: 6"
        dispatcher.utter_message(results)

        # prompt for .pdf results file or any file
        dispatcher.utter_template(template="utter_ask_file_results")

        # flag to true on successful login via 1 / 0
        return [SlotSet("loggedIn", '1'), SlotSet("candidate_results", results)]

        # flag to true on successful login via 1 / 0
        #return [SlotSet("loggedIn", '1')]

class ActionHandleForgetDetails(Action):
    # TODO: Might need to implement a FormAction here to capture all required info
    def name(self):
        return "action_handle_forget_details"

    def run(self, dispatcher, tracker, domain):
        # implement handling forgotten details
        pass

class ActionPromptForgetCandidateDetails(Action):
    def name(self):
        return "action_prompt_forget_details"

    def run(self, dispatcher, tracker, domain):
        # prompt candidate if they forgot their details
        resp = "Forgot your login details?"
        confirm_button = [
            {
                'title': 'Forgot details',
                'payload': 'yes'
            },

            {
                'title': 'No, proceed',
                'payload': 'no'
            }]

        dispatcher.utter_button_message(text=resp, buttons=confirm_button)

class ActionGetResults(Action):
    def name(self):
        return "action_get_candidate_results"

    def run(self, dispatcher, tracker, domain):
        # check if there was successful candidate login
        isLogged = tracker.get_slot("loggedIn")
        Cusernam = tracker.get_slot("username")

        debugMsg(isLogged)
        debugMsg(Cusernam)

        '''
        if isLogged == '1':
            dispatcher.utter_message("Login successful!")
            # TODO: Get results from database, and format it to suite the channel used (FB)
            #results = "<db-query>"
            results = "English\t\t\tA\nMaths\t\t\tA\nHistory\t\t\tB\nPhysics\t\t\tA\nChemistry\t\t\tB\nAccounts\t\t\tC"
            dispatcher.utter_message(results)

            # prompt for .pdf results file
            dispatcher.utter_template(template="utter_ask_file_results")

            return [SlotSet("candidate_results", results)]

        else:
            # TODO: Ofcourse do something about it
            dispatcher.utter_message("Could not find candidate with username `{username_}`".format(username_=Cusernam))
        '''
        pass

class ActionSendFileResults(Action):
    def name(self):
        return "action_send_results_file"

    def run(self, dispatcher, tracker, domain):
        # check again if user is logged in, just in case
        isLogged = tracker.get_slot("loggedIn")
        Cresults = tracker.get_slot("candidate_results")
        debugMsg(isLogged)

        if isLogged == '1' and Cresults:
            # TODO: Create a file of candidate result in any meaningful format
            debugMsg(Cresults)

            # attachmentResult = "<converted-file>"
            attachmentResult = "https://i2.wp.com/zimtrending.co.zw/wp-content/uploads/2020/01/WhatsApp-Image-2020-01-17-at-5.00.04-PM.jpeg"  # demo image file
            dispatcher.utter_attachment(attachment=attachmentResult)

        # it should be the end of a conversation now, we hope. So reset everything yoh!
        return [AllSlotsReset()]

# utils
def CandidateRegister(tracker_obj):
    # param:  tracker
    # return: candidate dict
    tracker   = tracker_obj
    candidate = {}

    candidate['Cname']      = tracker.get_slot("candidateName")
    candidate['Cnumber']    = tracker.get_slot("candidateNumber")
    candidate['Cntrnumber'] = tracker.get_slot("center_number")
    candidate['Clevel']     = tracker.get_slot("candidateLevel")
    candidate['Cbirth']     = tracker.get_slot("candidateBirth")
    candidate['Cgender']    = tracker.get_slot("gender")
    candidate['Cseat']      = tracker.get_slot("seat")
    candidate['year']       = tracker.get_slot("year")

    return  candidate

def CandidateCredentials(Cname):
    # randomize candidate info to create username and password for them, automatically
    fullNameSplit     = Cname.split(' ')
    CandidateUsername = "zimsec" + fullNameSplit[0].title() + fullNameSplit[1].title() + str(uuid4().int)[:2]
    CandidatePassword = "$" + fullNameSplit[1].title() + str(uuid4().int)[:3] + fullNameSplit[0].title() + choice(punctuation)
    return CandidateUsername, CandidatePassword

def debugMsg(mesg):
    # TODO: Should use logging not this lame way
    #print("[INFO]: ", mesg)
    pass
