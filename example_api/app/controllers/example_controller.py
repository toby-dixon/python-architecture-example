from app.util.logging import add_log

from app.models.example_model import ExampleModel

from app.services.emergency_service import emergency_service
from app.services.critical_service import critical_service
from app.services.alert_service import alert_service
from app.services.debug_service import debug_service
from app.services.error_service import error_service
from app.services.info_service import info_service
from app.services.notice_service import notice_service
from app.services.warning_service import warning_service

def example_controller() -> ExampleModel:
    
    add_log("INFO", "Getting messages", {"controller": "example_controller"})
    
    messages = []

    messages.append(emergency_service())
    messages.append(critical_service())
    messages.append(alert_service())
    messages.append(debug_service())
    messages.append(error_service())
    messages.append(info_service())
    messages.append(notice_service())
    messages.append(warning_service())
    
    return ExampleModel(messages=messages) 
    
    