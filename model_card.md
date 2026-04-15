# Model Card: Music Recommender Simulation

## 1. Model Name

VibeMatch MVP 1.0

## 2. Intended Use

This model suggests top songs from a small local catalog based on user taste inputs for genre, mood, and energy, plus a simple acoustic preference. It is designed for classroom exploration and explainability, not for production deployment.

## 3. How the Model Works

Each song is scored against a user profile using four components:
- Genre alignment
- Mood alignment
- Energy distance from the user target
- Acousticness match with the user preference

The model adds weighted points for each component, then ranks songs by total score. It also returns a short explanation listing which components matched.

## 4. Data

The dataset contains 10 songs in a CSV file with fields including title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

Represented styles include pop, lofi, rock, ambient, jazz, synthwave, and indie pop with moods such as happy, chill, focused, intense, relaxed, and moody.

The dataset is tiny and synthetic, so many real listening patterns are missing.

## 5. Strengths

- Transparent and easy-to-debug ranking behavior
- Explanations are human-readable and tied to explicit features
- Performs reasonably for users with clearly defined preferences

## 6. Limitations and Bias

- Very small catalog leads to limited recommendation diversity
- No collaborative signal from other users
- No history-aware personalization across sessions
- Weight choices can over-favor direct genre matches and reduce discovery
- Data composition may over-represent certain vibe clusters

## 7. Evaluation

Evaluation was done through:
- Manual profile testing with multiple preference combinations
- Checking if top results matched expected vibe and energy
- Running unit tests for recommendation ordering and explanation output

Compared with Spotify or YouTube Music, this model is far simpler. Those systems combine collaborative filtering, content-based features, and rich behavior/context logs. This MVP captures only content-style matching from a single profile snapshot.

## 8. Future Work

- Add collaborative signals from multiple users
- Add diversity constraints so top results are less repetitive
- Include sequence/session context and skip behavior
- Calibrate and learn weights instead of hand-tuning
- Expose adjustable controls in a small UI

## 9. Personal Reflection

This project showed that even a small, interpretable scoring system can generate plausible recommendations quickly. The biggest insight was how strongly recommendations depend on feature design and weighting decisions.

It also made clear why real-world systems like Spotify and YouTube Music need hybrid recommenders: collaborative filtering improves discovery, while content-based signals preserve consistency with user taste.
