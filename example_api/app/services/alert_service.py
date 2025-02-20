from typing import *
from typing_extensions import *

from app.util.logging import add_log

def alert_service() -> str:
    add_log("ALERT", "This is an alert error message")
    return "Alert!"