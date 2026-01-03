class QuestionGenerator:
    def __init__(self, topics):
        self.topics = topics

    def initial_questions(self):
        questions = []

        if "Machine Learning" in self.topics:
            questions.append("How did you train your machine learning model?")

        if "Backend" in self.topics:
            questions.append("How does your backend API handle requests?")

        return questions

    def follow_up(self, response):
        response = response.lower()
        followups = []

        if "accuracy" in response:
            followups.append("Why did you choose accuracy as the evaluation metric?")

        if "model" in response:
            followups.append("Did you experiment with other models?")

        if "flask" in response:
            followups.append("How would this application scale with more users?")

        if not followups:
            followups.append("Can you explain this in more detail?")

        return followups