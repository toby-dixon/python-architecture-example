from typing import *
from typing_extensions import *

from app.util.logging import add_log

def critical_service() -> str:
    add_log("CRITICAL", "This is an example critical message")
    return "Critical!"