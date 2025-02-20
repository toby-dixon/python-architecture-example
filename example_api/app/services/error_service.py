from typing import *
from typing_extensions import *

from app.util.logging import add_log

def error_service() -> str:
    add_log("ERROR", "This is an example error message")
    return "Error!"