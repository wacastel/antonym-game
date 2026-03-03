import csv
import time
import random
from gensim import downloader as api

# A quick helper function to manifest our CSV scroll
def create_question_bank():
    questions = [
        ["man", "king", "woman", "queen"],
        ["paris", "france", "tokyo", "japan"],
        ["walk", "walked", "run", "ran"],
        ["cold", "colder", "hot", "hotter"],
        ["good", "better", "bad", "worse"],
        ["uncle", "aunt", "nephew", "niece"]
    ]
    
    # We include the 'target_answer' column for your future Head-to-Head mode!
    with open("questions.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word_a", "word_b", "word_c", "target_answer"])
        writer.writerows(questions)
    print("📜 'questions.csv' has been inscribed and safely stored!")

if __name__ == "__main__":
    create_question_bank() # Creates the data file

