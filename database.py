from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL de la base de datos para conectar a SQLite
SQLALCHEMY_DATABASE_URL = (
    "postgresql://db_login_8pok_user:HihVbRsMtBzdehPfp6pBlTLnZrNztJXU@localhost:5432/db_login_8pok"
)
# Crea una instancia del motor de la base de datos
# connect_args={"check_same_thread": False} es necesario para SQLite en aplicaciones multihilo
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea una fábrica de sesiones para interactuar con la base de datos
# autocommit=False asegura que las transacciones no se confirmen automáticamente
# autoflush=False evita que los cambios se envíen automáticamente a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para definir modelos de SQLAlchemy
Base = declarative_base()
