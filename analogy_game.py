import csv
import time
import random
from gensim import downloader as api

def play_analogy_game():
    print("\nSaraswati is opening the scrolls... (Loading knowledge model)")
    model = api.load("glove-wiki-gigaword-50")
    
    # Load questions from the CSV
    game_questions = []
    try:
        with open("questions.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                game_questions.append(row)
    except FileNotFoundError:
        print("Alas! I cannot find 'questions.csv'.")
        return

    # Randomize the questions and slice to exactly 5 rounds!
    random.shuffle(game_questions)
    game_questions = game_questions[:5]

    score = 0
    print("\n--- WELCOME TO THE SEMANTIC CHALLENGE ---")
    print("Format: 'A' is to 'B' as 'C' is to [?]")
    
    for q in game_questions:
        a, b, c, target_answer = q["word_a"], q["word_b"], q["word_c"], q["target_answer"]
        
        # The AI calculates its target organically, right or wrong!
        ai_organic_target = model.most_similar(positive=[b, c], negative=[a], topn=1)[0][0]
        
        print(f"\nQuestion: {a.upper()} is to {b.upper()} as {c.upper()} is to...")
        
        start_time = time.time()
        guess = input("Your Guess: ").strip().lower()
        elapsed = round(time.time() - start_time, 2)

        print("\n--- The Reveal ---")
        
        # 1. Check the AI's homework
        print(f"🤖 AI's Guess: '{ai_organic_target}'")
        if ai_organic_target == target_answer:
            print("   The AI was correct! It matches the true target.")
        else:
            print(f"   The AI was incorrect! The true target is '{target_answer}'.")

        if guess not in model:
            print(f"\nAlas! '{guess}' is not in my library. 0 points.")
            continue

        # 2. Score the human against the true target answer
        if target_answer in model:
            similarity = model.similarity(guess, target_answer)
        else:
            similarity = 0

        print(f"\n👤 William's Score:")
        if guess == target_answer:
            points = 10
            print(f"✨ Perfect! '{target_answer.capitalize()}' is exactly right. (+{points} pts in {elapsed}s)")
        elif similarity > 0.7:
            points = 5
            print(f"💡 So close! '{guess}' is semantically near '{target_answer}'. Similarity: {similarity:.2f} (+{points} pts)")
        else:
            points = 0
            print(f"❌ Not quite. The vector was too far away. Similarity: {similarity:.2f}")
            
        score += points

    print(f"\n--- GAME OVER ---")
    print(f"William's Final Score: {score}")

if __name__ == "__main__":
    play_analogy_game()
