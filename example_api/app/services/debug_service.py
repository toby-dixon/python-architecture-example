from typing import *
from typing_extensions import *

from app.util.logging import add_log

def debug_service() -> str:
    add_log("DEBUG", "This is an example debug message")
    return "Debug!"