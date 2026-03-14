# I acknowledge the use of Claude (Anthropic, https://claude.ai/) to create the code in this file.

class ScoreTracker:
    """Tracks wins and draws for both players."""

    def __init__(self):
        self.scores = {"X": 0, "O": 0, "Draws": 0}

    def record_win(self, player):
        """Record a win for the given player."""
        self.scores[player] += 1

    def record_draw(self):
        """Record a draw."""
        self.scores["Draws"] += 1

    def get_scores(self):
        """Return current scores as a formatted string."""
        return f"X: {self.scores['X']}  |  O: {self.scores['O']}  |  Draws: {self.scores['Draws']}"

    def reset(self):
        """Reset all scores to zero."""
        self.scores = {"X": 0, "O": 0, "Draws": 0}