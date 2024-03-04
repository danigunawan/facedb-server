"""
Implementation of the face search.
"""

from time import sleep

from fastapi import UploadFile


class ReadOnlyFaceDB:
    """
    Class to handle the face database
    """

    def __init__(self):
        self.faces = self._get_existing_images()

    def search(self, image: UploadFile) -> list[str]:
        """
        Search for similar faces in the database
        Returns a list of URLs of the similar faces
        """
        sleep(2)
        return ["https://picsum.photos/id/400/400"] * 5

    def _get_existing_images(self) -> list[str]:
        """
        Get the existing images in the database
        """
        return ["https://picsum.photos/id/400/400"] * 5
