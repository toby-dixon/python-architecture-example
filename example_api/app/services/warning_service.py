from typing import *
from typing_extensions import *

from app.util.logging import add_log

def warning_service() -> str:
    add_log("WARNING", "This is an example warning message")
    return "Warning!"