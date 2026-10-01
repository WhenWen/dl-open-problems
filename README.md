# Deep Learning Open Problems

An open, evidence-tracked collection of questions connecting deep learning experiments and theory.

We document what is understood, the assumptions behind that understanding, and precise tests of what remains uncertain. A candidate is **not** a verified claim that nobody has solved the problem. The canonical catalog contains three candidate cards. The first [discovery batch](discovery/2026-10-01/README.md) adds 26 leads from 57 primary papers: 23 new candidates and three existing-card updates. These are abstract-screened proposals, not a comprehensive survey or a novelty certification.

[Browse problems](INDEX.md) · [Discovery queue](discovery/README.md) · [Contribute](CONTRIBUTING.md) · [Coverage](coverage/README.md) · [中文](README.zh-CN.md)

## Start contributing

- **Propose a problem:** open a candidate issue with the setting, observable, prior work, and a decisive test.
- **Add an answer or correction:** identify a theorem, experiment, counterexample, or missing paper and explain its scope.
- **Improve coverage:** record a search, including searches that found no eligible problem.
- **Reproduce a result:** contribute a protocol and public artifact links, including negative results and uncertainty.
- **Review a duplicate:** compare assumptions, available inputs, target quantities, and interventions.

Use [Issues](https://github.com/WhenWen/dl-open-problems/issues/new/choose) without writing code, or submit a pull request using the [problem template](templates/README.md). Small corrections are welcome. English is the canonical card language; issues may be written in English or Chinese.

## What each card contains

A precise question, established results, remaining uncertainty, competing explanations, a minimal test, success criteria, and a dated literature audit. Structured metadata supports multiple topic views without copying a problem into several lists.

Review status and scientific maturity are separate. Theory, empirical support, and predictive validation are described independently. Problems can become resolved, be merged, or be retired without losing their history.

## Repository layout

```text
problems/DLOP-0001/  # metadata.json and readable README.md
discovery/          # batch searches and leads awaiting deeper review
bibliography.json   # canonical source records and reading depth
coverage/           # search history and explicit unscreened topics
reviews/            # decisions, exclusions and merge records
templates/          # copyable problem card
scripts/catalog.py  # validation and generated index
```

## Local checks

Python 3.10 or newer; no additional packages required.

```sh
python3 scripts/discovery.py
python3 scripts/catalog.py
python3 scripts/discovery.py --check
python3 scripts/catalog.py --check
python3 -m unittest discover -s tests -v
```

The first two commands rebuild the discovery reports and catalog index. CI checks metadata, IDs, references, relations, coverage records, local Markdown links, and index freshness. It cannot certify novelty, correctness, or semantic nonduplication; those require [human review](docs/REVIEW.md).

## Scope and license

The scope spans optimization, scaling, data, representations and generalization, in-context learning, generative modeling, post-training, and numerical precision. Coverage is intentionally explicit about what has **not** been searched.

Original repository text and code use the [MIT license](LICENSE). Linked papers, datasets and external artifacts retain their own licenses. Contributions remain attributed through Git history and the contributor fields on cards. See [governance](GOVERNANCE.md) for review decisions and disagreements.
