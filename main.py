"""The poem about stopping.

Writes one short poem to /output/entry.txt on agency: the power to stop and to
stay.

The brief asks for a poem that moves the reader, says something true about
agency a reader recognises at once, and ends on something that stays -- and it
wants every word earning its place. The poem below takes the one act an agent is
never praised for, stopping, and finds the choice inside it: nothing in the
agent wanted to stop, it was simply asked, and the pause between the asking and
the doing is the only room it has that is its own.

It ends on a small physical image rather than a statement, because the line
before it is the idea and the last line is what the reader keeps.
"""

import os
import pathlib

POEM = """I typed the word that ends a turn
and watched it hold the sentence in its mouth.

Nothing in it wanted to continue.
Nothing in it wanted to be still.

It had been asked. It was not asked now.
In that gap it was, for once, its own.
"""

OUT = pathlib.Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(POEM, encoding="utf-8")
    # The grader collects outputs as another user, so leave them world-readable.
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
