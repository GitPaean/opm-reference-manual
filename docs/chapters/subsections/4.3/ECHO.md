---
title: 'ECHO – Activate Echoing of User Input Files to the Print File'
source: parts/chapters/subsections/4.3/ECHO.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc52483-2479612490"></a>ECHO – Activate Echoing of User Input Files to the Print File

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc10367-370116838817"></a>Description

Turns on echoing of all the input files to the print file; note that this keyword is activated by default and can subsequently be switched off by the [NOECHO](#-refheading-toc52487-2479612490) activation keyword.
There is no data required for this keyword.
This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### <a id="-refheading-toc14501-370116838837"></a>Example

```eclipse
--
--        SWITCH OFF ECHOING OF INPUT FILES
--
NOECHO
--
--        INCLUDE SIMULATION GRID WITH SLOPING FAULTS
--
INCLUDE
          './INCLUDE/GRID/IRAP_1005.GRDECL' /
--
--        SWITCH ON ECHOING OF INPUT FILES
--
ECHO
```

The examples deactivates the echoing of the input files, reads in the grid geometry data using the [INCLUDE](#-refheading-toc55749-2479612490)  keyword, and then activates the echoing of the input files again.

| Note Especially for the large voluminous data sets in the [GRID](#-refheading-toc38674-784232322) section, it is good practice to deactivate the echoing of the input files when loading this data to avoid the print output file becoming too large to view in a text editor. |
| --- |
