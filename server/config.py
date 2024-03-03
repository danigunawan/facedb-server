"""
This module contains all the configuration for the application.
"""

import os

# Vector database
QDRANT_API_URL = os.getenv("QDRANT_API_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Should be MinIO or AWS
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://localhost:9000")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_REGION = os.getenv("S3_REGION", "eu-west-1")

# General encryption key
SECRET_KEY = os.getenv("SECRET_KEY")
