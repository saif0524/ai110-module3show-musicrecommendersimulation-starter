# Music Recommender Simulation

## Project Summary

This MVP builds a rule-based music recommender that scores songs by genre match, mood match, energy closeness, and acoustic preference. It loads a small CSV catalog, computes a score for each song, sorts by score, and returns top recommendations with plain-language explanations.

## How The System Works

The recommender uses song-level features and user preferences, then computes a weighted score.

### Data Flow Plan (Input -> Process -> Output)

Input (User Preferences):
- Favorite genre
- Favorite mood
- Target energy
- Acoustic preference

Process (Scoring Loop):
- Load `data/songs.csv`
- For each song, compute a score using:
	- Genre match: +2.0
	- Mood match: +1.0
	- Energy similarity points (higher when song energy is closer to target)
	- Acoustic preference alignment bonus
- Save each song with score and explanation

Output (Ranking):
- Sort songs by score descending
- Break ties with song id for stable ordering
- Return Top-K recommendations with short reasons

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
- Genre exact or close match: +2.0
- Mood match: +1.0
- Energy similarity: up to +1.5, based on absolute distance
- Acoustic preference alignment: +1.0

Top-k selection:
- Score each song
- Sort by descending score
- Return top k with short explanations



## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate      # Mac or Linux
.venv\Scripts\activate         # Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in tests/test_recommender.py.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

- Tiny catalog of 10 songs limits coverage and diversity.
- No real listening-history feedback loop.
- No handling of novelty, fairness, or diversity constraints.
- Can over-favor direct feature matches and miss exploratory recommendations.

## Reflection

Read and complete model_card.md.

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
