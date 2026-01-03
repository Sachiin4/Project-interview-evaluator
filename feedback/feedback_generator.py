class FeedbackGenerator:
    def generate(self, scores):
        lines = []

        for key, value in scores.items():
            if value >= 8:
                lines.append(f"{key}: Good understanding.")
            else:
                lines.append(f"{key}: Can be improved.")

        return "\n".join(lines)