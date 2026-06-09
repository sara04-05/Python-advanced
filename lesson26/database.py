import sqlite3
from models import Recipe, RecipeCreate
from models import CategoryCreate, Category

def create_connection():
    connection = sqlite3.connect("recipe.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            ingredients INTEGER NOT NULL,
            category_id INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def create_category(category: CategoryCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO categories (name) VALUES (?)",
        (category.name,)
    )

    connection.commit()
    category_id = cursor.lastrowid
    connection.close()

    return category_id

def read_categories():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()

    connection.close()

    categories = [
        Category(
            id=row["id"],
            name=row["name"]
        )
        for row in rows
    ]

    return categories

def read_category(category_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM categories WHERE id = ?",
        (category_id,)
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return Category(
        id=row["id"],
        name=row["name"]
    )


def create_recipe(recipe: RecipeCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO recipes (name, description, ingredients, category_id) VALUES (?, ?, ?, ?)",
        (recipe.name, recipe.description, recipe.ingredients, recipe.category_id)
    )
    connection.commit()
    recipe_id = cursor.lastrowid
    connection.close()

    return recipe_id


def read_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    connection.close()
    recipes = [
        Recipe(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            ingredients=row["ingredients"],
            category_id=row["category_id"]
        )
        for row in rows
    ]
    return recipes

def read_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return Recipe(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        ingredients=row["ingredients"],
        category_id=row["category_id"]
    )


def update_recipe(recipe_id: int, recipe: RecipeCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE recipes
        SET name = ?, description = ?, ingredients = ?, category_id = ?
        WHERE id = ?
        """,
        (
            recipe.name,
            recipe.description,
            recipe.ingredients,
            recipe.category_id,
            recipe_id
        )
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()

    return updated > 0


def delete_recipe(recipe_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM recipes WHERE id = ?",
        (recipe_id,)
    )

    connection.commit()
    deleted = cursor.rowcount
    connection.close()

    return deleted > 0