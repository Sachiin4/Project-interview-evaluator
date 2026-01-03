import re

class ContentAnalyzer:
    def __init__(self, text):
        self.text = text.lower()

    def detect_topics(self):
        topics = []

        if any(word in self.text for word in ["model", "training", "accuracy"]):
            topics.append("Machine Learning")

        if any(word in self.text for word in ["api", "flask", "backend"]):
            topics.append("Backend")

        return topics