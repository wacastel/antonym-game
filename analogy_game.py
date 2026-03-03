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

    # --- THE NEW MAIN MENU ---
    print("\n" + "="*40)
    print(" 🏛️  THE PALACE LIBRARY ARCADE  🏛️ ")
    print("="*40)
    print("1. Solo Semantic Challenge (Classic)")
    print("2. Head-to-Head: William vs. The Machine")
    print("="*40)
    
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Choose your mode (1 or 2): ").strip()
    
    is_head_to_head = (mode == "2")

    # Randomize the questions and slice to exactly 5 rounds!
    random.shuffle(game_questions)
    game_questions = game_questions[:5]

    william_score = 0
    ai_score = 0
    
    if is_head_to_head:
        print("\n⚔️ --- HEAD-TO-HEAD MODE INITIATED --- ⚔️")
        print("Let the battle of wits begin!")
    else:
        print("\n--- WELCOME TO THE SEMANTIC CHALLENGE ---")
        
    print("Format: 'A' is to 'B' as 'C' is to [?]")
    
    for q in game_questions:
        a, b, c, target_answer = q["word_a"], q["word_b"], q["word_c"], q["target_answer"]
        
        # The AI calculates its target organically
        ai_organic_target = model.most_similar(positive=[b, c], negative=[a], topn=1)[0][0]
        
        print(f"\nQuestion: {a.upper()} is to {b.upper()} as {c.upper()} is to...")
        
        start_time = time.time()
        guess = input("Your Guess: ").strip().lower()
        elapsed = round(time.time() - start_time, 2)

        print("\n--- The Reveal ---")
        
        # 1. Score the AI
        print(f"🤖 AI's Guess: '{ai_organic_target}'")
        ai_points = 0
        
        if target_answer in model:
            ai_similarity = model.similarity(ai_organic_target, target_answer)
        else:
            ai_similarity = 0

        if ai_organic_target == target_answer:
            ai_points = 10
            print("   The AI was correct! It matches the true target. (+10 AI pts)")
        elif ai_similarity > 0.7:
            ai_points = 5
            print(f"   The AI was close. Similarity: {ai_similarity:.2f} (+5 AI pts)")
        else:
            print(f"   The AI was incorrect! The true target is '{target_answer}'. (0 AI pts)")
            
        if is_head_to_head:
            ai_score += ai_points

        # 2. Score the human
        if guess not in model:
            print(f"\nAlas! '{guess}' is not in my library. 0 points.")
            human_points = 0
        else:
            if target_answer in model:
                human_similarity = model.similarity(guess, target_answer)
            else:
                human_similarity = 0

            print(f"\n👤 William's Score:")
            if guess == target_answer:
                human_points = 10
                print(f"✨ Perfect! '{target_answer.capitalize()}' is exactly right. (+{human_points} pts in {elapsed}s)")
            elif human_similarity > 0.7:
                human_points = 5
                print(f"💡 So close! '{guess}' is semantically near '{target_answer}'. Similarity: {human_similarity:.2f} (+{human_points} pts)")
            else:
                human_points = 0
                print(f"❌ Not quite. The vector was too far away. Similarity: {human_similarity:.2f}")
                
        william_score += human_points

    # --- THE GRAND FINALE SCOREBOARD ---
    print("\n" + "="*40)
    print(" 🏁  GAME OVER  🏁 ")
    print("="*40)
    
    if is_head_to_head:
        print(f"👤 William's Final Score: {william_score}")
        print(f"🤖 AI's Final Score:      {ai_score}")
        print("-" * 40)
        if william_score > ai_score:
            print("🏆 HUMANITY WINS! You outsmarted the 50-dimensional matrix!")
        elif ai_score > william_score:
            print("🤖 THE MACHINE WINS! Don't worry, its training corpus was just lucky today.")
        else:
            print("🤝 IT'S A TIE! A perfect balance between human intuition and machine logic.")
    else:
        print(f"William's Final Score: {william_score}")
        
    print("="*40)

if __name__ == "__main__":
    play_analogy_game()
