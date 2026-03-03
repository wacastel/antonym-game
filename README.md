# 🧠 Semantic Analogy Engine: The "Saraswati" Challenge

Welcome to the **Semantic Analogy Engine**, a Natural Language Processing (NLP) project that uses high-dimensional word embeddings to solve linguistic analogies and challenge users in a game of semantic wit.

## 📖 The Theory: Word Embeddings & Vector Space

At the heart of this project lies the concept of **Distributional Semantics**: the idea that a word's meaning is defined by the company it keeps.

### 1. Word2Vec & GloVe
We utilize **GloVe (Global Vectors for Word Representation)**. Unlike traditional one-hot encoding, GloVe represents each word as a dense vector in a continuous vector space ($\mathbb{R}^d$). In our case, $d=50$.

### 2. The Math of Analogies
The "magic" of the game—solving $A \text{ is to } B \text{ as } C \text{ is to } ?$—is rooted in **Linear Algebraic Cosine Similarity**. 

The engine performs the following vector arithmetic:

$$\vec{V}_{target}=\vec{V}_{B}-\vec{V}_{A}+\vec{V}_{C}$$

For the classic example:

$$\vec{V}_{king}-\vec{V}_{man}+\vec{V}_{woman}\approx\vec{V}_{queen}$$

### 3. Scoring via Cosine Similarity
To provide partial credit for "close" guesses, we calculate the **Cosine Similarity** ($\cos(\theta)$) between the player's guess ($\vec{u}$) and the target word ($\vec{v}$):

$$\text{similarity}=\cos(\theta)=\frac{\vec{u}\cdot\vec{v}}{\|\vec{u}\|\|\vec{v}\|}$$

* **1.0**: Perfect match (Exact word).
* **> 0.7**: High semantic overlap (Partial credit).
* **< 0.5**: Weak semantic relationship (No points).

---

## 🎮 How to Play

1.  **The Prompt**: The AI presents three words: $A$, $B$, and $C$.
2.  **The Goal**: You must provide the fourth word ($D$) that completes the relationship.
3.  **Scoring**:
    * **10 Points**: Exact Match.
    * **5 Points**: Semantic Near-Miss (Similarity > 0.7).
    * **0 Points**: Incorrect or word not in library.
4.  **Speed**: Your time is tracked—challenge yourself to find the vector in under 2 seconds!

## 🛠️ Requirements

- Python 3.8+
- `gensim` library
- `glove-wiki-gigaword-50` (auto-downloaded via the script)

---

*“Knowledge is a treasure that grows when shared. May your vectors always point toward the truth.”* — **Saraswati**
