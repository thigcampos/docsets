import os

import requests
from cyclopts import App

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
IGNORED_FILES_AND_FOLDERS = ["man", "releases", "_", ".", "make", "bat"]

app = App()


def fetch_docs(docset_url: str):
    print("Fetching docs from GitHub")
    r = requests.get(docset_url)
    return r


def filter_files_and_folders(docs):
    accepted_docs = []
    for doc in docs:
        if not any(st in doc["name"].lower() for st in IGNORED_FILES_AND_FOLDERS):
            accepted_docs.append(doc)
    return accepted_docs


@app.command()
def add(docset_url: str) -> None:
    """Add a new docset to the database"""
    response = fetch_docs(docset_url)
    content = response.json()
    valid_docs = filter_files_and_folders(content)
    for doc in valid_docs:
        print(doc["name"], doc["type"])


@app.command()
def remove(docset_name: str) -> None:
    """Remove a docset from the database"""
    pass


@app.command()
def sync():
    """Sync all docsets with remote"""
    pass


@app.default()
def main():
    print("Hello, World!")


if __name__ == "__main__":
    app()
