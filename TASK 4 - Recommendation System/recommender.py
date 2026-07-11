"""
Movie Recommendation System (Content-Based Filtering)
CodSoft Internship - Task 4

Recommends movies to a user based on genre similarity to a movie
they already like, using cosine similarity over genre vectors.
No external ML libraries required.
"""

import math

# Small sample movie dataset: title -> set of genres
MOVIES = {
    "The Dark Knight": {"Action", "Crime", "Drama"},
    "Inception": {"Action", "Sci-Fi", "Thriller"},
    "Interstellar": {"Sci-Fi", "Drama", "Adventure"},
    "The Notebook": {"Romance", "Drama"},
    "La La Land": {"Romance", "Musical", "Drama"},
    "John Wick": {"Action", "Thriller", "Crime"},
    "Titanic": {"Romance", "Drama", "History"},
    "The Matrix": {"Action", "Sci-Fi"},
    "Pride and Prejudice": {"Romance", "Drama"},
    "Mad Max: Fury Road": {"Action", "Adventure", "Sci-Fi"},
    "The Conjuring": {"Horror", "Thriller"},
    "Get Out": {"Horror", "Thriller", "Mystery"},
}

ALL_GENRES = sorted({genre for genres in MOVIES.values() for genre in genres})


def vectorize(genres):
    """Convert a set of genres into a binary vector over ALL_GENRES."""
    return [1 if g in genres else 0 for g in ALL_GENRES]


def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def recommend(movie_title, top_n=3):
    if movie_title not in MOVIES:
        print(f"'{movie_title}' not found in the database.")
        return []

    target_vector = vectorize(MOVIES[movie_title])
    scores = []

    for title, genres in MOVIES.items():
        if title == movie_title:
            continue
        score = cosine_similarity(target_vector, vectorize(genres))
        scores.append((title, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


def main():
    print("Available movies:")
    for title in MOVIES:
        print(f"  - {title}")

    movie = input("\nEnter a movie you like: ").strip()
    recommendations = recommend(movie)

    if recommendations:
        print(f"\nBecause you liked '{movie}', you might also enjoy:")
        for title, score in recommendations:
            print(f"  - {title}  (similarity: {score:.2f})")


if __name__ == "__main__":
    main()
