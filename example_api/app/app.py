from fastapi import FastAPI

from app.routes.routes import register_routes

def initialise_app() -> FastAPI:
    
    app = FastAPI()
    app.include_router(register_routes())

    return app