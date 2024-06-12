# Constants for behavior messages
FRIENDLY_MESSAGE = "The door opens!"
HOSTILE_MESSAGE = "The door stays closed."
UNKNOWN_MESSAGE = "Time of day is unknown. The door stays closed."

def get_time_of_day() -> str:
    return input("What time of the day is it? ").strip().lower()

def determine_action(time_of_day: str) -> str:
    # Dictionary to map times of day to messages
    actions = {
        "morning": FRIENDLY_MESSAGE,
        "afternoon": FRIENDLY_MESSAGE,
        "evening": HOSTILE_MESSAGE,
        "night": HOSTILE_MESSAGE,
    }
    # Return the corresponding message or a default message for unknown times
    return actions.get(time_of_day, UNKNOWN_MESSAGE)
    
def main():
    time_of_day = get_time_of_day()
    action = determine_action(time_of_day)
    print(action)

if __name__ == "__main__":
    main()
