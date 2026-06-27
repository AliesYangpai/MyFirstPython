# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- **Python version**: 3.10.9 (Homebrew-installed)
- **Virtual environment**: `.venv/` — activate with `source .venv/bin/activate`
- **Dependencies**: `openai` (OpenAI SDK, used with DeepSeek's compatible API), `python-dotenv` (env var loading). No `requirements.txt` or `pyproject.toml` exists.
- **API key**: Stored in `.env` as `DEEPSEEK_API_KEY`. Calls DeepSeek API at `https://api.deepseek.com`. `.gitignore` excludes `.env`.

## Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the main script (Anthropic API call)
python main.py

# Run the test script
python test01.py

# Install a new dependency
pip install <package>
```
