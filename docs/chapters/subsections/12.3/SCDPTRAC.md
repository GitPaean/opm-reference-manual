### SCDPTRAC -- Allocate Sea Water Tracer for Scale Deposition

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SCDPTRAC](#__RefHeading___Toc644103_516898843) keyword is used to allocate an existing passive water tracer defined by the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, to represent the sea water flowing into a well connection as a fraction of the total water influx. The keyword is used together with the [SCDPTAB](#__RefHeading___Toc644093_516898843) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to calculated the volume of scale deposited around the well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name   | > Description                                                                                                                                                                                                        | > Default |
+-------------------------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric | > Laboratory                                                                                                                                                                                                         |           |
+-------------------------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > NAME   | > A three letter character string defining the tracer's name that has previously been defined by the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section | > None    |
|                                           |          |                                                                                                                                                                                                                      |           |
+-------------------------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |          |                                                                                                                                                                                                                      |           |
|                                           |          |                                                                                                                                                                                                                      |           |
| 1)  The keyword is terminated by a "/".   |          |                                                                                                                                                                                                                      |           |
+-------------------------------------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 12.63: SCDPTRAC Keyword Description

#### Example

In the [PROPS](#__RefHeading___Toc39329_784232322) section define a tracer in the water phase, for example:

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER

\-- NAME PHASE

\-- \-\-\-\-\-- \-\-\-\-\--

TRACER

\'SEA\' \'WAT\' / SEA WATER TRACER

/

Then in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section allocate the previously defined water tracer as a sea water tracer to be used with the scale deposition facility, that is:

\--

\-- ALLOCATE SEA WATER TRACER FOR SCALE DEPOSITION

\--

\-- TRACER

\-- NAME

\-- \-\-\-\-\--

SCDPTRAC

\'SEA\' / SEA WATER TRACER

/
