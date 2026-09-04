class StudySession:

    def __init__(self, date, subject, topic, minutes, score):
        self.date = date
        self.subject = subject
        self.topic = topic
        self.minutes = minutes
        self.score = score

    def __str__(self):
        return f"Date: {self.date}\nSubject: {self.subject}\nTopic: {self.topic}\nMinutes: {self.minutes}\nScore: {self.score}"
    