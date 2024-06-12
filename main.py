#constants for behaviour messages
FRIENDLY_MESSAGE = "The door opens!"
HOSTILE_MESSAGE = "The door stays closed."

#Get the creatures behaviour from the player
def get_creature_behaviour():
  return input("What is the behaviour: friendly or hostile? ").strip().lower()

#Use if-else statement to determine the action based on the creatures behaviour
def determine_action(creature_behaviour):
  if creature_behaviour == "friendly":
    print(FRIENDLY_MESSAGE)
  else:
    print(HOSTILE_MESSAGE)

def main():
  behaviour = get_creature_behaviour()
  determine_action(behaviour)

if __name__ == "__main__":
  main()
