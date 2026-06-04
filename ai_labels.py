from dataclasses import dataclass
from typing import Tuple


@dataclass
class Label3D:
    text: str
    x: float
    y: float
    z: float
    color: Tuple[float, float, float] = (1.0, 1.0, 1.0)
    size: int = 12


def create_3d_label(text: str, x: float, y: float, z: float, color: Tuple[float, float, float] = (1.0, 1.0, 1.0), size: int = 12) -> Label3D:
    """Create a text label for a 3D model at coordinates x, y, z."""
    return Label3D(text=text, x=float(x), y=float(y), z=float(z), color=color, size=size)
