from pydantic import BaseModel

class Category(BaseModel):
    name: str
    description: str
    ingredients: int

class Recipe(Category):
    id: int

