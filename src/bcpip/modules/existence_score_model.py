#(integrated class version)
import numpy as np

class CalculateScore:
    """Parent class for scoring models used in converting features to scores."""

    def __call__(self, x: np.ndarray) -> np.ndarray:
        return self.calculate(x)

    def calculate(self, x: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class CalculateScoreLogistic(CalculateScore):
    """Scoring model used in converting features (eg. identity) to scores."""

    def calculate(self, x: np.ndarray) -> np.ndarray:
        """Calculate scores from features using logistic function.

        Args:
            x: Features to be converted to scores
        Returns:
            An array of converted scores
        """
        # prob. ver.2
        y = 1 / (1 + np.exp(-1 / 10 * (x - 40)))
        return y
