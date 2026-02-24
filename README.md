# SpotifyData

Analysis of Spotify chart data across European countries, combining chart rankings with audio features to explore music trends.

## Data Sources

| Folder | Dataset |
|--------|---------|
| `data/kaggle1/` | [Spotify Charts](https://www.kaggle.com/datasets/dhruvildave/spotify-charts/data) — daily/weekly top-200 and viral-50 charts by country |
| `data/kaggle2/` | [Spotify Dataset 1921-2020 (600k+ Tracks)](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/data) — track audio features and artist metadata |
| `data/european_countries.csv` | List of European countries used to filter the charts |

**Note:** To run this notebook you must first download `charts.csv` from the [Spotify Charts](https://www.kaggle.com/datasets/dhruvildave/spotify-charts/data) dataset on Kaggle and place it in `data/kaggle1/`. The file is ~3.2 GB, which exceeds GitHub's file-size limit, so it is not included in this repository.

**Note:** To run this notebook you must first download `tracks.csv` and `artists.csv` from the [Spotify Dataset 1921-2020 (600k+ Tracks)](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/data) dataset on Kaggle and place it in `data/kaggle2/`. The files exceed GitHub's file-size limit, so it is not included in this repository.

## 🚀 Setup & Installation

1. Clone the repository.
2. Create a virtual environment (recommended).
3. Install the required Python packages using the [`requirements.txt`](requirements.txt) file:

```sh
pip install -r requirements.txt