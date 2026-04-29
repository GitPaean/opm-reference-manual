---
title: 'END – Define the End of the Input File'
source: parts/chapters/subsections/4.3/END.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc46631-2479612490"></a>END – Define the End of the Input File

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc14499-3701168388310"></a>Description

This keyword marks the end of the input file and can occur in any section. Any keywords and data after the [END](#-refheading-toc46631-2479612490) keyword are ignored.
There is no data required for this keyword.

#### <a id="-refheading-toc14501-3701168388310"></a>Example

```eclipse
-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2006-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
'WELLS=2'    'WELSPECS'    'CPU=2'     'FIP=2'                                 /

DATES
 1  JAN   2006  /
/

RPTSCHED
'NOTHING'                                                                      /

DATES
 1  APR   2006  /
 1  JLY   2006  /
 1  OCT   2006  /
/
       ECHO
--
-- ******************************************************************************
-- END OF FILE
-- ******************************************************************************
END
-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2007-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
'WELLS=2'    'WELSPECS'    'CPU=2'     'FIP=2'                                 /

DATES
 1  JAN   2007  /
/
```

In the above example OPM Flow will process the data up to October 1, 2006 only, and then start to run the simulation. All keywords after the [END](#-refheading-toc46631-2479612490) file keyword will not be read or processed.
