from datetime import datetime

class ReportWriter:
    def write(self, topics, questions, followups, scores, feedback):
        content = []

        content.append("Project Interview Evaluation")
        content.append(str(datetime.now()))
        content.append("")

        content.append("Topics:")
        for t in topics:
            content.append(f"- {t}")

        content.append("\nQuestions:")
        for q in questions:
            content.append(f"- {q}")

        content.append("\nFollow-up Questions:")
        for f in followups:
            content.append(f"- {f}")

        content.append("\nScores:")
        for k, v in scores.items():
            content.append(f"{k}: {v}/10")

        content.append("\nFeedback:")
        content.append(feedback)

        with open("final_report.txt", "w") as f:
            f.write("\n".join(content))
