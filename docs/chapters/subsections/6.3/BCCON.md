### BCCON -- Define Boundary Conditions Connections

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [BCCON](#REF_HEADING_KEYWORD_BCCON) keyword defines the grid connections for the boundary conditions.

Together the [BCCON](#REF_HEADING_KEYWORD_BCCON) and [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keywords define the boundary conditions for the model, and can be used to set boundary conditions for when external influx or efflux volumes are influencing the reservoir pressure and production history. For example, when the average reservoir pressure remains constant throughout the production period due to water influx, or gas migration from an external source.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                                                                              | > INDEX  | > A positive integer that identifies the boundary condition.                                                                                                                                                    | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                                                                              | > I1     | > A positive integer that defines the lower bound of the grid in the I-direction for which the boundary conditions are to be applied, must be greater than or equal 1 and less than or equal to I2 and NX.      | > 1    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                                                                              | > I2     | > A positive integer that defines the upper bound of the grid in the I-direction for which the boundary conditions are to be applied, must be greater than or equal to II and less than or equal to NX          | > NX   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                                                                                                                              | > J1     | > A positive integer that defines the lower bound of the grid in the J-direction for which the boundary conditions are to be applied, must be greater than or equal 1 and less than or equal to J2 and NY.      | > 1    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 4                                                                                                                                                                                              | > J2     | > A positive integer that defines the upper bound of the grid in the J-direction for which the boundary conditions are to be applied, must be greater than or equal to JI and less than or equal to NY.         | > NY   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 5                                                                                                                                                                                              | > K1     | > A positive integer that defines the lower bound of the grid in the K-direction for which the boundary conditions are to be applied, must be greater than or equal to one and less than or equal to K2 and NZ. | > 1    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 6                                                                                                                                                                                              | > K2     | > A positive integer that defines the upper bound of the grid in the K-direction for which the boundary conditions are to be applied, must be greater than or equal to KI and less than or equal to NZ.         | > NZ   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 7                                                                                                                                                                                              | > DIRECT | > A character string that defines the direction to apply the boundary conditions, and should be set to one of the following X, Y, or Z for the positive direction, or X-, Y- or Z- for the negative direction.  | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                                                                         |          |                                                                                                                                                                                                                 |        |
|                                                                                                                                                                                                  |          |                                                                                                                                                                                                                 |        |
| 1)  Where NX, NY and NZ are the dimensions of the model as defined on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |          |                                                                                                                                                                                                                 |        |
|                                                                                                                                                                                                  |          |                                                                                                                                                                                                                 |        |
| 2)  Each record must be terminated by a "/" and the keyword is terminated by a "/\".                                                                                                             |          |                                                                                                                                                                                                                 |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 6.3.12.1: BCCON Keyword Description

See also the [AQUFLUX](#__RefHeading___Toc202105_1310555686) keyword that is supported by OPM Flow in both the [SOLUTION](#__RefHeading___Toc43947_784232322) and [SCHEDULE](#__RefHeading___Toc43945_784232322) sections, to define a constant flux analytical aquifer.

If the [BCCON](#REF_HEADING_KEYWORD_BCCON) and [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keywords are not present in the input deck, then the boundary conditions for the model are set to be no flow, which is the normal behavior in both OPM Flow and the commercial simulator.

The [BC](#__RefHeading___Toc42110_36712116751) keyword has been replaced by the [BCCON](#REF_HEADING_KEYWORD_BCCON) and [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keywords.

#### Examples

The first example shows how to set a constant pressure boundary using TYPE equal to FREE:

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1\* 1 1\* X- /

2 1 1\* 1 1 1 1\* Y /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE PHASE RATE PRESS TEMP

BCPROP

1 FREE 1\* 1\* 1\* 1\* /

2 FREE /

/

With this option it is only necessary to define the boundary cells and all the other parameters (COMPONENT, RATE, PRESS, and TEMP) can be defaulted, as they are ignored when TYPE equals FREE.

The next example is based on NX, NY and NZ equal to 20, 1, 10 respectively, on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and shows how different boundary types can be assigned to different parts of the model.

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1 1 10 X- /

2 20 20 1 1 1 10 X /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE PHASE RATE PRESS TEMP

BCPROP

1 DIRICHLET GAS 1\* 256.0 100.0 /

2 FREE 4\* /

/

The last example shows how the DIRICHLET boundary condition option may be used:

\--

\-- DEFINE BOUNDARY CONDITIONS CONNECTION (OPM FLOW GRID KEYWORD)

\--

\--INDEX \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- BC

\-- I1 I2 J1 J2 K1 K2 DIRC

BCCON

1 1 1 1 1\* 1 1\* X- /

2 1 1\* 1 1 1 1\* Y /

/

\--

\-- DEFINE BOUNDARY CONDITIONS PROPERTIES (OPM FLOW SCHEDULE KEYWORD)

\--

\--INDEX BC BC BC BC BC

\-- TYPE PHASE RATE PRESS TEMP

BCPROP

1 DIRICHLET WAT 1\* 256.0 100.0 /

2 DIRICHLET WAT 1\* 1\* 100.0 /

/

Here, the first line sets both the pressure and temperature at the boundary, and the second line defaults the pressure entry, so that the simulator calculated initial boundary pressure will be used.
