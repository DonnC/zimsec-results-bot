'''
 * run server first with command:
    python3.6 -m rasa_core.server -d ./models/dialogue -u ./models/zimsec_bot/default/nlu --debug -o out.log --cors *
'''

import requests as req
from pprint import pprint

def bot_chat(msg, user_id):
    user_msg = '{"query": "%s"}' %(msg)
    url = "http://localhost:5005/conversations/{sender_id}/respond".format(sender_id=user_id)

    try:
        resp = req.post(url, data=user_msg)
        reply = resp.json()
        print("[INFO] Respond")
        pprint(reply)

        if len(reply) != 1 and len(reply) > 1:
            bot_response = ""
            for data in reply:
                #print(data)
                bot_response += data.get("text") + "\n"


        elif len(reply) == 1:
            bot_response = reply[0]["text"]

        else:
            pprint(reply)
            bot_response = "sorry, i can't process that at the moment. Can you try something else"

    except:
        bot_response = "Oops. I couldn't reach my server!"

    return  bot_response

# ########## debug #################
while True:
    f = input("USER: ")
    print("BOT: ", bot_chat(f, "donny"))