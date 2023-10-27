import asyncio
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from database.models.base import Base
from dotenv import load_dotenv
# from database.models import TextInput, ParsedText


load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    connectable = context.config.attributes.get("connection", None)
    if connectable is None:
        connectable = create_async_engine(DATABASE_URL)

    if isinstance(connectable, AsyncEngine):
        asyncio.run(run_async_migrations(connectable))
    else:
        do_run_migrations(connectable)


async def run_async_migrations(connectable):
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


run_migrations_online()
