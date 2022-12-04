from sqlalchemy import create_engine
import models

engine = create_engine(
    "mysql+pymysql://extuser:password@docker-for-desktop/external_db",
    echo=True,
    future=True,
)

models.Base.metadata.create_all(engine)
