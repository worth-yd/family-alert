import os


# Base configuration class
class Config:
    # Secret key for securely signing session cookies (generate your own unique key)
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")

    # Track modifications of objects (for SQLAlchemy). Set to False to disable.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database URI for SQLAlchemy (default to SQLite if no other DB is specified)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")


# Development-specific configuration
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEV_DATABASE_URI", "postgresql+psycopg2://dev_user:password@localhost/dev_db"
    )


# Production-specific configuration
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "PROD_DATABASE_URI",
        "postgresql+psycopg2://prod_user:password@localhost/prod_db",
    )


# Testing-specific configuration
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI", "sqlite:///test.db")
    # Optionally disable CSRF for easier testing
    WTF_CSRF_ENABLED = False


# Map of configurations for easy selection
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
