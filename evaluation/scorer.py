class Scorer:
    def __init__(self, text):
        self.text = text.lower()

    def score(self):
        scores = {}

        tech_terms = ["model", "training", "api", "accuracy"]
        scores["Technical Depth"] = min(10, 5 + sum(t in self.text for t in tech_terms))

        scores["Clarity"] = 8
        scores["Originality"] = 7
        scores["Understanding"] = 6

        return scores
