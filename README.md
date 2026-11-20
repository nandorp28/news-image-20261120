# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nandorp28/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nandorp28/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — Friday 20 November 2026

A newspaper-style front page summing up the world news of Friday
20 November 2026. The image (`entry.png`, 1024x1024, under 1 MiB) is
drawn by `assets/generate.py` (PIL + Liberation fonts, run at build
time); `main.py` (Python 3.13, standard library only) copies it to
`/output/entry.png` and verifies the copy byte-for-byte. No network,
no randomness — two runs write byte-identical output.

## The stories

- **Lead, Games — GTA VI smashes every record.** Sensor Tower
  estimates 19.05 million copies worth $1.84 billion in the first
  24 hours, the biggest entertainment launch ever; a peak of 7.9
  million people watched streams at once, and internet traffic hit a
  record 33 terabits a second. Take-Two's first official figures are
  expected today.
- **Diplomacy — Three leaders, one table.** Trump, Xi and Putin hold
  the first-ever three-way summit in Shenzhen, talking nuclear arms
  control and global security.
- **Middle East — Missile hits Riyadh tower.** A Houthi strike damages
  the PIF Tower, the Saudi wealth fund's HQ and the city's tallest
  building — the second hit on the financial district in two weeks.
  No injuries.
- **Weather — Cyclone Akvan bears down.** 80,000 people evacuated in
  Odisha as the storm nears India's east coast; Andhra Pradesh on
  high alert as heavy rain begins.
- **Justice — Court: Myanmar "likely" genocide.** The World Court
  rules Myanmar's military likely intended to destroy a substantial
  part of the Rohingya in the 2017 crackdown.
- **Also today:** Kerch Bridge rail link halted; Anthropic valued at
  $1.5tn; Nicholls century in the Wellington Test; Voyager 1 reaches
  one light-day; Fiji declares a drought disaster; Seoul court clears
  ex-PM Han Duck-soo; US and Venezuela restore military ties.

Every story is an event that happened, or was first reported, on
19–20 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qyk2abaw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
