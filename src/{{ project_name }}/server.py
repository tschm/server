import numpy as np
from tschm.flight import Server


class TestServer(Server):
    def f(self, matrices: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
        self.logger.info(f"Matrices: {matrices.keys()}")
        return {key : 2*value for key, value in matrices.items()}


# needed for uv run
def main():
    TestServer.start()

if __name__ == "__main__":  # pragma: no cover
    main()

    from tschm.flight import Client
    with Client(location="grpc://127.0.0.1:5555") as client:
        output = client.compute(command="compute", data={"input": np.array([1,2,3])})
        print(output)
