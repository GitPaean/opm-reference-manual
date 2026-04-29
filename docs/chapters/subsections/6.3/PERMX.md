---
title: 'PERMX – Define the Permeability in the X Direction for All the Cells'
source: parts/chapters/subsections/6.3/PERMX.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc45791-719036256"></a>PERMX – Define the Permeability in the X Direction for All the Cells

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc715821-3964674244"></a>Description

[PERMX](#-refheading-toc45791-719036256) defines the permeability in the X direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.
| No. | Name | Description |  |  | Default |
| --- | --- | --- | --- | --- | --- |
| Field | Metric | Laboratory |  |  |  |
| 1 | [PERMX](#-refheading-toc45791-719036256) | [PERMX](#-refheading-toc45791-719036256) is an array of real positive numbers assigning the permeability in the X direction to each cell in the model. Repeat counts may be used, for example 20\*100.0. |  |  | None |
| mD | mD | mD |  |  |  |
| Notes: - The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section, unless the [BOX](#-refheading-toc42110-3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#-refheading-toc42110-3671211675) statement. - The keyword is terminated by a “/”. |  |  |  |  |  |

Table 6.105: PERMX Keyword Description

See also the [PERMY](#-refheading-toc45793-719036256) and [PERMZ](#-refheading-toc45795-719036256) keywords to fully define the permeability for the model.

#### <a id="-refheading-toc715823-3964674244"></a>Example

```eclipse
--
--       DEFINE GRID BLOCK PERMX DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PERMX
         100*500.0   100*50.0   100*200.0                                       /
```

The above example defines the [PERMX](#-refheading-toc45791-719036256) to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section.
