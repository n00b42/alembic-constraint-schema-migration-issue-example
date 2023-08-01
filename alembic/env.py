from alembic import context
from sqlalchemy import Column, create_engine, ForeignKey, Integer, Table, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


################################################################################

# Test Data

# CREATE USER legacy WITH PASSWORD 'legacy';
# CREATE DATABASE mydatabase WITH OWNER legacy;
# GRANT ALL PRIVILEGES ON DATABASE mydatabase to legacy;
# \c mydatabase
# CREATE TABLE users (id int PRIMARY KEY, name varchar NOT NULL);
# INSERT INTO users VALUES (1, 'Aaa'), (2, 'Bbb');
# CREATE USER myuser WITH PASSWORD 'myuser';
# CREATE SCHEMA myschema AUTHORIZATION myuser;
# GRANT REFERENCES (id) ON public.users TO myuser;

# Idea
# There is a legacy read-only application using schema "public"
# Another application wants to have foreign key constraints on the legacy user table

################################################################################

myengine = create_engine(f"postgresql://myuser:myuser@localhost:5432/mydatabase")

LEGACY_SCHEMA = "public"
MAIN_SCHEMA = "myschema"

class Base(DeclarativeBase):
    pass

Table("users", Base.metadata, Column("id", Integer, primary_key=True), schema=LEGACY_SCHEMA)

class Test(Base):
    __tablename__ = "test"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(LEGACY_SCHEMA + ".users.id", ondelete="CASCADE"))
    __table_args__ = {"schema": MAIN_SCHEMA}


################################################################################


def include_object(object, name, type_, reflected, compare_to):
    """Filter out any tables not in MAIN_SCHEMA"""
    if type_ == "table" and object.schema != MAIN_SCHEMA:
        return False
    return True


def run_migrations_online() -> None:
    with myengine.connect() as connection:
        connection.execute(text(f'set search_path to "{MAIN_SCHEMA}"'))
        connection.commit()
        connection.dialect.default_schema_name = MAIN_SCHEMA
        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
            # version_table_schema=MAIN_SCHEMA,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    raise NotImplementedError
else:
    run_migrations_online()
