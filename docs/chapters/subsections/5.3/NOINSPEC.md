### NOINSPEC -- Deactivate Output of the INIT Index File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NOINSPEC keyword deactivates the writing out of the INIT index file (\*.INSPEC). The initialization data (or static data) is written out to two files one file contains the data, \*.INIT, and the second file contains an index of the data (\*.INSPEC) stored in the \*.INIT file. This functionality is redundant as most post-processing software require the \*.INSPEC file to load the \*.INIT data set.

Hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE OUTPUT OF THE INIT INDEX FILE \*.INSPEC

\--

NOINSPEC

The above example switches off the writing of the INIT index file (\*.INSPEC); however, this has no effect in OPM Flow input decks.
