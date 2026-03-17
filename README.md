# Computer Vision

This repository holds the code behind my computer vision work and blog posts at [aryanjain.work/blog](https://www.aryanjain.work/blog).

Right now it is centered around notebooks, experiments, and handwritten implementations as I learn and build more projects over time.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Manim Notes

- Manim setup is not required to use the rest of this repo.
- LaTeX is required for `MathTex`.
- If you want to run the Manim side locally, use AI to help with dependency setup if anything gets finicky.

### Run a scene

```bash
manim -pql manim/canny-edge-detection/canny_edge_detection.py SceneName
```

### Mac setup

```bash
brew install --cask basictex
```

## Structure

- `notebooks/` contains notebook experiments and implementations.
- `manim/` contains project-specific animation or standalone Python files.
- `data/` contains project-specific folders that usually match notebook names.
- `outputs/` contains project-specific output folders that usually match notebook names.

In most cases, each notebook or manim project will have a matching folder in `data/` and `outputs/` with the same name. Some projects may use subfolders like `raw/` and `processed/`, but that will depend on the project.
