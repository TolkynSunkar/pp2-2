from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_json_file(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    print("=== 1) json.loads() (string -> python) ===")
    s = '{"name": "Sunkar", "age": 21, "skills": ["python", "c++"]}'
    obj = json.loads(s)
    print("String:", s)
    print("Parsed dict:", obj)
    print()

    print("=== 2) json.dumps() (python -> string) ===")
    data = {
        "university": "KBTU",
        "city": "Almaty",
        "ramadan": True,
        "numbers": [1, 2, 3],
    }
    dumped = json.dumps(data, ensure_ascii=False, indent=2)
    print(dumped)
    print()

    print("=== 3) Read sample-data.json (if exists) ===")
    sample_path = HERE / "sample-data.json"
    if sample_path.exists():
        sample = load_json_file(sample_path)
        print("Loaded sample-data.json type:", type(sample).__name__)

        # Try to do something useful no matter the structure
        if isinstance(sample, list):
            print("Items count:", len(sample))
            preview = sample[:3]
        elif isinstance(sample, dict):
            print("Keys:", list(sample.keys())[:10])
            preview = dict(list(sample.items())[:3])
        else:
            preview = sample

        print("Preview:", preview)

        # Create a small report and save it
        report = {
            "source_file": str(sample_path.name),
            "python_type": type(sample).__name__,
        }
        if isinstance(sample, list):
            report["count"] = len(sample)
        elif isinstance(sample, dict):
            report["count_keys"] = len(sample.keys())

        out_path = HERE / "output-data.json"
        save_json_file(out_path, report)
        print(f"\nSaved report to: {out_path.name}")
    else:
        print("sample-data.json not found in this folder.")
        print("Tip: put sample-data.json in the same folder as json.py")
    print()


if __name__ == "__main__":
    main()