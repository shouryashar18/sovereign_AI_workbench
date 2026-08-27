from fastapi import FastAPI
from app.database import db
from app.routers.workspace import router as workspace_router
from app.routers.documents import router as document_router
from app.routers.analysis import router as analysis_router
from app.routers import analysis


app = FastAPI(
    title="Sovereign Industrial AI Workbench",
    version="1.0.0"
)
app.include_router(analysis_router)
app.include_router(workspace_router)
app.include_router(document_router)
app.include_router(analysis.router)

@app.get("/")
def root():
    return {
        "message": "Backend is running"
    }


@app.get("/db-test")
def database_test():
    try:
        db.command("ping")

        return {
            "status": "success",
            "message": "MongoDB connected successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
