# Collaboration repository

This is a demo repository to allow participants on the [SCIC RAP Accelerator](https://the-strategy-unit.github.io/RAP-accelerator/) to practice working together using Git and GitHub, as part of the Collaboration module.

## What does the code do?

The code in this repository reads the .txt files in the `data/` folder that start with the filename `file_`. It then parses the text files to check if a valid name and message are provided, and then randomly selects one name and message to display in the terminal.

## How to run

We recommend using `uv` as a package manager. If using `uv`, run the code with:

```bash
uv run python main.py
```