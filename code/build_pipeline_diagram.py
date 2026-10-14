# -*- coding: utf-8 -*-
"""Fig. 1: Disclosure-audit pipeline (DAP) schematic.

Vector figure built with a wrap-safe cursor layout (no manual line breaks, so
no overlap risk from re-wrapped text) and every string kept in-script so it is
easy to audit for typos. Reflects the 5-dimension transparency index as of the
2026-09-02 methodology revision: Facility-level and Region-resolved are merged
into "Spatially attributable electricity", and "Renewable-electricity
accounting transparency" is the new fifth dimension.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path
import textwrap

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

BLUE = '#1F4E79'
BLUE_LIGHT = '#EAF0F7'
BLUE_BORDER = '#B9CBE0'
GREEN = '#2E7D32'
GREEN_LIGHT = '#EAF4EA'
GREEN_BORDER = '#B7D8B7'
PANEL_BG = '#FFFFFF'
TEXT_DARK = '#242A30'
TEXT_MID = '#4A4F55'
ARROW_COLOR = '#5B84AE'
CALLOUT_BORDER = '#1F4E79'

fig, ax = plt.subplots(figsize=(17.5, 14.0), dpi=300)
ax.set_xlim(0, 105)
ax.set_ylim(0, 64)
ax.axis('off')
fig.patch.set_facecolor('white')

ax.text(52.5, 62.2, "Disclosure-audit pipeline (DAP) for grid-relevant interpretation",
        ha='center', va='center', fontsize=15, fontweight='bold', color='#141A2E')


def panel(x, y, w, h, num, title, header_bg=BLUE_LIGHT, header_border=BLUE_BORDER,
          badge_color=BLUE, body_bg=PANEL_BG, body_border=None):
    body_border = body_border or header_border
    body = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.7",
                           facecolor=body_bg, edgecolor=body_border, linewidth=1.1, zorder=1)
    ax.add_patch(body)
    ax.add_patch(mpatches.Circle((x + 2.0, y + h - 2.4), 1.15, facecolor=badge_color, edgecolor='none', zorder=3))
    ax.text(x + 2.0, y + h - 2.4, str(num), ha='center', va='center', fontsize=8.5,
            fontweight='bold', color='white', zorder=4)
    ax.text(x + 3.7, y + h - 2.4, title, ha='left', va='center', fontsize=9.2,
            fontweight='bold', color=badge_color, zorder=3)
    ax.plot([x + 1.0, x + w - 1.0], [y + h - 4.3, y + h - 4.3], color=header_border, linewidth=0.9, zorder=2)
    return x, y, w, h


def bullets(x, top_y, width, items, fontsize=6.6, wrap_chars=36, line_h=1.62, item_gap=1.0,
            marker='dot', color=TEXT_DARK, marker_color=TEXT_MID):
    """Wrap-safe bullet/numbered list. Returns the y just below the last item."""
    cursor = top_y
    for i, item in enumerate(items):
        lines = textwrap.wrap(item, width=wrap_chars) or [""]
        n = len(lines)
        if marker == 'dot':
            ax.add_patch(mpatches.Circle((x + 0.35, cursor - line_h * 0.5), 0.24,
                                          facecolor=marker_color, edgecolor='none', zorder=4))
            text_x = x + 1.15
        else:
            ax.text(x, cursor - line_h * 0.5, f"{i + 1}.", ha='left', va='center', fontsize=fontsize,
                    color=marker_color, fontweight='bold', zorder=4)
            text_x = x + 1.9
        ax.text(text_x, cursor, "\n".join(lines), ha='left', va='top', fontsize=fontsize,
                color=color, linespacing=1.28, zorder=4)
        cursor -= n * line_h + item_gap
    return cursor


def content_height(items, wrap_chars, line_h, item_gap):
    total = 0.0
    for item in items:
        n = len(textwrap.wrap(item, width=wrap_chars) or [""])
        total += n * line_h + item_gap
    return total - item_gap


def centered_top(body_bottom, body_top, items, wrap_chars, line_h, item_gap):
    h = content_height(items, wrap_chars, line_h, item_gap)
    return body_bottom + (body_top - body_bottom + h) / 2.0


def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=14,
                         color=ARROW_COLOR, linewidth=2.1, zorder=0, shrinkA=0, shrinkB=0)
    ax.add_patch(a)


# ---------------------------------------------------------------------------
# Column geometry
# ---------------------------------------------------------------------------
COL_TOP = 55.0
COL_BOTTOM = 12.0
COL_H = COL_TOP - COL_BOTTOM

x_c1, w_c1 = 4.0, 16.5
x_c2, w_c2 = 23.5, 16.5
x_c3, w_c3 = 43.0, 22.5
x_c4, w_c4 = 68.5, 16.5
x_c5, w_c5 = 88.0, 16.5

# ---------------------------------------------------------------------------
# Step 1: Source identification
# ---------------------------------------------------------------------------
MID_Y = (COL_BOTTOM + COL_TOP) / 2  # 33.5

body_bottom, body_top = COL_BOTTOM + 1.0, COL_TOP - 4.3

panel(x_c1, COL_BOTTOM, w_c1, COL_H, 1, "Source\nidentification")
c1_items = [
    "Public corporate sustainability / environmental reports",
    "Source inventory and report-year tracking",
    "Explicit evidence locations recorded",
]
c1_top = centered_top(body_bottom, body_top, c1_items, 27, 1.7, 2.2)
bullets(x_c1 + 1.0, c1_top, w_c1 - 2.0, c1_items, wrap_chars=27, fontsize=7.0, line_h=1.7, item_gap=2.2)

arrow(x_c1 + w_c1 + 0.3, MID_Y, x_c2 - 0.3, MID_Y)

# ---------------------------------------------------------------------------
# Step 2: Structured coding
# ---------------------------------------------------------------------------
panel(x_c2, COL_BOTTOM, w_c2, COL_H, 2, "Structured\ncoding")
c2_items = [
    "Company × metric assessment",
    "Electricity quantity, location, temporal alignment, and boundary fields",
    "Only explicitly reported values are coded",
    "Renewable-claim disclosures coded for accounting method (market- vs. location-based Scope 2) and procurement-instrument breakdown",
]
c2_top = centered_top(body_bottom, body_top, c2_items, 27, 1.7, 2.2)
bullets(x_c2 + 1.0, c2_top, w_c2 - 2.0, c2_items, wrap_chars=27, fontsize=7.0, line_h=1.7, item_gap=2.2)

# ---------------------------------------------------------------------------
# Step 3a / 3b (green, stacked) -- generous heights: 5 long bullets need real room
# ---------------------------------------------------------------------------
h3a = 28.0
h3b = COL_H - h3a - 1.3
y3b = COL_BOTTOM
y3a = COL_BOTTOM + h3b + 1.3

arrow(x_c2 + w_c2 + 0.3, y3a + h3a / 2, x_c3 - 0.3, y3a + h3a / 2)
arrow(x_c2 + w_c2 + 0.3, y3b + h3b / 2, x_c3 - 0.3, y3b + h3b / 2)

panel(x_c3, y3a, w_c3, h3a, "3a", "Spatial attribution test",
      header_bg=GREEN_LIGHT, header_border=GREEN_BORDER, badge_color=GREEN, body_border=GREEN_BORDER)
bullets(x_c3 + 1.0, y3a + h3a - 5.0, w_c3 - 2.0, [
    "Does the company report electricity for named data-center facilities, campuses, or metro locations?",
    "Does the company report a regional aggregation for a defined data-center portfolio at a qualifying geography?",
    "Qualifying region-resolved geography: state, balancing authority, electrical interconnection, or comparable subnational geography",
    "Facility-level and region-resolved are alternative, not separately scored, routes to Spatially attributable electricity",
    "Facility or metro observations are not aggregated or externally mapped to award region-resolved granularity",
], wrap_chars=42, fontsize=5.9, line_h=1.28, item_gap=0.7)

panel(x_c3, y3b, w_c3, h3b, "3b", "Boundary clarity test",
      header_bg=GREEN_LIGHT, header_border=GREEN_BORDER, badge_color=GREEN, body_border=GREEN_BORDER)
bullets(x_c3 + 1.0, y3b + h3b - 4.6, w_c3 - 2.0, [
    "Inclusion / exclusion of owned, leased, colocation, and third-party infrastructure",
    "Quantified scope where available",
    "Boundary definition assessed separately from electricity quantity",
], wrap_chars=42, fontsize=5.9, line_h=1.28, item_gap=0.7)

arrow(x_c3 + w_c3 + 0.3, MID_Y, x_c4 - 0.3, MID_Y)

# ---------------------------------------------------------------------------
# Callout: does NOT qualify as Spatially attributable (sits below the columns)
# ---------------------------------------------------------------------------
callout_h = 6.8
callout_y = 2.6
callout = FancyBboxPatch((x_c3 - 1.0, callout_y), w_c3 + 2.0, callout_h, boxstyle="round,pad=0,rounding_size=0.6",
                          linestyle=(0, (4, 2)), facecolor='white', edgecolor=CALLOUT_BORDER, linewidth=1.1, zorder=1)
ax.add_patch(callout)
ax.text(x_c3 + (w_c3 + 2.0) / 2 - 1.0, callout_y + callout_h - 1.4, "Does NOT qualify as Spatially attributable",
        ha='center', va='center', fontsize=7.6, fontweight='bold', color=BLUE, zorder=3)
bullets(x_c3, callout_y + callout_h - 2.7, w_c3, [
    "Broad geographies such as “Americas,” “Europe,” or “Asia Pacific”",
    "External mapping of named sites into grid regions",
], wrap_chars=52, fontsize=6.1, line_h=1.3, item_gap=0.5)
ax.plot([x_c3 + w_c3 / 2, x_c3 + w_c3 / 2], [callout_y + callout_h, y3b - 0.2],
        color=CALLOUT_BORDER, linewidth=1.1, linestyle=(0, (3, 2)), zorder=1)

# ---------------------------------------------------------------------------
# Goal banner (full width)
# ---------------------------------------------------------------------------
banner = FancyBboxPatch((4.0, 0.3), 100.0, 1.9, boxstyle="round,pad=0,rounding_size=0.5",
                         facecolor=BLUE_LIGHT, edgecolor=BLUE_BORDER, linewidth=1.0, zorder=1)
ax.add_patch(banner)
ax.text(54.0, 1.25, "Goal: evaluate disclosure verifiability, not environmental performance.",
        ha='center', va='center', fontsize=8.0, fontweight='bold', color=BLUE, zorder=3)

# ---------------------------------------------------------------------------
# Step 4: Five-dimension transparency index
# ---------------------------------------------------------------------------
panel(x_c4, COL_BOTTOM, w_c4, COL_H, 4, "Five-dimension\ntransparency index")
c4_items = [
    "Data-center-only MWh",
    "Spatially attributable electricity",
    "Time-based alignment",
    "Boundary clarity",
    "Renewable-electricity accounting transparency",
]
c4_score_h = 2.4  # reserve room below the list for the divider + scoring line
c4_top = centered_top(body_bottom + c4_score_h, body_top, c4_items, 27, 1.9, 0.9)
b4_bottom = bullets(x_c4 + 1.0, c4_top, w_c4 - 2.0, c4_items,
                     wrap_chars=27, marker='num', fontsize=6.9, line_h=1.9, item_gap=0.9)
ax.plot([x_c4 + 1.0, x_c4 + w_c4 - 1.0], [b4_bottom + 0.3, b4_bottom + 0.3], color=BLUE_BORDER, linewidth=0.8)
ax.text(x_c4 + w_c4 / 2, b4_bottom - 1.3, "Scoring: Yes = 1, Partial = 0.5, No = 0",
        ha='center', va='top', fontsize=6.5, color=TEXT_MID, fontweight='bold', linespacing=1.3)

arrow(x_c4 + w_c4 + 0.3, MID_Y, x_c5 - 0.3, MID_Y)

# ---------------------------------------------------------------------------
# Step 5: Interpretation
# ---------------------------------------------------------------------------
panel(x_c5, COL_BOTTOM, w_c5, COL_H, 5, "Interpretation")
c5_items = [
    "Assess whether disclosures support independent grid-aware interpretation",
    "Distinguish annual matching from hourly alignment",
    "Identify remaining interpretability gaps",
]
c5_top = centered_top(body_bottom, body_top, c5_items, 27, 1.7, 2.2)
bullets(x_c5 + 1.0, c5_top, w_c5 - 2.0, c5_items, wrap_chars=27, fontsize=7.0, line_h=1.7, item_gap=2.2)

plt.tight_layout()
PROJECT_DIR = Path(__file__).resolve().parents[1]
out_dir = PROJECT_DIR / "plots"
out_dir.mkdir(parents=True, exist_ok=True)
pdf_path = out_dir / "DataCenters Diagram.pdf"
png_path = out_dir / "DataCenters Diagram.png"
plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
print("Saved:", pdf_path)
print("Saved:", png_path)
