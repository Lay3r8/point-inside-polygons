# How to determine if a point is inside of a polygon or not?

## Installation
```bash
git clone git@github.com:Lay3r8/point-inside-polygons.git
cd point-inside-polygons
# Preferably, use a venv here. I use pyenv for more convenience.
# pyenv virtualenv 3.8.12 point-inside-polygons
# pyenv activate point-inside-polygons
pip install -r requirements.txt
```

## Scripts
Each pair of scripts demonstrate respectively an example using unittest to prove the algorithm is working (for polygons we don't use any algorithm as all the job is handled by the shapely library) and another example showing a graphical test done with matplotlib.

### triangle.py and triangle_graphical_test.py
These two examples are based on [this response](https://stackoverflow.com/a/51479401/5944716) on stackoverflow and shows an algorith that only works with triangles.

### polygon.py and polygon_graphical_test.py
These two scripts shows how to use the shapely library to determine if a point is inside a polygon.
