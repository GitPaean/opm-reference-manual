---
title: 'DX – Define the Size of Grid Blocks in the X Direction for All Cells'
source: parts/chapters/subsections/6.3/DX.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc92905-705534506"></a>DX – Define the Size of Grid Blocks in the X Direction for All Cells

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc715679-3964674244"></a>Description

[DX](#-refheading-toc92905-705534506) defines the size of all grid blocks in the X direction via an array for each cell in a Cartesian Regular Grid model.
| No. | Name | Description |  |  | Default |
| --- | --- | --- | --- | --- | --- |
| Field | Metric | Laboratory |  |  |  |
| 1 | [DX](#-refheading-toc92905-705534506) | [DX](#-refheading-toc92905-705534506) is an array of real numbers describing the cell size in the X direction for each cell in the model. Repeat counts may be used, for example 10\*100.0. |  |  | None |
| feet | m | cm |  |  |  |
| Notes: - The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section, unless the [BOX](#-refheading-toc42110-3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#-refheading-toc42110-3671211675) statement. - The keyword is terminated by a “/”. |  |  |  |  |  |

Table 6.26: DX Keyword Description

See also the [DY](#-refheading-toc45767-719036256), [DZ](#-refheading-toc45769-719036256) and [TOPS](#-refheading-toc55283-3701168388) keywords to fully define a Cartesian Regular Grid.

#### <a id="-refheading-toc715681-3964674244"></a>Example

```eclipse
--
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX x NY x NZ = 300)
--
DX
         300*1000                                                              /
```

The above example defines the size of the cells in the X direction based on 300 cells in the model as defined by the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section.
