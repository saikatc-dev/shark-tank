"""CLI for Pitch to the AI Sharks.

python run.py                 # judge the bundled sample pitch (TiffinAI)
python run.py --demo          # same as above
python run.py mypitch.txt     # judge a pitch from a text file
"""

import os
import sys

from panel import run_panel

HERE = os.path.dirname(os.path.abspath(__file__))


def load_pitch(args) -> str:
    files = [a for a in args if not a.startswith("-")]
    path = files[0] if files else os.path.join(HERE, "sample_pitch.txt")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    pitch = load_pitch(sys.argv[1:])
    print("\n🦈  PITCH TO THE AI SHARKS", flush=True)
    print("=" * 60, flush=True)
    print("The founder pitches… the panel deliberates…\n", flush=True)

    result = run_panel(pitch)

    for v in result["final"]:
        badge = "💰 INVEST" if v.stance.upper().startswith("INVEST") else "🚫 PASS"
        print(f"{badge} — {v.shark}", flush=True)
        if v.offer:
            print(f"   Offer: {v.offer}", flush=True)
        print(f"   {v.reasoning}\n", flush=True)

    print("-" * 60, flush=True)
    print(f"🎤 HOST: {result['summary']}", flush=True)


if __name__ == "__main__":
    main()
