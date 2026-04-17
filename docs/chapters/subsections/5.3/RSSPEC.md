### RSSPEC -- Activate Output of the RESTART Index File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RSSPEC keyword activates the writing out of the RESTART index file (\*.RSSPEC). The restart data (pressure, saturations etc. through time for each active cell) are written out to two files one file contains the data, \*.UNRST for example, and the second file contains an index of the data (\*.RSSPEC) stored in the \*.UNRST file. This keyword is somewhat redundant as the RESTART index file is written out by default. See the NORSSPEC keyword in the RUNSPEC section that deactivates the writing out of the file.

Hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE OUTPUT OF THE RESTART INDEX FILE \*.RSSPEC

\--

RSSPEC

The above example switches on the writing of the restart index file (\*.RSSPEC); however, this has no effect in OPM Flow input decks.
