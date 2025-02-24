import numpy as np
from tschm.flight import Server


class BallServer(Server):
    def f(self, matrices: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
        self.logger.info(f"Matrices: {matrices.keys()}")
        return {key : 2*value for key, value in matrices.items()}


if __name__ == "__main__":  # pragma: no cover
    BallServer.start()
