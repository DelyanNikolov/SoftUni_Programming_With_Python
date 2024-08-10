from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import seed
from helpers import session_decorator
from models import Recipe

engine = create_engine("postgresql+psycopg2://postgres:123@localhost/sqlalchemy_db")
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions,
    )

    session.add(new_recipe)


for name, ingredients, instructions in seed.recipes:
    create_recipe(name, ingredients, instructions)
