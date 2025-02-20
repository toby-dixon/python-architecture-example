from typing import *
from typing_extensions import *

from pydantic import BaseModel


class ExampleModel(BaseModel):
    messages: List[str]