# Fibonacci TDD Kata

A small Python project developed with Test-Driven Development to explore
different Fibonacci implementations, packaging, automated testing,
command-line usage, PyPI publishing, and an interactive Marimo demo.

## Installation

pip install fibonacci-tdd-kata-matthieuringd

## Usage

from fibonacci_kata import fibonacci, fibonacci_mod

print(fibonacci(10))
print(fibonacci_mod(100, 1000))

## CLI

fibonacci-kata 10
fibonacci-kata 100 --mod 1000

## Development

uv sync
uv run pytest
uv run ruff check .
uv run mypy src