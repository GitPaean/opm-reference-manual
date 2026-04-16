### FOAMMOB -- Define Foam Gas Mobility versus Foam Concentration Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [FOAMMOB](#__RefHeading___Toc224978_3519154785) keyword defines the reduction in gas mobility as a function of the foam concentration within a grid block. The Foam option must be activated by the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. In addition, this keyword must be supplied if the foam model is activated.

| 1 | FOAMCON | A columnar vector of real monotonically increasing down the column values that defines the foam concentration for the corresponding gas mobility reduction factor (FOAMRATI).<br>The first entry should be zero to define a no foam concentration data set.<br>Units are dependent on the transport phase specified via the FOAMOPT1 variable on the [FOAMOPTS](#__RefHeading___Toc224982_3519154785) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. FOAMOPT1 should be set to either [GAS](#__RefHeading___Toc38607_2267116897) or [WATER](#__RefHeading___Toc38611_2267116897). | None |
| --- | --- | --- | --- |
| Gas: lb/Mscf<br>Water: lb/stb | Gas: kg/sm^3^<br>Water: kg/sm^3^ | Gas: gm/scc<br>Water: gm/scc |  |
| 2 | FOAMRATI | A columnar vector of real decreasing down the column values that defines the corresponding gas mobility reduction factor for a given FOAMCON.<br>The first table data set entry should be one to define a no foam concentration data set.<br>Each FOAMCON/FOAMRATI data set should be terminated by a "/" | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.36: FOAMMOB Keyword Description

See also the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the [FOAMADS](#__RefHeading___Toc224974_3519154785), [FOAMOPTS](#__RefHeading___Toc224982_3519154785) and [FOAMROCK](#__RefHeading___Toc224980_3519154785) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

\--

\-- FOAM GAS MOBILITY VERSUS FOAM CONCENTRATION TABLES

\--

FOAMMOB

\-- FOAM FOAM

\-- FOAMCON FOAMRATI

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 1.00000

0.005 0.50000

0.010 0.20000

0.015 0.10000

0.020 0.07500

0.025 0.07000

0.030 0.06500

0.035 0.06500 / TABLE NO. 01

\-- FOAM FOAM

\-- FOAMCON FOAMRATI

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 1.00000

0.010 0.50000

0.015 0.25000

0.020 0.07500

0.025 0.07000

0.030 0.07000 / TABLE NO. 02

Given NTPVT equals two and NPPVT is greater and or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the example defines the foam gas mobility versus foam concentration tables for two tables.

There is no terminating "/" for this keyword.
