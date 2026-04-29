---
title: 'PORO – Define the Porosity Values for All the Cells'
source: parts/chapters/subsections/6.3/PORO.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc45797-719036256"></a>PORO – Define the Porosity Values for All the Cells

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc715835-3964674244"></a>Description

[PORO](#-refheading-toc45797-719036256) defines the porosity for all the cells in the model via an array. The keyword can be used with all grid types.
| No. | Name | Description |  |  | Default |
| --- | --- | --- | --- | --- | --- |
| Field | Metric | Laboratory |  |  |  |
| 1 | [PORO](#-refheading-toc45797-719036256) | [PORO](#-refheading-toc45797-719036256) is an array of real positive numbers that are greater than or equal to zero and less than or equal to one that are the porosity values for each cell in the model. Repeat counts may be used, for example 3000\*0.15 |  |  | None |
| dimensionless | dimensionless | dimensionless |  |  |  |
| Notes: - The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section, unless the [BOX](#-refheading-toc42110-3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#-refheading-toc42110-3671211675) statement. - The keyword is terminated by a “/”. |  |  |  |  |  |

Table 6.112: PORO Keyword Description

See also the [NTG](#-refheading-toc33334-784232322), [PERMX](#-refheading-toc45791-719036256), [PERMY](#-refheading-toc45793-719036256) and [PERMX](#-refheading-toc45791-719036256) keywords to fully define a grid’s properties

#### <a id="-refheading-toc715837-3964674244"></a>Example

```eclipse
--
--    DEFINE GRID BLOCK POROSITY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PORO
      300*0.300                                                                 /
```

The above example defines a constant porosity of 0.300 to all 300 cells in the model as defined by the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section.
