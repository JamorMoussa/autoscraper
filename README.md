# AutoScraper

**AutoScraper** is a JSON-based scraping library that allows you to extract content from websites using the power of CSS selectors. It supports **classes**, **IDs**, and even **attributes**. You can use it in two ways: directly in code or via an HTTP API.

## 🚀 Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/JamorMoussa/autoscraper.git
cd autoscraper
````

### 2. Install dependencies

We recommend using a virtual environment. With `uv`, installation is straightforward:

```bash
uv sync
```

### 3. Start the server

Since AutoScraper can be used both programmatically and via HTTP requests, let’s start with the server mode:

```bash
uv run uvicorn main:app --reload
```

If successful, you should see something like this:

```bash
INFO:     Will watch for changes in these directories: ['/home/moussa/Documents/programming/autoscraper']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [115132] using StatReload
INFO:     Started server process [115147]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Your FastAPI server is now up and running! 🎉

continue .............
