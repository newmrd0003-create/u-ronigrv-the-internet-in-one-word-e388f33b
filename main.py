"""The Internet in One Word — deterministic entry writer.

Entry (final): "Scrollhole"
- Draft 1 was "Brainrot": funny and short, but by 2026 it is the first word
  that comes to mind for internet natives (weak on the surprise criterion)
  and it names a mental state/mood rather than the internet itself.
- Final "Scrollhole" (scroll + rabbit hole): a fresh coinage, so it is
  surprising; it describes the whole-internet experience — open one tab,
  fall in, emerge hours later — which is true of the entire internet, not
  one app; and it lands in one beat at 10 characters, instantly readable.

Every run writes the exact same entry to <OUTPUT_DIR>/entry.txt (UTF-8).
"""

import hashlib
import os

ENTRY = "Scrollhole"


def validate(entry):
    """Return (True, []) if entry is a valid single-word entry, else (False, [reasons])."""
    errors = []
    if not isinstance(entry, str):
        return False, ["entry is not a string"]
    if not (1 <= len(entry) <= 30):
        errors.append("entry must be 1-30 characters, got %d" % len(entry))
    if entry.strip() == "":
        errors.append("entry must not be whitespace only")
    if any(ch.isspace() for ch in entry):
        errors.append("entry must be a single word (no whitespace)")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must not contain a newline")
    return (len(errors) == 0), errors


def main():
    valid, errors = validate(ENTRY)
    if not valid:
        raise ValueError("invalid entry: %s" % "; ".join(errors))
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print("entry: %s" % ENTRY)
    print("characters: %d" % len(ENTRY))
    print("sha256: %s" % digest)
    print("wrote: %s" % path)


if __name__ == "__main__":
    main()
