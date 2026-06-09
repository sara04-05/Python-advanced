from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class Category(CategoryCreate):
    id: int


class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: int
    category_id: int

class Recipe(RecipeCreate):
    id: int