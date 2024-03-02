"""
Implementation of the face search.
"""


class FaceDB:
    """
    Class to handle the face database
    """

    def __init__(self):
        self.faces = []

    def search(self, image: UploadFile) -> list[str]:
        """
        Search for similar faces in the database
        """
        return ["https://picsum.photos/id/400/400"] * 5

    def _get_existing_images(self) -> list[str]:
        """
        Get the existing images in the database
        """
        return ["https://picsum.photos/id/400/400"] * 5
