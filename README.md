# Computer Vision

This repository holds the code behind my computer vision work and blog posts at [aryanjain.work/blog](https://www.aryanjain.work/blog).

Right now it is centered around notebooks, experiments, and handwritten implementations as I learn and build more projects over time.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Structure

- `notebooks/` contains notebook experiments and implementations.
- `data/` contains project-specific folders that usually match notebook names.
- `outputs/` contains project-specific output folders that usually match notebook names.

In most cases, each notebook will have a matching folder in `data/` and `outputs/` with the same name. Some projects may use subfolders like `raw/` and `processed/`, but that will depend on the project.
