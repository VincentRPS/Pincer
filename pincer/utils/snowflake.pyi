class Snowflake(int):
    def __init__(self, _) -> None: ...
    @classmethod
    def __factory__(cls, string: str) -> Snowflake: ...
    @classmethod
    def from_string(cls, string: str): ...
    @property
    def timestamp(self) -> int: ...
    @property
    def worker_id(self) -> int: ...
    @property
    def process_id(self) -> int: ...
    @property
    def increment(self) -> int: ...
    @property
    def unix(self) -> int: ...
