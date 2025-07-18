# Define functions for each traffic light color 

def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow.")

def green_light():
    print("Go! The light is green.")

# Define a controller function to call the right light function

def traffic_light(state):
    if state =="red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
        print("Error: Invalid traffick light state") 

# Test the traffic_light function 

traffic_light("red")
traffic_light("yellow")
traffic_light("green")


"""
# Customize the function - celebrating a goal

def celebrate_goal(player):
    print("GOOOOOAAALLL!!", player, "scores!")

celebrate_goal("Ronaldo")


# Customize another function - announce a final score

def match_result(team1, team2, score1, score2):
    print(f"Final Score: {team1} {score1} - {score2} {team2}")

match_result("Portugal", "Brazil", 2, 1)
"""