---
title: 'INCLUDE – Load Another Data File at the Current Position'
source: parts/chapters/subsections/4.3/INCLUDE.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc55749-2479612490"></a>INCLUDE – Load Another Data File at the Current Position

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc32167-370116838817"></a>Description

The [INCLUDE](#-refheading-toc55749-2479612490) keyword informs OPM Flow to continue reading input data from the specified [INCLUDE](#-refheading-toc55749-2479612490) file. When the end of the [INCLUDE](#-refheading-toc55749-2479612490) file is reached, or the [ENDINC](#-refheading-toc51671-2479612490) keyword is encountered in the included file, input data is read from the next keyword in the current file. Although [INCLUDE](#-refheading-toc55749-2479612490) files can be nested, that is [INCLUDE](#-refheading-toc55749-2479612490) files within [INCLUDE](#-refheading-toc55749-2479612490) files etc., in practice this should be avoided due to the complexity of tracking the files.
| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FILENAME | A character string enclosed in quotes that defines a file to read in and be processed by OPM Flow. | None |
| Notes: - The keyword is terminated by a “/”. |  |  |  |

Table 4.4: INCLUDE Keyword Description

#### <a id="-refheading-toc32169-370116838817"></a>Examples

The first example shown below loads the grid file from the same directory as the data file.
```eclipse
--
--       LOAD INCLUDE FILE
--
INCLUDE
         'NOR-OPM-A00-GRID.inc'  /
```

The next example loads the same file one directory above from where the data file is located.
```eclipse
--
--       LOAD INCLUDE FILE
--
INCLUDE
         '../NOR-OPM-A00-FAULTS.inc'  /
```

The final example loads the same file from a separate include directory found in the parent directory relative to where the data file is located.
```eclipse
--
--       LOAD INCLUDE FILE
--
INCLUDE
         '../INCLUDE/NOR-OPM-A00-FAULTS.inc'  /
```
