# Mox Buy Me A Coffee

This is part of the Cyfrin Updraft Vyper Course. 

- [Mox Buy Me A Coffee](#mox-buy-me-a-coffee)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
- [Usage](#usage)
  - [Compile](#compile)
  - [Test](#test)
- [Formatting](#formatting)
  - [Python](#python)
  - [Vyper](#vyper)

# Getting Started

## Prerequisites

- [git](https://git-scm.com/)
  - You'll know you've done it right if you can run `git --version` and see a version number.
- [anvil](https://book.getfoundry.sh/anvil/)
  - You'll know you've done it right if you can run `anvil --version` and see an output like `anvil 0.2.0 (fdd321b 2024-10-15T00:21:13.119600000Z)`
- [moccasin](https://github.com/Cyfrin/moccasin)
  - You'll know you've done it right if you can run `mox --version` and get an output like: `Moccasin CLI v0.3.0`

## Installation

```bash
git clone https://github.com/cyfrin/mox-buy-me-a-coffee-cu
cd mox-buy-me-a-coffee-cu
```

## Quickstart

```bash
mox run deploy 
```

# Usage

## Compile

```bash
mox compile
```

## Test

```bash
mox test
```

# Formatting

## Python

```
uv run ruff check --select I --fix
uv run ruff check . --fix
```

## Vyper 

```
uv run mamushi src
```