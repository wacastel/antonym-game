import csv
import time
import random
from gensim import downloader as api

# The Main Game Logic
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

    # Randomize the questions so it's a fresh game every time!
    random.shuffle(game_questions)

    score = 0
    print("\n--- WELCOME TO THE SEMANTIC CHALLENGE ---")
    print("Format: 'A' is to 'B' as 'C' is to [?]")
    
    for q in game_questions:
        a, b, c = q["word_a"], q["word_b"], q["word_c"]
        
        # As you requested: The AI calculates the target organically!
        # It ignores the CSV's 'target_answer' for now and trusts its own vector math.
        ai_organic_target = model.most_similar(positive=[b, c], negative=[a], topn=1)[0][0]
        
        print(f"\nQuestion: {a.upper()} is to {b.upper()} as {c.upper()} is to...")
        
        start_time = time.time()
        guess = input("Your Guess: ").strip().lower()
        elapsed = round(time.time() - start_time, 2)

        if guess not in model:
            print("Alas! That word is not in my library. 0 points.")
            continue

        # Score against the AI's organically calculated target
        similarity = model.similarity(guess, ai_organic_target)
        
        if guess == ai_organic_target:
            points = 10
            print(f"✨ Perfect! '{ai_organic_target.capitalize()}' is exactly right. (+{points} pts in {elapsed}s)")
        elif similarity > 0.7:
            points = 5
            print(f"💡 So close! '{guess}' is semantically near '{ai_organic_target}'. Similarity: {similarity:.2f} (+{points} pts)")
        else:
            points = 0
            print(f"❌ Not quite. The vector was too far away. Similarity: {similarity:.2f}")
            
        score += points

    print(f"\n--- GAME OVER ---")
    print(f"William's Final Score: {score}")

if __name__ == "__main__":
    play_analogy_game()    # Runs the application
