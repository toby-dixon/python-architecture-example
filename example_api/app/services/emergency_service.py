from typing import *
from typing_extensions import *

from app.util.logging import add_log

def emergency_service() -> str:
    add_log("EMERGENCY", "This is an example emergency message")
    return "Emergency!"