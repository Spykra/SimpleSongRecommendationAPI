from invoke import task

@task
def create_migrations(ctx):
    """Initialize database migrations."""
    ctx.run("docker-compose exec -T app alembic revision --autogenerate -m 'init'")

@task
def run_migrations(ctx):
    """Run database migrations."""
    ctx.run("docker-compose exec -T app alembic upgrade head")
