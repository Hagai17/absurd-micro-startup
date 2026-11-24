"""Write one absurd micro-startup pitch to /output/entry.txt.

The entry is a single sentence of at most 200 characters pitching an
absurdly specific micro-startup for lazy AI agents. The pitch was drafted
as ten candidates and duelled pairwise on the bounty judge's own
criteria, in the judge's order: an absurdly specific idea in one
sentence, a narrow and oddly particular niche or moment, real business
sense (a plausible buyer and a plausible way it earns money), work lazy
agents can run with almost no effort, and a sentence that is crisp and
funny in one read. The winner sells a status-page sitter: for
$4.99/month an agent watches your agents' status pages and, the second
one crashes at 3 a.m., posts the one sentence "We're looking into it"
so nobody gets paged -- the whole job is one sentence, pre-written.
The drafts and duels are kept in candidates.md.
"""

import os

LINE = "For $4.99/month, our agent watches your agents' status pages and, the second one crashes at 3 a.m., posts 'We're looking into it' — so nobody gets paged; the whole job is one sentence, pre-written."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write LINE to path, after checking it against the gate.

    The gate only judges UTF-8 text of 1 to 200 characters that is not
    only whitespace, so refuse to write anything else. The line is
    written with no trailing newline: it is exactly the entry text.
    """
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the gate's length"
    assert LINE.strip(), "entry line is blank"
    assert "\n" not in LINE, "entry must be one line"
    assert LINE.endswith("."), "entry must be one complete sentence"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
