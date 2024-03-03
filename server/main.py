"""
FastAPI main module

GET / - returns a FastUI with a form to upload a file with buttons to search or add a face
POST /search-face - returns FastUI at / with results (links to similar images from S3)
"""

from time import sleep

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastui import (
    FastUI,
    AnyComponent,
    prebuilt_html,
    components as c,
)
from fastui.events import BackEvent

from forms import SearchFaceForm
from services.face_search import ReadOnlyFaceDB

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def main_page() -> list[AnyComponent]:
    """
    Returns the main UI page
    """
    return [
        c.Page(
            components=[
                c.Heading(text="Welcome to the Face Database", level=2),
                c.ModelForm(
                    model=SearchFaceForm,
                    display_mode="page",
                    submit_url="/api/search-face",
                    loading=[c.Spinner(text="Searching...")],
                ),
            ]
        ),
    ]


@app.post("/api/search-face", response_model=FastUI, response_model_exclude_none=True)
async def search_face(image: UploadFile = File(...)) -> list[AnyComponent]:
    """
    Returns the main UI page with the results of the search after doing an operation
    on the image file
    """
    face_db = ReadOnlyFaceDB()
    results = face_db.search(image)

    return [
        c.Page(
            components=[
                c.Link(
                    components=[c.Text(text="Back to main page")],
                    on_click=BackEvent(),
                ),
                c.Heading(text="Search Results", level=3),
                c.Text(text="Here are the results of your search"),
            ]
            + [
                c.Image(
                    src=url,
                    referrer_policy="no-referrer",
                    class_name="border rounded",
                    loading="lazy",
                    width=200,
                    height=200,
                )
                for url in results
            ]
        )
    ]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Face Database"))
