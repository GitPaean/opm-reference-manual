---
title: 'TOPS – Define the Depth at the Center of the Top Face for Each Cell'
source: parts/chapters/subsections/6.3/TOPS.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc55283-3701168388"></a>TOPS – Define the Depth at the Center of the Top Face for Each Cell

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc14509-3701168388172"></a>Description

[TOPS](#-refheading-toc55283-3701168388) defines the depth of the top face of each cell in the model.
It can only be used with the Cartesian Regular Grid or Radial Grid models.
| No. | Name | Description |  |  | Default |
| --- | --- | --- | --- | --- | --- |
| Field | Metric | Laboratory |  |  |  |
| 1 | [TOPS](#-refheading-toc55283-3701168388) | [TOPS](#-refheading-toc55283-3701168388) is an array of real numbers defining the depth at the top face of each cell in the model. One can either just enter the [TOPS](#-refheading-toc55283-3701168388) for the first layer only based on NX x NY entries and OPM Flow will calculate the remaining [TOPS](#-refheading-toc55283-3701168388) based on either [DZ](#-refheading-toc45769-719036256) or [DZV](#-refheading-toc55601-3701168388). Alternatively NX x NY x NZ [TOPS](#-refheading-toc55283-3701168388) may be entered for each cell in the model. See the [DIMENS](#-refheading-toc20387-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section for the definition of NX, NY and NZ. Repeat counts may be used, for example 10\*5201.0. |  |  | None |
| feet | m | cm |  |  |  |
| Notes: - The keyword is terminated by a “/”. |  |  |  |  |  |

Table 6.129: TOPS Keyword Description

See also the DEPTHS keyword to define the structural depth for the cells.

#### <a id="-refheading-toc715873-3964674244"></a>Examples

The example below defines the [TOPS](#-refheading-toc55283-3701168388) of the cells for each cell for NX = 5, NY = 5 and NZ = 3 model, as well as the X and Y direction cells sizes.
```eclipse
--
--       DEFINE GRID BLOCK TOPS FOR THE TOP LAYER (NX=5, NY=5, and NZ=3)
--
TOPS
         25*3100  25*3105  25*3110                                             /                                                                                 --
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)
--
DXV
         5*100                                                                 /                                                                                 --
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NY = 5)
--
DYV
         5*100                                                                 /
```

A second example is shown on the following page.                                                                                
This example defines the same grid as before but with the [TOPS](#-refheading-toc55283-3701168388) keyword only defining the top layer and [DZV](#-refheading-toc55601-3701168388) keyword defining the cells thickness.
```eclipse
--
--       DEFINE GRID BLOCK TOPS FOR THE TOP LAYER (NX = 5, NY = 5, NZ = 3)
--
TOPS
         25*3100                                                               /
--
--       DEFINE GRID BLOCK Z DIRECTION CELL SIZE (BASED ON NZ = 3)
--
DZV
         3*5.0                                                                 /
--
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)
--
DXV
         5*100                                                                 /                                                                                 --
--       DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NY = 5)
--
DYV
         5*100                                                                 /
```
