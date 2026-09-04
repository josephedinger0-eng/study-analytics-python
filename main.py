from study_session import StudySession
from study_analytics import StudyAnalytics
from datetime import date

study_sessions = []
analytics = StudyAnalytics(study_sessions)

today = date.today()
subject = input("Enter your subject: ")
topic = input("Enter the topic: ")
minutes = int(input("Enter the number of minutes: "))
score = int(input("Enter your score: "))

test = StudySession(today, subject, topic, minutes, score)
study_sessions.append(test)
study_sessions.append(StudySession(today, "English", "Grammar", 60, 100))

for session in study_sessions:
    print(session)

total_minutes = analytics.get_total_minutes()

print(f"Total study time: {total_minutes} minutes")

average_score = analytics.get_average_score()

print(f"Average score: {average_score}%")