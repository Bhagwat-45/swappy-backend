from app.core.database import Base
from app.models.profile import ProfileTable
from app.models.assignment import AssignmentTable

# This list allows you to control what is exported when 
# someone uses 'from app.models import *'
__all__ = [
    "Base",
    "ProfileTable",
    "AssignmentTable",
]