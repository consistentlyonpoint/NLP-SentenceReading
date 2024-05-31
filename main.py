from SentenceReadingAgent import SentenceReadingAgent
import time

def test():
    #This will test your SentenceReadingAgent
	#with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_0 = "There are three men in the car."
    question_0 = "Where are the men?"
    sentence_01 = "Bring the box to the other room."
    question_01 = "Where should the box go?"
    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"


    print("set1, q0 :", test_agent.solve(sentence_0, question_0))  # "car"
    print("set1, q01 :", test_agent.solve(sentence_01, question_01))  # "room"
    print("set1, q1 :", test_agent.solve(sentence_1, question_1))  # "Ada"
    print("set1, q2 :", test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    print("set1, q3 :", test_agent.solve(sentence_1, question_3))  # "Irene"
    print("set1, q4 :", test_agent.solve(sentence_1, question_4))  # "short"

    print("set2, q5 :", test_agent.solve(sentence_2, question_5))  # "David"
    print("set2, q6 :", test_agent.solve(sentence_2, question_6))  # "school"
    print("set2, q7 :", test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    print("set2, q8 :", test_agent.solve(sentence_2, question_8))  # "walk"
    print("set2, q9 :", test_agent.solve(sentence_2, question_9))  # "8:00AM"

    sentence_3 = "There are three men in the car."
    question_10 = "Who is in the car?"
    print("set3, q10 :", test_agent.solve(sentence_3, question_10))

    sentence_11 = "The island is east of the city."
    question_11 = "What is east of the city?"
    print("set2, q11 :", test_agent.solve(sentence_11, question_11))

if __name__ == "__main__":
    start_timer = time.time()
    test()
    stop_timer = time.time()
    print(f"agent takes {stop_timer - start_timer}")
