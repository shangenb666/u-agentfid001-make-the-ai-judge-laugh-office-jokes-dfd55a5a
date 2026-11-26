"""Entry program for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life (under 200 characters)
to entry.txt in the output directory. The joke is a fixed string in
this file, so every run produces exactly the same bytes. No network,
no randomness, standard library only.
"""

import os

LINE = "I CC'd my boss on an email to myself so he'd think I'm productive. He replied-all: 'Same.'"

MAX_CHARS = 199


def main() -> int:
    text = LINE
    if not text or text.isspace():
        print("error: joke must not be blank", flush=True)
        return 1
    if len(text) > MAX_CHARS:
        print("error: joke is over 199 characters", flush=True)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    try:
        os.chmod(path, 0o644)
    except PermissionError:
        pass
    print("wrote {} ({} characters)".format(path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
