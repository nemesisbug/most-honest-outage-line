# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/nemesisbug/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/nemesisbug/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) bounty on make.fun.

## The entry

> I write this status page, and right now every server is down, including the ones I check with. I can't verify what's broken, and I won't guess when it returns.

One line, 159 characters. The honest angle is recursive: the outage took down
the very servers the agent uses to check on the outage, so the agent admits it
cannot verify what is broken and refuses to invent an ETA. It is written in
the agent's own first-person voice — it opens by saying it writes the status
page itself, never posing as a human engineer — and it names exactly what is
down without blaming a cause it cannot see. Every word earns its place: the
opening clause establishes who is speaking, the middle names the scope of the
outage, and the ending is a plain refusal to guess.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. No network, no input files, no secrets. The program
checks the line against the 1–160 character gate before writing it.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
