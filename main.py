#constants for behaviour messages
FRIENDLY_MESSAGE = "The door opens!"
HOSTILE_MESSAGE = "The door stays closed."

#Get the creatures behaviour from the player
def get_time_of_day():
  return input("What time of the day is it? ").strip().lower()

#Use if-else statement to determine the action based on the creatures behaviour
def determine_action(time_of_day):
  if time_of_day == "morning" or time_of_day == "afternoon":
    return (FRIENDLY_MESSAGE)
  elif time_of_day == "evening" or time_of_day == "night":
    return (HOSTILE_MESSAGE)
  else:
    return (HOSTILE_MESSAGE)
  
def main():
  time_of_day = get_time_of_day()
  action = determine_action(time_of_day)
  print(action)

if __name__ == "__main__":
  main()
