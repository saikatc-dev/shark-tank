# Pitch to the AI Sharks

Pitch a startup to a panel of AI investors. The sharks evaluate the pitch, debate, and give their verdicts.

## Setup

Install the dependencies and add your Groq API key:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `GROQ_API_KEY`.

## Run

```bash
streamlit run app.py
```

Choose a bundled sample pitch or enter your own. To run a pitch file from the command line:

```bash
python run.py sample_pitches/fleetshift.txt
```

Run the offline checks with `python test_offline.py`.
