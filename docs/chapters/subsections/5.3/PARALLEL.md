### PARALLEL -- Define Parallel Run Configuration

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PARALLEL](#__RefHeading___Toc88962_4106839650) keyword defines the run to use parallel processing and sets the domain decomposition options. See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to run OPM Flow in parallel mode.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NPROCS | A positive integer that defines the number of domains or parallel processors to use for this run. | 1 |
| 2 | RTYPE | A character string set to either SERIAL to run the parallel code in serial mode for testing the code, or DISTRIBUTED to full utilize parallel processing. | DISTRIBUTED |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.33: PARALLEL Keyword Description

OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

#### Example

\--

\-- PARALLEL MULTI-CORE OPTIONS

\-- NDMAIN MACHINE TYPE

PARALLEL

2 DISTRIBUTED /

The above example sets the number of domains (or processors) to two and for the simulation to run in parallel mode. This has no effect in OPM Flow input decks.
