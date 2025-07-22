import os

username = os.getenv("USERNAME")
language = os.getenv("LENGUAJE")

print(
    f"Hello, {username}! Welcome to the GitHub Actions Course, your favorite language is {language}."
)
