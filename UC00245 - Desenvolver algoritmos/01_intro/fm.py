from dataclasses import dataclass


@dataclass(frozen=True)
class Constantes:
    PI: float = 3.14159
    MAX_USERS: int = 100
