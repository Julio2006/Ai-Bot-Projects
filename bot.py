import json
import random

with open ("responses.json", "r") as f:
    chat_bot_data = json.load(f)


def chat_bot():
    while True:
        user_text = input("You: ").lower()
        
        if user_text == "quit":
            break
        
        found_response = None

        for category, data in chat_bot_data.items():
            for trigger in data["triggers"]:
                if trigger in user_text:
                    found_response = random.choice(data["responses"])
                    break
            if found_response:
                break
    
        if found_response:
            print("Bot: ",found_response)
        else:
            print("Bot: I don't know that. Want to teach me? (yes/no)")
            learn_mode = input("You: ").lower()
            if learn_mode == "yes":
                print("Bot: Are you giving me a new category or just a new trigger (c/t)")
                add = input("You: ").lower()
                if add == "c":
                    print("Bot: What is the new Category called?")
                    new_category = input("You: ").lower()
                    if not new_category in chat_bot_data:
                        triggers = []
                        while True:
                            trigger = input("Bot: Enter trigger word (or q to finish): ").lower()
                            if trigger == "q":
                                break
                            triggers.append(trigger)

                        respond = []
                        print("Bot: How should I respond to that? (q to finish)")
                        
                        while True:
                            response = input("Enter bot's response: ").lower()
                            if response == "q":
                                break
                            respond.append(response)
                        
                        chat_bot_data[new_category] = {"triggers": triggers, "responses": respond}
                        with open ("responses.json", "w") as f:
                            json.dump(chat_bot_data, f, indent=4)
                        print("Bot: Got it learned something new!")
                elif add == "quit":
                    break            
                elif add == "t":
                    print("Bot: What category am I adding the trigger to?")
                    cat = input("You: ").lower()
                    if cat in chat_bot_data:
                        print("Bot: What is the trigger word?")
                        new_trig = input("You: ").lower()
                        if new_trig not in chat_bot_data[cat]["triggers"]:
                            chat_bot_data[cat]["triggers"].append(new_trig)
                            with open ("responses.json" ,"w") as f:
                                json.dump(chat_bot_data, f, indent=4)
                            print("Bot: Got it! Learned something new ")
                        else:
                            print("Bot: I already know that trigger!")
            else:
                print("Alright, maybe next time")              
chat_bot()