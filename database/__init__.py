from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fast_inventory_db"

POSTGRES_ROOT_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

root_engine = create_engine(POSTGRES_ROOT_URL, isolation_level='AUTOCOMMIT', pool_pre_ping=True)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_database_if_not_exists():
    print(f"Intentando conectar a la base de datos raiz: {POSTGRES_ROOT_URL}")
    try:
        with root_engine.connect() as connection:
            result = connection.execute(
                text(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'")
            )
            if not result.scalar_one_or_none():
                print(f"La base de datos '{DB_NAME}' no existe Creandola...")
                connection.execute(text(f"CREATE DATABASE {DB_NAME}"))
                print(f"Base de datos '{DB_NAME}' creada exitosamente")
            else:
                print(f"La base de datos '{DB_NAME}' ya existe")

        print("Creando/verificando tablas en la base de datos")
        Base.metadata.create_all(bind=engine)
        print("Tablas verificadas y creadas si no existian")

    except OperationalError as e:
        print(f"Error de conexion u operacional con la base de datos: {e}")
        print("Asegurate de que PostgreSQL este corriendo y las credenciales sean correctas")
        raise
    except Exception as e:
        print(f"Ocurrio un error inesperado al inicializar la base de datos: {e}")
        raise

def get_db():
    """
    Obtiene una sesión de base de datos para las dependencias de FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()