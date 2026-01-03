from nlp.content_analyzer import ContentAnalyzer
from questions.question_generator import QuestionGenerator
from evaluation.scorer import Scorer
from feedback.feedback_generator import FeedbackGenerator
from feedback.report_writer import ReportWriter

with open("data/presentation.txt") as f:
    presentation_text = f.read()

with open("data/responses.txt") as f:
    responses = f.readlines()

analyzer = ContentAnalyzer(presentation_text)
topics = analyzer.detect_topics()

question_gen = QuestionGenerator(topics)
initial_questions = question_gen.initial_questions()

followups = []
for r in responses:
    followups.extend(question_gen.follow_up(r))

scorer = Scorer(" ".join(responses))
scores = scorer.score()

feedback_gen = FeedbackGenerator()
feedback = feedback_gen.generate(scores)

writer = ReportWriter()
writer.write(topics, initial_questions, followups, scores, feedback)

print("Evaluation completed. Report saved as final_report.txt")
