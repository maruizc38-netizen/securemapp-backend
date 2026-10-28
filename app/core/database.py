from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. La URL de conexión a tu base de datos MySQL local
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/securemapp"

# 2. El motor (Engine) que maneja el canal de comunicación con MySQL
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# 3. La fábrica de sesiones para hacer operaciones (INSERT, SELECT, etc.)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. La clase Base de la cual heredarán todas nuestras tablas
Base = declarative_base()

# 5. Dependencia para inyectar y cerrar la sesión de base de datos en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()