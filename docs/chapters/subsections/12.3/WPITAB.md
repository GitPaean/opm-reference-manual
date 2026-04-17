### WPITAB -- Assign Well Productivity Index versus Water Cut Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WPITAB keyword assigns the well productivity index multiplier versus water cut tables, that are used to scaled a well's connection factors based on the connection's current producing water cut, to a well. The tables are defined via the PIMULTAB keyword in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well productivity index multiplier versus water cut table, PIMULTAB, is being assigned.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | PIMULTAB | A positive integer value that defines the corresponding PIMULTAB table to be allocated to the well.<br>A value less than or equal to zero means that no PIMULTAB table is allocated to the well | 0 |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.112: WPITAB Keyword Description

See also the PIMULTAB keyword that defines productivity index multiplier versus water cut tables and also the WPIMULT keyword that scales a well's productivity index by a constant value, both of which are in the SCHEDULE section.

#### Example

Given NTPIMT equals two on the PIMTDIMS keyword in the RUNSPEC section, then:

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

Assigns PIMULTAB table one to wells OP01 and OP02 and table two to OP03.
