import csv
from typing import Any, List, Dict, Tuple
from dataclasses import dataclass


GENRE_MATCH_POINTS = 2.0
MOOD_MATCH_POINTS = 1.0
MAX_ENERGY_SIMILARITY_POINTS = 1.5


def _normalize_text(value: Any) -> str:
    return str(value).strip().lower()


def _score_song_values(
    user_genre: str,
    user_mood: str,
    target_energy: float,
    likes_acoustic: bool,
    song_genre: str,
    song_mood: str,
    energy: float,
    acousticness: float,
) -> Tuple[float, List[str]]:
    score = 0.0
    reasons: List[str] = []

    if user_genre and song_genre:
        if _normalize_text(user_genre) == _normalize_text(song_genre) or _normalize_text(user_genre) in _normalize_text(song_genre) or _normalize_text(song_genre) in _normalize_text(user_genre):
            score += GENRE_MATCH_POINTS
            reasons.append(f"genre matches {song_genre}")

    if user_mood and song_mood:
        if _normalize_text(user_mood) == _normalize_text(song_mood):
            score += MOOD_MATCH_POINTS
            reasons.append(f"mood matches {song_mood}")

    energy_gap = abs(float(target_energy) - float(energy))
    energy_score = max(0.0, MAX_ENERGY_SIMILARITY_POINTS - (energy_gap * MAX_ENERGY_SIMILARITY_POINTS))
    score += energy_score
    if energy_gap <= 0.15:
        reasons.append("energy is close to the target")

    acousticness_value = float(acousticness)
    if likes_acoustic and acousticness_value >= 0.6:
        score += 1.0
        reasons.append("leans acoustic")
    elif not likes_acoustic and acousticness_value <= 0.4:
        score += 1.0
        reasons.append("stays away from acoustic-heavy tracks")

    return score, reasons


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = [
            (
                _score_song_values(
                    user.favorite_genre,
                    user.favorite_mood,
                    user.target_energy,
                    user.likes_acoustic,
                    song.genre,
                    song.mood,
                    song.energy,
                    song.acousticness,
                )[0],
                song,
            )
            for song in self.songs
        ]
        scored_songs.sort(key=lambda item: (-item[0], item[1].id))
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = _score_song_values(
            user.favorite_genre,
            user.favorite_mood,
            user.target_energy,
            user.likes_acoustic,
            song.genre,
            song.mood,
            song.energy,
            song.acousticness,
        )
        if reasons:
            return f"Score {score:.2f} because it " + ", ".join(reasons) + "."
        return f"Score {score:.2f} because it is a reasonable overall match."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict[str, Any]] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    return _score_song_values(
        user_prefs.get("genre", ""),
        user_prefs.get("mood", ""),
        float(user_prefs.get("energy", 0.5)),
        bool(user_prefs.get("likes_acoustic", False)),
        song.get("genre", ""),
        song.get("mood", ""),
        float(song.get("energy", 0.0)),
        float(song.get("acousticness", 0.0)),
    )

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "general fit"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: (-item[1], item[0].get("id", 0)))
    return scored_songs[:k]
