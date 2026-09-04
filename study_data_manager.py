import csv
from datetime import date
from study_session import StudySession


def save_sessions(study_sessions):
    with open("study_data.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["date", "subject", "topic", "minutes", "score"])
        for session in study_sessions:
            writer.writerow([session.date,
                session.subject,
                session.topic,
                session.minutes,
                session.score
                ])

def load_sessions():
    study_sessions = []

    try:
        with open("study_data.csv", "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                session = StudySession(date.fromisoformat(row[0]), row[1], row[2], int(row[3]), int(row[4]))
                study_sessions.append(session)
    except FileNotFoundError:
        return study_sessions

    return study_sessions



