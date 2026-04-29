---
title: 'ACTNUM – Set the Status of a Grid Block To Active or Inactive'
source: parts/chapters/subsections/6.3/ACTNUM.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc4410-421927891"></a>ACTNUM – Set the Status of a Grid Block To Active or Inactive

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc5743-3701168388"></a>Description

The [ACTNUM](#-refheading-toc4410-421927891) keyword specifies which grid blocks are either active or inactive. A grid block is automatically set to inactive if its pore volume is less than the value entered using the [MINPV](#-refheading-toc569208-3181922006) keyword. The [ACTNUM](#-refheading-toc4410-421927891) keyword can be used to also make blocks with pore volumes greater than [MINPV](#-refheading-toc569208-3181922006) inactive. 
| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ACTNUM | An array of integers equal to either 0 or 1 that define the activity of each cell in the model. A value of 0 indicates the cell is inactive. Grid blocks are ordered with the I index cycling fastest, followed by the J and K indices. Repeat counts may be used, for example 20\*1. | 1 |
| Notes: - The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section, unless the [BOX](#-refheading-toc42110-3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#-refheading-toc42110-3671211675) keyword. - The keyword is terminated by a “/”. |  |  |  |

Table 6.2: ACTNUM Keyword Description

#### <a id="-refheading-toc5745-3701168388"></a>Examples

The example below sets several cells to be inactive for a 4 x 5 x 2 model. 
```eclipse
ACTNUM
-- Layer 1
0 0 1 1
0 0 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-- Layer 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
/
```

Alternatively the [EQUALS](#-refheading-toc296597-1576177388) keyword could be employed to accomplish the same task, that is:
```eclipse
--       -- ARRAY    CONSTANT --  ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         'ACTNUM’    1.0000       1*  1*   1*  1*   1*  1* / SET ACTIVE CELLS
         'ACTNUM’    0.0000       1   2    1   2    1   1  / SET INACTIVE CELLS
         'ACTNUM’    0.0000       1   4    5   5    2   2  / SET INACTIVE CELLS
/
```
