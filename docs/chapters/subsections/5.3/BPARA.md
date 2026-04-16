### BPARA -- Activate Block Parallel License

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [BPARA](#__RefHeading___Toc171154_1314821763) keyword activates the block parallel license in the commercial simulator. There is no data required for this keyword; however the keyword should be followed by the [PARALLEL](#__RefHeading___Toc88962_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, as illustrated in the example below.

There is no data required for this keyword and there is no terminating "/" for this keyword.

OPM Flow is an open source project and therefore there is no license management of the various implemented options or the number of cores/threads that can be utilized; hence this keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See section [[2.2](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline)[](#2.2.Running OPM Flow 2018-10 |outline)[[Running OPM Flow 2023-04 From The Command Line](#anchor-2)](#2.2.Running OPM Flow 2018-10 |outline) on how to run OPM Flow in parallel mode.

#### Example

\--

\-- ACTIVATE BLOCK PARALLEL LICENSE

\--

BPARA

\--

\-- PARALLEL MULTI-CORE OPTIONS

\-- NDMAIN MACHINE TYPE

PARALLEL

8 DISTRIBUTED /

The above example sets the number of domains (or processors) to eight and for the simulation to run in block parallel mode. This has no effect in OPM Flow input decks.
