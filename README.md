# Music Recommender Simulation

## Project Summary

This MVP builds a rule-based music recommender that scores songs by genre match, mood match, energy closeness, and acoustic preference. It loads a small CSV catalog, computes a score for each song, sorts by score, and returns top recommendations with plain-language explanations.

## How The System Works

The recommender uses song-level features and user preferences, then computes a weighted score.

In real-world apps, recommendation systems usually blend collaborative filtering (patterns across similar users), content-based filtering (similarity across song attributes), and session context (what the user is doing right now). My version prioritizes transparent content-based matching first, especially genre, mood, and energy alignment, so each recommendation is easy to explain and debug while still producing a useful top-k list.

Song features used:
- Genre
- Mood
- Energy
- Acousticness
- Supporting metadata (title, artist, tempo, valence, danceability)

User profile inputs used:
- Favorite genre
- Favorite mood
- Target energy
- Whether the user prefers acoustic-heavy tracks

Scoring logic:
- Genre exact or close match: +2.5
- Mood match: +2.0
- Energy closeness: up to +1.5, based on absolute distance
- Acoustic preference alignment: +1.0

Top-k selection:
- Score each song
- Sort by descending score
- Return top k with short explanations

## Similar Apps

Apps like Spotify and YouTube Music use similar ranking ideas but at much larger scale with richer signals. They combine:
- Collaborative filtering: users with similar listening behavior
- Content-based filtering: similar song/audio features
- Context signals: time, session behavior, skip patterns, and trends

This class MVP keeps the logic transparent so it is easy to inspect and explain.

## Getting Started

### Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the app.

Commands:

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main

### Running Tests

python -m pytest

## Experiments You Tried

1. Pop happy user with high target energy.
Result: pop and indie pop songs with happy mood were ranked highest.

2. Lower target energy by 0.3.
Result: chill/lofi songs moved higher because energy distance became smaller.

3. Toggle acoustic preference on.
Result: tracks with high acousticness gained points and rose in ranking.

## Limitations and Risks

- Tiny catalog of 10 songs limits coverage and diversity.
- No real listening-history feedback loop.
- No handling of novelty, fairness, or diversity constraints.
- Can over-favor direct feature matches and miss exploratory recommendations.

## Reflection

Building this MVP showed how quickly a recommender can be created from a clear scoring function, and how much outcomes depend on feature design and weighting choices. Even with a simple model, ranking behavior is interpretable and easy to debug.

It also highlights why production apps like Spotify and YouTube Music need hybrid systems: collaborative filtering for discovery, content-based matching for consistency, and context-aware ranking for timing and relevance. Bias and fairness risks can appear early when data is small or narrow.

For deeper analysis, see [model_card.md](model_card.md).

