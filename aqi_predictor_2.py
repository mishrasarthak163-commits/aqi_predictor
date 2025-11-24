import time

def begin_talking():
    print("\nWell hello there!")
    time.sleep(1.2)
    print("I was sitting here thinking about air quality...")
    time.sleep(1.5)
    print("Funny how we breathe all day but rarely stop to think about what's in the air.")
    time.sleep(1.8)
    print("Anyway, I made this little helper to sort through the numbers.")
    print(" ")

def ask_about_current_air():
    print("So what's happening with your air right now?")
    print(" ")
    
    print("First up - those invisible tiny particles.")
    print("You know, the ones you can't see but can sometimes feel?")
    print("Like:")
    print("  • Crystal clear mountain air might be around 5-15")
    print("  • Your average Tuesday in the city: 25-55")
    print("  • When the air feels thick: 65 or above")
    
    got_it = False
    tiny_particles = 0
    while not got_it:
        user_says = input("\nWhat number comes to mind? ")
        try:
            tiny_particles = float(user_says)
            if tiny_particles > 200:
                print("Whoa, that seems really high! Maybe double check?")
                continue
            got_it = True
        except:
            print("Hmm, that didn't work. Maybe try something like 30?")
    
    print(" ")
    print("Now what about visible dust?")
    print("Like dust on your furniture or floating in sunlight?")
    print("For instance:")
    print("  • Almost no dust visible: 10-35")
    print("  • Normal dust levels: 40-85") 
    print("  • Definitely dusty: 95 or higher")
    
    got_dust = False
    dust_particles = 0
    while not got_dust:
        user_dust = input("\nWhat's your best guess here? ")
        try:
            dust_particles = float(user_dust)
            if dust_particles > 300:
                print("That seems quite high - are you in a dust storm?")
                continue
            got_dust = True
        except:
            print("Let's try that again - maybe 50 or 60?")

    return tiny_particles, dust_particles

def make_sense_of_air(tiny, dust):
    # My homemade way of understanding these numbers
    overall_air_score = (tiny * 1.8) + (dust * 0.6) + 5
    
    if overall_air_score < 45:
        return {
            'score': overall_air_score,
            'summary': "Absolutely beautiful air! 🌈",
            'explanation': "The air quality is fantastic today - what a treat!",
            'personal_take': "I'd be outside enjoying this if I were you.",
            'expression': "😊",
            'sensation': "like that first clean breath after rain",
            'recommendations': "• Go for a nice long walk\n• Perfect for outdoor exercise\n• Open up the windows and enjoy"
        }
    elif overall_air_score < 95:
        return {
            'score': overall_air_score,
            'summary': "Pretty decent air ☀️",
            'explanation': "The air is totally fine for pretty much everyone.",
            'personal_take': "No need to change any plans because of the air today.",
            'expression': "🙂",
            'sensation': "like your average comfortable day",
            'recommendations': "• Your normal outdoor stuff\n• Gardening would be nice\n• Nothing to worry about here"
        }
    elif overall_air_score < 145:
        return {
            'score': overall_air_score,
            'summary': "Air's not bad but not great 🎗️",
            'explanation': "People with breathing stuff might want to take it easy.",
            'personal_take': "Maybe don't push too hard if you have asthma or allergies.",
            'expression': "😐",
            'sensation': "a bit heavy, like the air before summer rain",
            'recommendations': "• Keep outdoor time reasonable\n• Indoor activities work well\n• Sensitive people should rest up"
        }
    elif overall_air_score < 185:
        return {
            'score': overall_air_score,
            'summary': "Air could use some improvement 😷",
            'explanation': "Most folks will notice the air isn't great today.",
            'personal_take': "Might want to save the heavy outdoor work for another day.",
            'expression': "😷",
            'sensation': "like you're downwind from a bonfire",
            'recommendations': "• Better to stay inside mostly\n• Air filters help if you have them\n• Take things easy today"
        }
    else:
        return {
            'score': overall_air_score,
            'summary': "Really poor air quality 💀",
            'explanation': "This air could be tough on everyone's breathing.",
            'personal_take': "Seriously consider staying indoors if you can.",
            'expression': "💀",
            'sensation': "like thick smoke that's hard to breathe",
            'recommendations': "• Definitely stay indoors\n• Use air purifiers if available\n• Avoid any outdoor activity"
        }

def share_my_thoughts(air_details):
    print(" ")
    print("Okay, so here's my take on your air situation...")
    time.sleep(2.5)
    
    print(" ")
    print("—" * 25)
    print(f"   {air_details['expression']}  {air_details['summary']}")
    print("—" * 25)
    
    time.sleep(1.3)
    print(f"Overall air number: {air_details['score']:.0f}")
    
    time.sleep(1.7)
    print(" ")
    print(f"My read: {air_details['explanation']}")
    print(f"To me it feels {air_details['sensation']}.")
    
    time.sleep(1.5)
    print(" ")
    print(f"Personal opinion: {air_details['personal_take']}")
    
    time.sleep(1.8)
    print(" ")
    print("Some things that might work well today:")
    print(air_details['recommendations'])
    
    # Little personal note
    if air_details['score'] < 45:
        print(" ")
        print("What gorgeous air! Make the most of it! 🌞")
    elif air_details['score'] < 95:
        print(" ")
        print("Hope your day is as nice as the air! ☀️")
    else:
        print(" ")
        print("Look after yourself today! 💝")

def demonstrate_with_examples():
    print(" ")
    print("Just to give you the general idea, here are some scenarios:")
    print(" ")
    
    example_days = [
        {"situation": "Fresh mountain hike", "tiny_num": 8, "dust_num": 15},
        {"situation": "Regular neighborhood walk", "tiny_num": 28, "dust_num": 45},
        {"situation": "Busy downtown area", "tiny_num": 58, "dust_num": 90},
        {"situation": "Industrial area or heavy traffic", "tiny_num": 82, "dust_num": 130}
    ]
    
    for example in example_days:
        air_thoughts = make_sense_of_air(example['tiny_num'], example['dust_num'])
        print(f"• {example['situation']}: {air_thoughts['expression']} {air_thoughts['summary']}")
        time.sleep(1.2)

def say_goodbye():
    print(" ")
    print("•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•")
    print("Thanks for thinking about air quality today!")
    print("It's one of those things we should notice more often.")
    print("Here's to good air and easy breathing! 🌬️")
    print("•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•~•")

def run_the_program():
    # Start our conversation
    begin_talking()
    
    # Show some examples so it makes sense
    demonstrate_with_examples()
    
    # Get their numbers
    tiny_num, dust_num = ask_about_current_air()
    
    # Process what it means
    print(" ")
    print("Let me mull this over for a bit...")
    time.sleep(3.5)
    
    # Share what I came up with
    air_analysis = make_sense_of_air(tiny_num, dust_num)
    share_my_thoughts(air_analysis)
    
    # Wrap it up nicely
    say_goodbye()

# This part runs if you start the file directly
if __name__ == "__main__":
    try:
        run_the_program()
    except KeyboardInterrupt:
        print(" ")
        print("Oh, heading out already? Come back if you want to chat about air! 👋")
    except Exception as whoops:
        print(" ")
        print(f"Well that's odd - something went sideways: {whoops}")
        print("Let's try that whole thing again, shall we?")
        run_the_program()