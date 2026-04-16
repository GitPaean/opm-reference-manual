### WPITAB -- Assign Well Productivity Index versus Water Cut Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPITAB](#__RefHeading___Toc121649_2412586160) keyword assigns the well productivity index multiplier versus water cut tables, that are used to scaled a well's connection factors based on the connection's current producing water cut, to a well. The tables are defined via the [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well productivity index multiplier versus water cut table, [PIMULTAB](#__RefHeading___Toc121637_2412586160), is being assigned.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | [PIMULTAB](#__RefHeading___Toc121637_2412586160) | A positive integer value that defines the corresponding [PIMULTAB](#__RefHeading___Toc121637_2412586160) table to be allocated to the well.<br>A value less than or equal to zero means that no [PIMULTAB](#__RefHeading___Toc121637_2412586160) table is allocated to the well | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.112: WPITAB Keyword Description

See also the [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword that defines productivity index multiplier versus water cut tables and also the [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword that scales a well's productivity index by a constant value, both of which are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

Given NTPIMT equals two on the [PIMTDIMS](#__RefHeading___Toc31215_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then:

\--

\-- ASSIGN WELL PRODUCTIVITY INDEX VS WATER CUT TABLE

\--

\-- WELL PI

\-- NAME TABLE

WPITAB

OP01 1 /

OP02 1 /

OP03 2 /

/

Assigns [PIMULTAB](#__RefHeading___Toc121637_2412586160) table one to wells OP01 and OP02 and table two to OP03.
