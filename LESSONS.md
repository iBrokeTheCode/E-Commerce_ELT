# Lessons

## Table of Contents

1. [📦 Git LFS (Large File Storage)](#1-git-lfs-large-file-storage)
2. [🌊 Marimo: Code Display Behavior](#2-marimo-code-display-behavior)

## 1. 📦 Git LFS (Large File Storage)

Git LFS (Large File Storage) is an extension for Git that allows you to track and version large files (e.g. `.db`, `.csv`, `.model`) without bloating your repository. Instead of storing the actual file content in Git, it stores a lightweight pointer and pushes the real content to a separate LFS server.

---

### How to Install

```bash
sudo apt install git-lfs
```

After installation, initialize LFS:

```bash
git lfs install
```

---

### How to Use (Basic Example)

1. **Track the file type or name:**

   ```bash
   git lfs track "olist.db"
   ```

2. **Edit `.gitignore` **

   ```bash
   # Ignore all database files
   *.db
   # But include this one (make sure it's tracked with git LFS)
   !olist.db
   ```

3. **Stage the tracking file (`.gitattributes`) and your large file:**

   ```bash
   git add .gitattributes
   git add olist.db
   git commit -m "Track olist.db with Git LFS"
   ```

4. **Push to your remote repo:**

   ```bash
   git push origin main
   ```

## 2. 🌊 Marimo: Code Display Behavior

By default, **Marimo hides the code cells** in the deployed (read-only) version of your app, especially when running as a Hugging Face Space or a `.py` script.

This behavior is intentional and aligns with Marimo’s goal of turning Python notebooks into polished, interactive **data apps** — focusing on the results and UI rather than code.

| Environment                          | Notes                              |
| ------------------------------------ | ---------------------------------- |
| Local Dev Mode (`marimo run app.py`) | Full interactivity + visible code  |
| Deployed App (e.g., HF Spaces)       | Only outputs / UI components shown |

**If you want to show the code:**

You can **explicitly render code** using `mo.ui.code()` or `mo.md()` with fenced code blocks:

```python
code = '''
revenue_by_month_year = query_results[QueryEnum.REVENUE_BY_MONTH_YEAR.value]
revenue_by_month_year
'''

mo.ui.code(code, language="python")
```

Or in Markdown:

````python
mo.md("""```python
revenue_by_month_year = ...
revenue_by_month_year
```""")
````

Or set a global config int hte app header

```py
__marimo__ = {
    "hide_code": False  # or True to hide all
}
```

### 💡 Tip:

If your app is intended as a tutorial or learning resource, you can:

- Create a separate `notebook.md` or `.ipynb` with all code visible
- Link to that from the main app using `mo.md("[View full notebook](./notebook.md)")`
- Use Marimo's UI components to conditionally show/hide code with toggles

  ```python
  show_code = mo.ui.checkbox(value=False, label="Show Code")

  if show_code.value:
      mo.ui.code(code)
  ```

### Set Dark Theme

Review the [documentation](https://docs.marimo.io/guides/configuration/theming/#forcing-dark-mode). In short, add the following snippet at the top of your main app file:

```py
# /// script
# [tool.marimo.display]
# theme = "dark"
# ///
```
