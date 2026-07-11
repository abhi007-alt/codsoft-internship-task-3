# Task 4 - Recommendation System

## CodSoft Internship

A simple **content-based movie recommendation system**. It represents
each movie as a genre vector and recommends the most similar movies
to one the user already likes, using **cosine similarity**.

## How to Run
```bash
python recommender.py
```

You'll be shown a list of available movies, then asked to enter one
you like. The system returns the top 3 most similar movies.

## Example
```
Enter a movie you like: Inception

Because you liked 'Inception', you might also enjoy:
  - The Matrix  (similarity: 0.82)
  - John Wick  (similarity: 0.67)
  - Mad Max: Fury Road  (similarity: 0.67)
```

## Concepts Used
- Content-based filtering
- Vector representation of items (genres)
- Cosine similarity

## Author
Built as part of the CodSoft Internship program.
