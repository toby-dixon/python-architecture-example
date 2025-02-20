from fastapi import APIRouter

from app.util.logging import auto_log

from app.controllers.example_controller import example_controller

def register_routes() -> APIRouter:
    router = APIRouter()

    @router.get("/example")
    @auto_log
    def example_route():
        return example_controller()

    return router