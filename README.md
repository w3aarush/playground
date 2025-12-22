# RobotX Playground

Lightweight collection of example scripts for chatbots and basic clustering utilities. This repository contains two interactive chatbot demos (one semantic, one LangChain-based) and small DBSCAN/distance utilities used for learning and experimentation.

## Contents
- **Semantic chatbot**: [chatbot_semantic/sematic_chatbot.py](chatbot_semantic/sematic_chatbot.py) — simple semantic search chatbot using `sentence-transformers` and an editable `chatdata.csv` dataset.
- **LangChain chatbot**: [langchain/chatbot.py](langchain/chatbot.py) — minimal local LangChain conversation loop using `ChatOllama` (requires local or configured Ollama/LLM support).
- **DBSCAN / distance utilities**: [dbscan/dbscan.py](dbscan/dbscan.py) and [dbscan/dbscan_niraj.py](dbscan/dbscan_niraj.py) — scripts that compute pairwise Euclidean distances and demonstrate basic clustering-related data prep.

## Project overview

This workspace is intended as an educational playground for exploring:
- embedding-based retrieval chatbots (semantic matching with SentenceTransformers),
- a minimal conversational interface using LangChain and a local chat model, and
- simple distance-matrix generation used as a preprocessing step for clustering algorithms.

Key files:

- [chatbot_semantic/sematic_chatbot.py](chatbot_semantic/sematic_chatbot.py): loads `chatdata.csv`, encodes user messages with `sentence-transformers/all-MiniLM-L6-v2`, finds the most similar existing user input, and either returns the associated response or prompts the user to provide a new response (which is appended to `chatdata.csv`). Use this to see a minimal online-learning chatbot.
- [chatbot_semantic/chatdata.csv](chatbot_semantic/chatdata.csv): the small CSV dataset of user prompts and responses used by the semantic chatbot.
- [langchain/chatbot.py](langchain/chatbot.py): minimal interactive loop using `ConversationChain` and `ChatOllama`. Intended as an example for local LLM-driven chat via LangChain.
- [dbscan/dbscan.py](dbscan/dbscan.py): reads `sample_data.csv`, computes pairwise Euclidean distances and writes `euclidian_distance.csv`.
- [dbscan/dbscan_niraj.py](dbscan/dbscan_niraj.py): small hard-coded example that prints a distance matrix for demonstration.

## Requirements

- Python 3.11+ (this workspace includes a `envplay` Python 3.13 virtualenv).
- Core packages: see [langchain/requirements.txt](langchain/requirements.txt) for LangChain dependencies.
- Additional packages used by other scripts: `sentence-transformers`, `pandas`, `numpy`.

Suggested install (from project root):

```bash
# create and activate a venv (adjust python path as needed)
python -m venv .venv
source .venv/bin/activate

# install langchain dependencies
pip install -r langchain/requirements.txt

# install other requirements
pip install sentence-transformers pandas numpy
```

If you prefer the included `envplay` virtual environment, use its `python` binary at `envplay/bin/python`.

## Usage

Semantic chatbot (interactive, editable dataset):

```bash
python chatbot_semantic/sematic_chatbot.py
```

- Type messages at the `user:` prompt. If the bot cannot find a match above the threshold (0.75), it will ask you for the correct response and append that pair to `chatdata.csv`.
- Type `exit` to save any new entries and quit.

LangChain chatbot (local model):

```bash
python langchain/chatbot.py
```

- Requires access to a compatible chat model backend (the example uses `ChatOllama`). Configure your local model environment accordingly.

DBSCAN / distance utilities:

```bash
python dbscan/dbscan.py         # generates euclidian_distance.csv from sample_data.csv
python dbscan/dbscan_niraj.py  # prints a small distance matrix example
```

## Data

- `chatbot_semantic/chatdata.csv` — example conversational pairs used by the semantic chatbot.
- `dbscan/sample_data.csv` — input for the distance computation performed by `dbscan/dbscan.py`.

## Notes & Next steps

- The semantic chatbot is intentionally simple and meant for learning — consider replacing the flat CSV with a lightweight vector DB (FAISS, Chroma, Milvus) for scale.
- The LangChain example assumes a locally available chat model; adapt the `ChatOllama` usage to your deployment or replace with an API-backed LLM.
- Add unit tests, a `requirements.txt` at the repo root, and basic CI for reproducible runs.

## Contributing

Improvements are welcome. Suggested PRs:
- add a consolidated `requirements.txt` or `pyproject.toml` for reproducible environments,
- add tests for the chatbot logic and DBSCAN preprocessing,
- package the semantic chatbot into a small CLI with flags for thresholds and model selection.

## License

This repository does not include a license file. Add one (for example MIT) if you intend to publish or share the code publicly.
