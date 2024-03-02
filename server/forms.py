"""
Models for the forms used in the application
"""

from typing import Annotated

from fastapi import UploadFile
from fastui.forms import FormFile
from pydantic import BaseModel, Field


class SearchFaceForm(BaseModel):
    """
    Form for the face database
    """

    image: Annotated[UploadFile, FormFile(accept="image/*", max_size=2_000_000)] = (
        Field(
            description="Upload an image with on face in it to search for similar images"
        )
    )
