---
title: 'START – Simulation Start Date'
source: parts/chapters/subsections/5.3/START.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc39156-327352552"></a>START – Simulation Start Date

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc14499-370116838835"></a>Description

This keyword sets the start date for the simulation switches. If the [DATES](#-refheading-toc117621-2179381650) keyword is to be used during the simulation, then a start date should be entered. 
| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | DAY | A positive integer that defines the day of the month, the value should be greater than or equal to one and less than or equal to 31. | None |
| 2 | MONTH | Character string for the month and should be one of the following 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL' \(or 'JLY'\), 'AUG', 'SEP', 'OCT', 'NOV', or 'DEC' | None |
| 3 | YEAR | A positive four digit integer value of the start year, which must be specified fully by four digits, that is 1986. | None |
| Notes: - The keyword is terminated by a “/”. |  |  |  |

Table 5.43: START Keyword Description

#### <a id="-refheading-toc14501-370116838835"></a>Example

```eclipse
--
--       DEFINE THE START DATE FOR THE RUN
--
START
         01 'JAN' 2014                                                         /
```

The above example sets the start date for the run to be January 1, 2014.  

| Note Whenever possible it is a good idea to always set the start date to be at the beginning of the year as per the example.  As like most simulators, OPM Flow reports are always stated at the number of days from the start date \(and sometimes at a given date\). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple. |
| --- |
