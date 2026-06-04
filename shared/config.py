"""
config.py — Project-wide constants for the Spotify Analysis Project.

Import in any notebook with:
    import sys; sys.path.append('..')
    from shared.config import PATHS, PALETTE, ERAS, FEATURES
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# -- PATHS ------------------------------------------------------------------

# Base directory: two levels up from shared/ (i.e. project root)
ROOT = Path(__file__).resolve().parents[1]

PATHS = {
    'raw'       : ROOT / 'data' / 'kaggle2' / 'tracks.csv',
    'clean'     : ROOT / 'data' / 'processed' / 'tracks_clean.parquet',
    'artists'   : ROOT / 'data' / 'kaggle2' / 'artists.csv',
    'processed' : ROOT / 'data' / 'processed',
}

# -- PALETTE ----------------------------------------------------------------

PALETTE = {
    'green'     : '#1ED760',   # primary accent (Spotify green)
    'purple'    : '#400073',   # secondary accent
    'dark'      : '#3A3A3A',   # near-black (lines, text)
    'cream'     : '#F7F9FA',   # background
    'stone'     : '#b0aea5',   # muted / neutral
    'graphite'  : '#6E6E6E',   # secondary neutral
    'silver'    : '#A0A0A0',   # tertiary neutral
}

# -- ERA DEFINITIONS --------------------------------------------------------
# Each tuple: (start_year, end_year, hex_color, label)
# Applied via axvspan(alpha=0.08) — colors blend across the gradient
# from deep purple (oldest) to Spotify green (most recent)

ERAS = [
    (1920, 1953, '#400073', 'Early Recording Era'),
    (1953, 1990, '#32566B', 'Rock Era'),
    (1990, 2000, '#298F66', 'CD / Digital Era'),
    (2000, 2020, '#1ED760', 'Streaming Era'),
]

# -- CUSTOM COLORMAPS -------------------------------------------------------
# Registered globally with matplotlib on import — use by name in any plot:
#   sns.heatmap(..., cmap='KGr')   or   plt.imshow(..., cmap='Pu_Gr')
#
#   'KGr'   : black → Spotify green        (sequential, 1-tail)
#   'Pu_Gr' : purple → white → green       (diverging, 2-tail)
#   'PuGr'  : purple → teal → green        (sequential gradient, 2-tone)

_CMAP_DEFS = {
    'KGr'   : ['#121212', '#1ED760'],
    'Pu_Gr' : ['#400073', '#FFFFFF', '#1ED760'],
    'PuGr'  : ['#400073', '#2F6C6A', '#1ED760'],
}

for _name, _colors in _CMAP_DEFS.items():
    _cmap = mcolors.LinearSegmentedColormap.from_list(_name, _colors)
    plt.colormaps.register(cmap=_cmap, force=True)

# -- AUDIO FEATURE GROUPS ---------------------------------------------------

FEATURES = {
    # All Spotify audio features used in analysis
    'all': [
        'acousticness', 'danceability', 'energy',
        'instrumentalness', 'liveness', 'speechiness',
        'valence', 'loudness', 'tempo', 'duration_min',
    ],
    # 0–1 bounded, no outlier cleaning needed
    'bounded': [
        'acousticness', 'danceability', 'energy',
        'instrumentalness', 'liveness', 'speechiness', 'valence',
    ],
    # Symmetric distribution → standard IQR cleaning
    'iqr': ['tempo'],
    # Right-skewed / unbounded → log + IQR cleaning
    'log_iqr': ['loudness', 'duration_min'],
    # Final feature set used for clustering (liveness excluded after ablation)
    'clustering': [
        'energy', 'acousticness', 'danceability', 'loudness',
        'speechiness', 'instrumentalness', 'valence', 'tempo_bpm',
    ],
}

# -- PITCH CLASS MAP --------------------------------------------------------
# Spotify `key` column: integer → note name (Pitch Class notation)

KEY_MAP = {
    0: 'C',  1: 'C♯', 2: 'D',  3: 'D♯',
    4: 'E',  5: 'F',  6: 'F♯', 7: 'G',
    8: 'G♯', 9: 'A', 10: 'A♯', 11: 'B',
}

# -- PLOT DEFAULTS ----------------------------------------------------------

def set_style():
    """Apply global matplotlib/seaborn style. Call once per notebook."""
    sns.set_style('ticks')
    plt.rcParams.update({
        'figure.figsize'        : (12, 5),
        'axes.facecolor'        : PALETTE['cream'],
        'font.family'           : 'sans-serif',
        'font.size'             : 11,
        'axes.titleweight'      : 'bold',
        'axes.labelweight'      : 'bold',
        'axes.edgecolor'        : PALETTE['dark'],
        'axes.spines.top'       : False,
        'axes.spines.right'     : False,
    })