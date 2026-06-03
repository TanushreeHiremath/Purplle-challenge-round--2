from services.api_service.database.models import Base
from services.api_service.database.session import engine

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")