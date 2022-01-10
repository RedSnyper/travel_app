from travel_app.models import user, trekdestination, itenary, comment, vote
from .db import engine

async def add_models_to_database() -> None:
    user.Base.metadata.create_all(bind=engine)
    trekdestination.Base.metadata.create_all(bind=engine)
    itenary.Base.metadata.create_all(bind=engine)
    comment.Base.metadata.create_all(bind=engine)
    vote.Base.metadata.create_all(bind=engine)
