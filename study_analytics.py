from datetime import timedelta

class StudyAnalytics:

    def __init__(self, study_sessions):
        self.study_sessions = study_sessions

    def get_total_minutes(self):
        total_minutes = 0

        for session in self.study_sessions:
            total_minutes += session.minutes

        return total_minutes

    def get_average_score(self):
        if len(self.study_sessions) == 0:
            return "Cannot get average of an empty list"
        
        total_score = 0.0

        for session in self.study_sessions:
            total_score += session.score

        return total_score / len(self.study_sessions)

    def get_minutes_by_subject(self):
        minutes_by_subject = {}

        for session in self.study_sessions:
            if session.subject in minutes_by_subject:
                minutes_by_subject[session.subject] += session.minutes
            else:
                minutes_by_subject[session.subject] = session.minutes

        return minutes_by_subject

    def get_average_score_by_topic(self):
        total_score_by_topic = {}
        count_by_topic = {}

        for session in self.study_sessions:
            topic = session.topic
            score = session.score

            if topic in total_score_by_topic:
                total_score_by_topic[topic] += score
                count_by_topic[topic] += 1
            else:
                total_score_by_topic[topic] = score
                count_by_topic[topic] = 1

        average_score_by_topic = {}

        for topic in total_score_by_topic:
            average_score_by_topic[topic] = total_score_by_topic[topic] / count_by_topic[topic]

        return average_score_by_topic

    def get_minutes_by_date(self):
        minutes_by_date = {}

        for session in self.study_sessions:
            session_date = session.date
            minutes = session.minutes

            if session_date in minutes_by_date:
                minutes_by_date[session_date] += minutes
            else:
                minutes_by_date[session_date] = minutes

        return minutes_by_date

    def get_longest_study_streak(self):
        if len(self.study_sessions) == 0:
            return 0

        study_dates = set()

        for session in self.study_sessions:
            study_dates.add(session.date)

        sorted_dates = sorted(study_dates)

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(sorted_dates)):

            if sorted_dates[i] == sorted_dates[i-1] + timedelta(days=1):
                current_streak += 1

                if current_streak > longest_streak:
                    longest_streak = current_streak

            else:
                current_streak = 1

        return longest_streak


        


