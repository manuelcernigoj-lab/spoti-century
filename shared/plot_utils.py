"""
plot_utils.py — Reusable plot helpers for the Spotify Analysis Project.

Import in any notebook with:
    import sys; sys.path.append('..')
    from shared.plot_utils import shade_eras, era_legend, make_fig

All functions follow project conventions:
    - fig, ax = plt.subplots() pattern
    - ax=ax passed explicitly to seaborn calls
    - era shading via ax.axvspan() at alpha=0.08
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from shared.config import ERAS, PALETTE


# -- ERA SHADING ------------------------------------------------------------

def shade_eras(ax, alpha=0.08, eras=ERAS):
    """
    Shade musical eras as background bands on a temporal axis.

    Parameters
    ----------
    ax    : matplotlib Axes — the target plot
    alpha : float          — transparency of the shading (default 0.08)
    eras  : list of tuples — override default ERAS if needed

    Example
    -------
    fig, ax = plt.subplots()
    sns.lineplot(data=yearly_means, x='year', y='valence', ax=ax)
    shade_eras(ax)
    """
    for start, end, color, _ in eras:
        ax.axvspan(start, end, alpha=alpha, color=color)


def era_legend(ax=None, fig=None, loc='upper center',
               bbox_to_anchor=(0.5, 1.05), ncols=4, fontsize=10,
               eras=ERAS):
    """
    Add a shared era legend using mpatches.Patch handles.

    Use `fig.legend()` (via fig=fig) for multi-axes figures,
    or `ax.legend()` (via ax=ax) for single-axis plots.

    Parameters
    ----------
    ax/fig          : pass one of these — ax for single plot, fig for subplots
    loc             : legend anchor location string
    bbox_to_anchor  : (x, y) offset tuple
    ncols           : columns in the legend (default 4, one per era)
    fontsize        : legend font size
    eras            : list of tuples — override default ERAS if needed

    Example (single axis)
    ---------------------
    era_legend(ax=ax, bbox_to_anchor=(0.5, 0.98))

    Example (shared across subplots)
    ---------------------------------
    era_legend(fig=fig, bbox_to_anchor=(0.5, 1.05))
    """
    patches = [
        mpatches.Patch(color=color, alpha=0.4, label=label)
        for _, _, color, label in eras
    ]
    if fig is not None:
        fig.legend(handles=patches, loc=loc,
                   bbox_to_anchor=bbox_to_anchor,
                   ncols=ncols, fontsize=fontsize)
    elif ax is not None:
        ax.legend(handles=patches, loc=loc,
                  bbox_to_anchor=bbox_to_anchor,
                  ncols=ncols, fontsize=fontsize)
    else:
        raise ValueError("Pass either ax= or fig= to era_legend().")


# -- FIGURE HELPERS ---------------------------------------------------------

def make_fig(nrows=1, ncols=1, figsize=None, **kwargs):
    """
    Thin wrapper around plt.subplots() with project background applied.

    Returns fig, ax (or array of axes for multi-panel figures).

    Example
    -------
    fig, ax = make_fig(figsize=(14, 5))
    fig, axes = make_fig(nrows=2, ncols=3, figsize=(16, 8))
    """
    if figsize is None:
        figsize = (12, 5) if (nrows == 1 and ncols == 1) else (14, 5 * nrows)

    fig, ax = plt.subplots(nrows=nrows, ncols=ncols,
                           figsize=figsize,
                           facecolor=PALETTE['cream'],
                           **kwargs)

    # Apply background to all axes
    axes_flat = [ax] if (nrows == 1 and ncols == 1) else \
                list(ax.flatten()) if hasattr(ax, 'flatten') else [ax]

    for a in axes_flat:
        a.set_facecolor(PALETTE['cream'])

    return fig, ax


# -- TEMPORAL LINE PLOT -----------------------------------------------------

def temporal_lineplot(data, x, y, ax, title='', xlabel='Year', ylabel='',
                      color=None, shade=True, xlim=(1920, 2020)):
    """
    Standard temporal line plot with optional era shading.

    Parameters
    ----------
    data   : DataFrame or Series
    x, y   : column names (or None if data is a Series indexed by year)
    ax     : matplotlib Axes
    title  : plot title string
    shade  : bool — whether to shade eras (default True)
    xlim   : tuple — x-axis range

    Example
    -------
    fig, ax = make_fig(figsize=(18, 5))
    temporal_lineplot(yearly_means, x='year', y='valence', ax=ax,
                      title='Valence over time')
    plt.show()
    """
    c = color or PALETTE['dark']

    if shade:
        shade_eras(ax)

    sns.lineplot(data=data, x=x, y=y, ax=ax, color=c, linewidth=1.5)

    ax.set_title(title, fontsize=13)
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.set_xlim(xlim)
    ax.set_xticks(range(xlim[0], xlim[1] + 1, 10))


# -- GET ERA LABEL ----------------------------------------------------------

def get_era(year, eras=ERAS):
    """
    Return the era label for a given year.

    Example
    -------
    get_era(1975)   # → 'Rock Era'
    get_era(2010)   # → 'Streaming Era'
    """
    for start, end, _, label in eras:
        if start <= year < end:
            return label
    return 'Unknown'
