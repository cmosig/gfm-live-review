"""gfm-live-review pipeline package.

A self-updating literature review of geospatial foundation models. All inference
runs through the local Claude Code CLI under a subscription login; this package
contains ZERO API credentials and no `anthropic` SDK dependency by design.
"""

__version__ = "0.1.0"

# Bumping EXTRACTOR_VERSION signals that previously extracted cards should be
# re-extracted (backfill). It is stamped onto every Card at ingest time.
EXTRACTOR_VERSION = "1"
