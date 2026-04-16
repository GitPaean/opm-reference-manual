### SALTPVD -- Initial Precipitated Salt Volume Fraction versus Depth Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SALTPVD](#__RefHeading___Toc613572_1667959253) keyword defines the initial precipitated salt volume fraction versus depth tables for each equilibration region for when OPM Flow's Salt Precipitation Model has been activated in the input deck via the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword defines the initial deposited salt as a volume fraction (Ss), that is solid salt saturation.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                  | > Name                                         | > Description                                                                                                                                        | > Default |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                                | > Metric                                       | > Laboratory                                                                                                                                         |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                    | > [DEPTH](#__RefHeading___Toc58139_3701168388) | > A columnar vector of real monotonically increasing down the column values that defines the depth for corresponding salt volume fraction SALTPSAT.  | > None    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > feet                                                                                                                                                                                 | > m                                            | > cm                                                                                                                                                 |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                                                                    | > SALTPSAT                                     | > A columnar vector of real values that defines the corresponding volume fraction of precipitated salt for the given depth.                          | > None    |
|                                                                                                                                                                                        |                                                |                                                                                                                                                      |           |
|                                                                                                                                                                                        |                                                | > Note only the standard Brine Model is supported and therefore there should be only one columnar vector of SALTPSAT.                                |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                                                                        | > dimensionless                                | > dimensionless                                                                                                                                      |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                               |                                                |                                                                                                                                                      |           |
|                                                                                                                                                                                        |                                                |                                                                                                                                                      |           |
| 1)  The keyword is followed by NTEQUL tables as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |                                                |                                                                                                                                                      |           |
|                                                                                                                                                                                        |                                                |                                                                                                                                                      |           |
| 2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQlDIMS keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.       |                                                |                                                                                                                                                      |           |
|                                                                                                                                                                                        |                                                |                                                                                                                                                      |           |
| 3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                                  |                                                |                                                                                                                                                      |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 10.38: SALTPVD Keyword Description

Precipitated salt can be viewed in OPM ResInsight via the [SALTP](#__RefHeading___Toc486358_4287353749) dynamic grid variable that represents the precipitated salt saturation.

#### Example

The example activates the standard Brine Tracking model using the [BRINE](#__RefHeading___Toc162083_289573908) keyword, OPM Flow's Salt Precipitation model using the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword, and OPM Flow's vaporized water phase with the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword; all three keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The example also sets the number of equilibrium regions to three (NTEQUL set to three on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979)), that is:

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- MAX MAX RSVD TVDP TVDP

\-- EQLNUM DEPTH NODES TABLE NODES

EQLDIMS

3 1\* 20 1\* 1\* /

\--

\-- ACTIVATE STANDARD BRINE MODEL

\--

BRINE

\--

\-- ACTIVATE THE OPM FLOW SALT PRECIPITATION MODEL (OPM FLOW KEYWORD)

\--

PRECSALT

\--

\-- VAPORIZED WATER IN WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

VAPWAT

Then in the [SOLUTION](#__RefHeading___Toc43947_784232322) section the [SALTPVD](#__RefHeading___Toc613572_1667959253) keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- PRECIPITATED SALT VOLUME FRACTION VERSUS DEPTH (OPM FLOW KEYWORD)

\--

\-- DEPTH SALTPSAT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

SALTPVD

3000.0 0.000

8000.0 0.000 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.000

8000.0 0.000 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.000

8000.0 0.000 / EQUIL REGN 03

Here the initial precipitated salt volume fraction has been set to zero for all three equilibration regions.
