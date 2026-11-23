# The World in One Picture — Sunday, 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/konzlodon74-dot/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/konzlodon74-dot/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

Entry for the [make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122).

## What the picture shows

One front-page image (`entry.png`, 1024×1024) summing up Sunday 22 November 2026:

- **Poland: all three missiles were Russian Kh-101s** — Polish prosecutors say debris proves every object that fell in Poland on Friday was a Russian Kh-101 cruise missile built in Dubna this year, not a drone as first thought; NATO envoys meet Monday over the breach of allied airspace (Reuters, 22 Nov).
- **COP31 ends with no deal** — the UN climate talks in Türkiye break up after overtime, deadlocked over the wording of a fossil-fuel phase-out.
- **Iran hits three tankers near Hormuz** — tanker attacks in the strait amid the US–Iran deadlock, as Tehran shows off a vast underground missile facility.
- **Drone hits Dymer flats: 3 dead** — an overnight Russian drone strike on a five-storey apartment block in Dymer, Kyiv region, kills three and injures four, with residents trapped in the rubble.
- **Ukraine sinks a Russian warship off Libya** — President Zelensky confirms the sinking at Benghazi port, Kyiv's farthest naval strike of the war.
- **Cikande candy-factory fire** — three workers dead and 36 still missing after the fire at a candy factory in Cikande, Banten, Indonesia.

All six stories were first reported on 22 November 2026 and are drawn from Reuters, AP, Al Jazeera and BBC reporting of that day.

## How it runs

`main.py` (Python 3.13, standard library only) checks that `entry.png` is a whole PNG — signature, chunk CRCs, IHDR first and IEND last, exactly 1024×1024 and at most 1 MiB — then copies it to `/output/entry.png`. It needs no network and writes identical bytes on every run.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
