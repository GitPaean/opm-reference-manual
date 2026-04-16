### SALTVD -- Equilibration Salt Concentration versus Depth Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SALTVD](#__RefHeading___Toc605882_516898843) keyword defines the initial salt concentration versus depth tables for each equilibration region for when the salt (brine) phase has been activated in the model via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and the EQLOPT1 variable has been set to a positive integer on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. Secondly, the keyword should also be used to set the initial salt concentration versus depth if OPM Flow's [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to activate the simulators Salt Precipitation model.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                   | > Name                                         | > Description                                                                                                                                                                                                                                                                                   | > Default |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                                 | > Metric                                       | > Laboratory                                                                                                                                                                                                                                                                                    |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                     | > [DEPTH](#__RefHeading___Toc58139_3701168388) | > A columnar vector of real monotonically increasing down the column values that defines the depth for corresponding salt concentrations SALTCON.                                                                                                                                               | > None    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > feet                                                                                                                                                                                  | > m                                            | > cm                                                                                                                                                                                                                                                                                            |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                                                                     | > SALTCON                                      | > A columnar vector of real monotonically increasing down the column values that defines the corresponding salt concentration within the water phase for the given depth. There should be one columnar vector for each type of salt.                                                            | > None    |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                | > For the standard Brine Model there is only one salt type and therefore there should be only one columnar vector of SALTCON.                                                                                                                                                                   |           |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                | > However, if the [BRINE](#__RefHeading___Toc162083_289573908) keyword has been invoked with the [ECLMC](#__RefHeading___Toc206960_803326780) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then there should one columnar SALTCON vector for each declared salt type. |           |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                | > It is recommended to provide initial salt concentrations less then or equal to values provided by [SALTSOL](#__RefHeading___Toc681417_1466963378) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.                                                                         |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > lb/stb                                                                                                                                                                                | > kg/sm^3^                                     | > gm/scc                                                                                                                                                                                                                                                                                        |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
| 1)  The keyword is followed by NTEQUIL tables as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
| 2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQlDIMS keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.        |                                                |                                                                                                                                                                                                                                                                                                 |           |
|                                                                                                                                                                                         |                                                |                                                                                                                                                                                                                                                                                                 |           |
| 3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                                   |                                                |                                                                                                                                                                                                                                                                                                 |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 10.40: SALTVD Keyword Description

#### Examples

The first example activates the standard Brine Tracking model using the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and sets the number of equilibrium regions to three (NTEQUIL set to 3 on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979)), that is:

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

Then in the [SOLUTION](#__RefHeading___Toc43947_784232322) section the [SALTVD](#__RefHeading___Toc605882_516898843) keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DEPTH SALT-1 SALT-2 SALT-3 SALT-4

\-- SALTCON SALTCON SALTCON SALTCON

\-- \-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- SALTVD

3000.0 1.200

8000.0 1.200 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.300

8000.0 1.300 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.400

8000.0 1.400 / EQUIL REGN 03

The next example shows how the [SALTVD](#__RefHeading___Toc605882_516898843) keyword is entered when both the [ECLMC](#__RefHeading___Toc206960_803326780) and [BRINE](#__RefHeading___Toc162083_289573908) keywords have activated the Multi-Component Brine model in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that is:

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

\--

\-- ACTIVATE MULTI-COMPONENT BRINE MODEL

\--

ECLMC

\--

\-- DEFINE WATER PHASE MULTI-COMPONENT BRINE COMPONENTS

\--

\-- SALT1 SALT2 SALT3 SALT4 SALT5

BRINE

NACL CACL MGC03 /

The above example activates the Multi-Component Brine model with three different water salinities for three equilibrium regions. In this case the resulting [SALTVD](#__RefHeading___Toc605882_516898843) keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DEPTH SALT-01 SALT-02 SALT-03 SALT-04

\-- CONCENTR CONCENTR CONCENTR CONCENTR

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- SALTVD

3000.0 1.200 0.540 0.020

7000.0 1.200 0.640 0.040 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.300 0.440 0.020

8000.0 1.300 0.540 0.040 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

5000.0 1.400 0.640 0.002

8000.0 1.400 0.640 0.002 / EQUIL REGN 03

In this case there are three data sets, on one for each equilibrium region and three SALTCON columnar vectors, one for each salt type (NACL, CACL and MGC03) declared via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Note that the Multi-Component Brine model is not available in OPM Flow.
