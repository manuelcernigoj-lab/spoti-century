# SpotifyData

Analysis of Spotify chart data across European countries, combining chart rankings with audio features to explore music trends.

## Data Sources

| Folder | Dataset |
|--------|---------|
| `data/kaggle1/` | [Spotify Charts](https://www.kaggle.com/datasets/dhruvildave/spotify-charts/data) — daily/weekly top-200 and viral-50 charts by country |
| `data/kaggle2/` | [Spotify Dataset 1921-2020 (600k+ Tracks)](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/data) — track audio features and artist metadata |
| `data/european_countries.csv` | List of European countries used to filter the charts |

## Dataset Size Reduction

The original `charts.csv` from kaggle1 (~3.2 GB, ~26 million rows) covers daily and weekly charts for every available country. Since our analysis focuses on Europe, we filtered the dataset to keep only rows whose `region` matches a European country (listed in `data/european_countries.csv`). This reduced the file to a manageable size that can be stored on GitHub and loaded comfortably in memory.

## Notebooks

### 00_filter_eu_charts

Filters the full Kaggle charts dataset down to European countries only.

> **Note:** To run this notebook you must first download `charts.csv` from the [Spotify Charts](https://www.kaggle.com/datasets/dhruvildave/spotify-charts/data) dataset on Kaggle and place it in `data/kaggle1/`. The file is ~3.2 GB, which exceeds GitHub's file-size limit, so it is not included in this repository.

> **Note:** To run this notebook you must first download `tracks.csv` and `artists.csv` from the [Spotify Dataset 1921-2020 (600k+ Tracks)](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks/data) dataset on Kaggle and place it in `data/kaggle2/`. The files exceed GitHub's file-size limit, so it is not included in this repository.