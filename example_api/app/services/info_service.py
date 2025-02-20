from typing import *
from typing_extensions import *

from app.util.logging import add_log

def info_service() -> str:
    add_log("INFO", "This is an example info message")
    return "Info!"