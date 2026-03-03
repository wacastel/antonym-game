import time
from gensim import downloader as api

# 1. Load the Knowledge Base (Re-using our 50-dim model)
print("Saraswati is opening the scrolls...")
model = api.load("glove-wiki-gigaword-50")

def play_analogy_game():
    score = 0
    # A small bank of 'Interesting' analogies for our PoC
    questions = [
        ("man", "king", "woman", "queen"),
        ("paris", "france", "tokyo", "japan"),
        ("walk", "walked", "run", "ran"),
        ("cold", "colder", "hot", "hotter"),
        ("good", "better", "bad", "worse")
    ]
    
    print("\n--- WELCOME TO THE SEMANTIC CHALLENGE ---")
    print("Format: 'A' is to 'B' as 'C' is to [?]")
    
    for a, b, c, target in questions:
        print(f"\nQuestion: {a.upper()} is to {b.upper()} as {c.upper()} is to...")
        
        start_time = time.time()
        guess = input("Your Guess: ").strip().lower()
        elapsed = round(time.time() - start_time, 2)

        if guess not in model:
            print("Alas! That word is not in my library. 0 points.")
            continue

        # CALCULATE SEMANTIC SIMILARITY
        # similarity() returns a value from -1 to 1. 1 is a perfect match.
        similarity = model.similarity(guess, target)
        
        if guess == target:
            points = 10
            # Using an f-string to pull the actual target word from our list!
            print(f"✨ Perfect! '{target.capitalize()}' is exactly right. (+{points} pts in {elapsed}s)")
        elif similarity > 0.7:
            points = 5
            # We can even suggest the target word as a hint!
            print(f"💡 So close! '{guess}' is semantically near '{target}'. Similarity: {similarity:.2f} (+{points} pts)")
        else:
            points = 0
            print(f"❌ Not quite. The vector was too far away. Similarity: {similarity:.2f}")
            
        score += points

    print(f"\n--- GAME OVER ---")
    print(f"William's Final Score: {score}")
    print("Saraswati is very proud of your progress!")

if __name__ == "__main__":
    play_analogy_game()
