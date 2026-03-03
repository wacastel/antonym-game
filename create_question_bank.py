import csv

def create_question_bank():
    # 100 carefully curated analogies for our NLP engine!
    questions = [
        # --- Geography & Capitals ---
        ["paris", "france", "tokyo", "japan"], ["rome", "italy", "berlin", "germany"],
        ["madrid", "spain", "athens", "greece"], ["london", "england", "dublin", "ireland"],
        ["moscow", "russia", "beijing", "china"], ["cairo", "egypt", "nairobi", "kenya"],
        ["ottawa", "canada", "washington", "usa"], ["havana", "cuba", "lima", "peru"],
        ["oslo", "norway", "stockholm", "sweden"], ["seoul", "korea", "bangkok", "thailand"],
        # --- Family & Gender ---
        ["man", "king", "woman", "queen"], ["uncle", "aunt", "nephew", "niece"],
        ["father", "mother", "son", "daughter"], ["brother", "sister", "grandfather", "grandmother"],
        ["boy", "girl", "man", "woman"], ["husband", "wife", "groom", "bride"],
        ["actor", "actress", "prince", "princess"], ["waiter", "waitress", "hero", "heroine"],
        ["monk", "nun", "wizard", "witch"], ["sir", "madam", "lord", "lady"],
        # --- Grammar: Past Tense ---
        ["walk", "walked", "run", "ran"], ["go", "went", "eat", "ate"],
        ["sleep", "slept", "wake", "woke"], ["swim", "swam", "fly", "flew"],
        ["catch", "caught", "bring", "brought"], ["teach", "taught", "buy", "bought"],
        ["see", "saw", "hear", "heard"], ["write", "wrote", "read", "read"],
        ["speak", "spoke", "choose", "chose"], ["fall", "fell", "hide", "hid"],
        # --- Grammar: Comparatives & Superlatives ---
        ["cold", "colder", "hot", "hotter"], ["good", "better", "bad", "worse"],
        ["fast", "faster", "slow", "slower"], ["high", "higher", "low", "lower"],
        ["big", "bigger", "small", "smaller"], ["tall", "taller", "short", "shorter"],
        ["young", "younger", "old", "older"], ["rich", "richer", "poor", "poorer"],
        ["hard", "harder", "soft", "softer"], ["bright", "brighter", "dark", "darker"],
        ["cold", "coldest", "hot", "hottest"], ["good", "best", "bad", "worst"],
        ["fast", "fastest", "slow", "slowest"], ["high", "highest", "low", "lowest"],
        ["big", "biggest", "small", "smallest"], ["tall", "tallest", "short", "shortest"],
        ["young", "youngest", "old", "oldest"], ["rich", "richest", "poor", "poorest"],
        ["hard", "hardest", "soft", "softest"], ["bright", "brightest", "dark", "darkest"],
        # --- Opposites / Antonyms ---
        ["up", "down", "left", "right"], ["in", "out", "over", "under"],
        ["start", "stop", "begin", "end"], ["open", "close", "push", "pull"],
        ["empty", "full", "heavy", "light"], ["loud", "quiet", "noisy", "silent"],
        ["early", "late", "first", "last"], ["win", "lose", "success", "failure"],
        ["day", "night", "morning", "evening"], ["summer", "winter", "spring", "autumn"],
        # --- Part to Whole & Object Properties ---
        ["car", "wheels", "airplane", "wings"], ["tree", "leaves", "bird", "feathers"],
        ["book", "pages", "house", "bricks"], ["keyboard", "keys", "guitar", "strings"],
        ["computer", "screen", "clock", "face"], ["dog", "bark", "cat", "meow"],
        ["lion", "roar", "snake", "hiss"], ["fire", "hot", "ice", "cold"],
        ["sun", "bright", "coal", "dark"], ["water", "wet", "sand", "dry"],
        # --- Assorted / Vocabulary ---
        ["baker", "bread", "chef", "food"], ["doctor", "hospital", "teacher", "school"],
        ["farmer", "crops", "artist", "art"], ["scissors", "cut", "pen", "write"],
        ["hammer", "hit", "knife", "slice"], ["eye", "see", "ear", "hear"],
        ["nose", "smell", "tongue", "taste"], ["leg", "walk", "hand", "grasp"],
        ["bird", "nest", "bear", "cave"], ["bee", "hive", "spider", "web"]
    ]
    
    with open("questions.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word_a", "word_b", "word_c", "target_answer"])
        writer.writerows(questions)
    print("📜 'questions.csv' has been inscribed with 100 analogies and safely stored!")

if __name__ == "__main__":
    create_question_bank()
