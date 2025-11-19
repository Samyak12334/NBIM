# NBIM Regulatory News Dashboard

Short Streamlit dashboard that fetches regulatory news and summarizes articles using the OpenAI API.

**Prerequisites**

- Python 3.10+ (or compatible)
- `pip` for installing dependencies
- A valid OpenAI API key (private) with access to a chat/completion model

**Recommended packages**

The project uses: `streamlit`, `openai`, `pandas`, `requests`, `beautifulsoup4`, and `lxml`.

Install dependencies quickly:

```bash
pip install streamlit openai pandas requests beautifulsoup4 lxml
```

**Environment / API Key**

The app expects an environment variable named `OPENAI_API_KEY`. You can provide it either by exporting it in your shell (zsh) or by creating an `openai.envs` (or `.env`) file in the project root.

Example (temporary export in zsh):

```bash
export OPENAI_API_KEY="sk-..."
```

Example `openai.envs` file content (project root):

```text
OPENAI_API_KEY="sk-..."
```

The project contains a tiny env-loader so `openai.envs` or `.env` will be read automatically if present.

**Run the app**

Run with Streamlit (recommended):

```bash
streamlit run dashboard.py
```

Or run directly with Python (non-interactive):

```bash
python dashboard.py
```

**Notes & Safety**

- Keep your `OPENAI_API_KEY` secret. Do not commit it to source control.
- The app fetches external news and calls the OpenAI API; network access and API usage may incur cost.
- If you want to test locally without calling OpenAI, consider temporarily stubbing `client.chat.completions.create` or toggling a dry-run flag.

**Files**

- `dashboard.py` – main Streamlit app and summarization logic
- `openai.envs` – optional file that may contain `OPENAI_API_KEY`


