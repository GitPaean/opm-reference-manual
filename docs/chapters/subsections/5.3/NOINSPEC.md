### NOINSPEC -- Deactivate Output of the INIT Index File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [NOINSPEC](#__RefHeading___Toc70892_4106839650) keyword deactivates the writing out of the INIT index file (\*.INSPEC). The initialization data (or static data) is written out to two files one file contains the data, \*.INIT, and the second file contains an index of the data (\*.INSPEC) stored in the \*.INIT file. This functionality is redundant as most post-processing software require the \*.INSPEC file to load the \*.INIT data set.

Hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE OUTPUT OF THE INIT INDEX FILE \*.INSPEC

\--

NOINSPEC

The above example switches off the writing of the INIT index file (\*.INSPEC); however, this has no effect in OPM Flow input decks.
