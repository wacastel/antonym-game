import gensim.downloader as api

def run_analogy_engine():
    # 1. Load a pre-trained model (50-dimensional vectors)
    # This model 'knows' 400,000 words based on Wikipedia data.
    print("Saraswati is fetching the knowledge... (Loading model)")
    model = api.load("glove-wiki-gigaword-50")
    print("Knowledge loaded!\n")

    def solve_analogy(a, b, c):
        """
        Solves the analogy: 'a' is to 'b' as 'c' is to '?'
        Logic: Vector(b) - Vector(a) + Vector(c) = Vector(Target)
        """
        try:
            # most_similar does the vector arithmetic under the hood!
            # positive=[b, c] adds those vectors, negative=[a] subtracts 'a'
            results = model.most_similar(positive=[b, c], negative=[a], topn=1)
            return results[0][0]
        except KeyError as e:
            return f"Error: Word '{e.args[0]}' not in my library!"

    # 2. Test the classic relationship
    test_word = solve_analogy('man', 'king', 'woman')
    print(f"Classical Test -> man : king :: woman : {test_word}")

    # 3. Test a few more 'interesting' ones for your game
    print(f"Family Test    -> father : son :: mother : {solve_analogy('father', 'son', 'mother')}")
    print(f"Geography Test -> paris : france :: tokyo : {solve_analogy('paris', 'france', 'tokyo')}")
    print(f"Verb Tense     -> walk : walked :: run : {solve_analogy('walk', 'walked', 'run')}")

if __name__ == "__main__":
    run_analogy_engine()
