from typing import *
from typing_extensions import *

from app.util.logging import add_log

def notice_service() -> str:
    add_log("NOTICE", "This is an example notice message")
    return "Notice!"