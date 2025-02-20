import contextvars
import inspect

from typing import *
from typing_extensions import *

from datetime import datetime
from functools import wraps
from pydantic import BaseModel, model_validator, Field

class PSR3_Log(BaseModel):
    timestamp: str
    loglevel: str
    message: str
    context: Dict[str, Any] = Field(default={})

    @model_validator(mode='after')
    def validate_model(self) -> Self:
        self.loglevel = self.loglevel.upper()

        if self.loglevel not in ['DEBUG', 'INFO', 'NOTICE', 'WARNING', 'ERROR', 'CRITICAL', 'ALERT', 'EMERGENCY']:
            raise ValueError("Invalid log level")

        frame = inspect.currentframe().f_back
        filename = frame.f_code.co_filename
        line_number = frame.f_lineno
        
        self.context['line_number'] = line_number
        self.context['filename'] = filename

        return self

log_context = contextvars.ContextVar('log_context', default={})

def add_log(loglevel: str, message: str, context: Dict[str, Any] = {}) -> None:
    """
    Adds a log to the current context.

    Args:
        loglevel (str): DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL, ALERT, EMERGENCY
        message (str): _description_
        context (dict, optional): _description_. Defaults to {}.
    """
    log = PSR3_Log(
        timestamp=datetime.now().isoformat(),
        loglevel=loglevel,
        message=message,
        context=context
    )
    
    logs = log_context.get()
    logs.append(log)
    log_context.set(logs)

def auto_log(func):
    """
    Decorator for route handlers that:
        1. Initialises the log context
        2. Executes the function (which can call add_log anywhere)
        3. Retrieves collected logs
        4. Wraps the original response in the final format.
    Args:
        func (_type_): The route handler function 
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = log_context.set([])
        try:
            data = func(*args, **kwargs)
            logs = log_context.get()
            
            return {
                "data": data,
                "logs": [log.dict() for log in logs]
            }
        finally:
            log_context.reset(token)
        
    return wrapper