from study_session import StudySession
from study_analytics import StudyAnalytics
from datetime import date

def get_study_session():
    today = date.today()
    subject = input("Enter your subject: ")
    topic = input("Enter the topic: ")
    minutes = validate_int_input("Enter the number of minutes: ", 1, 1440)
    score = validate_int_input("Enter the score: ", 0, 100)

    session = StudySession(today, subject, topic, minutes, score)
    return session

def display_study_sessions(study_sessions):
    if len(study_sessions) == 0:
        print("No Study Sessions to Display.")
        return
    
    for session in study_sessions:
        print(session)
        print()

def display_summary(analytics):
    print("======= STUDY SUMMARY =======")

    print(f"Total minutes: {analytics.get_total_minutes()}")
    print(f"Average Score: {analytics.get_average_score()}")

    minutes_by_subject = analytics.get_minutes_by_subject()
    for subject, minutes in minutes_by_subject.items():
        print(f"{subject}: {minutes} minutes")
    
    average_score_by_topic = analytics.get_average_score_by_topic()
    for topic, score in average_score_by_topic.items():
        print(f"{topic}: {score}%")
        
    minutes_by_date = analytics.get_minutes_by_date()
    for date, minutes in minutes_by_date.items():
        print(f"{date}: {minutes} minutes")

    print(f"Longest Study Streak: {analytics.get_longest_study_streak()}")

def modify_or_delete_session(study_sessions):
    if len(study_sessions) == 0:
        print("No sessions to modify or delete.")
        return

    for i, session in enumerate(study_sessions, start=1):
        print(f"{i}. {session}")

    choice = validate_int_input("Enter the session number: ", 1, len(study_sessions))

    selected_session = study_sessions[choice - 1]
    print(selected_session)

    action = validate_int_input("1. Modify\n2. Delete\n3. Cancel\nChoose an action: ", 1, 3)

    match action:
        case 1:
            modify(study_sessions, choice - 1)
        case 2: 
            study_sessions.pop(choice - 1)
        case 3:
            return
        
def modify(study_sessions, index):
    action = validate_int_input("1. Modify Date\n2. Modify Subject\n3. Modify Topic\n4. Modify Minutes\n5. Modify Score\n6. Cancel\nChoose an action: ", 1, 6)
    
    match action:
        case 1:
            study_sessions[index].date = validate_date_input("Set new date (YYYY-MM-DD): ")
        case 2:     
            study_sessions[index].subject = input("Set new subject: ")
        case 3: 
            study_sessions[index].topic = input("Set new topic: ")
        case 4:
            study_sessions[index].minutes = validate_int_input("Set new minutes: ", 1, 1440)
        case 5:
            study_sessions[index].score = validate_int_input("Set new score: ", 0, 100)
        case 6: 
            return

def validate_int_input(prompt, lower, upper):
    while True:
        try:
            value = int(input(prompt))

            if lower <= value <= upper:
                return value

            print(f"Invalid input. Please choose a number between {lower}-{upper}. ")

        except ValueError:
            print("Please enter a valid number.")

def validate_date_input(prompt):
    while True:
        try:
            value = input(prompt)
            value = date.fromisoformat(value)
            return value
        except ValueError:
            print("Please enter a valid date.")
    
def main():
    study_sessions = []
    analytics = StudyAnalytics(study_sessions)
    running = True

    while running:
        print("Welcome to the Study Session Tracker!")
        print("\n1. Add a new study session")
        print("\n2. View all study sessions")
        print("\n3. View study session summary")
        print("\n4. Modify or delete a study session")
        print("\n5. Save & exit")

        choice = validate_int_input("Please select an option (1-5): ", 1, 5)

        match choice:
            case 1:
                session = get_study_session()
                study_sessions.append(session)
            case 2: 
                display_study_sessions(study_sessions)
            case 3:
                display_summary(analytics)
            case 4:
                modify_or_delete_session(study_sessions)
            case 5: 
                running = False

if __name__ == "__main__":
    main()
    