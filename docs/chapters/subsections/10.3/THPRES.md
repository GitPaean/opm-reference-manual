### THPRES -- Define Equilibration Region Threshold Pressures

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [THPRES](#__RefHeading___Toc210168_2884651453) defines the threshold pressure between various equilibration regions that have been defined by the [EQLNUM](#__RefHeading___Toc73734_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section. The threshold pressure defines the potential difference between two regions which must be exceeded before flow can occur between the two regions. Once flow occurs the potential between the two regions is reduced by the threshold pressure.

This option must be activated by [THPRES](#__RefHeading___Toc210168_2884651453) variable on [EQLOPTS](#__RefHeading___Toc131554_398689501) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to utilize this feature. Note that the irreversible option, as defined by IRREVER variable on [EQLOPTS](#__RefHeading___Toc131554_398689501) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, is not supported.

+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                               | > Name                                           | > Description                                                                                                                                                                                                                                                                                                                                       | > Default |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                             | > Metric                                         | > Laboratory                                                                                                                                                                                                                                                                                                                                        |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                 | > EQLNUM1                                        | > EQLNUM1 is an a positive integer that is greater or equal to one and less than or equal to NTEQUL on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the "from" equilibration region number.                                                                | > None    |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                     | > dimensionless                                  | > dimensionless                                                                                                                                                                                                                                                                                                                                     |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                 | > EQLNUM2                                        | > EQLNUM1 is an a positive integer that is greater or equal to one and less than or equal to NTEQUL on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the "to" equilibration region number.                                                                  | > None    |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                     | > dimensionless                                  | > dimensionless                                                                                                                                                                                                                                                                                                                                     |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 3                                                                                                                                 | > [THPRES](#__RefHeading___Toc210168_2884651453) | > [THPRES](#__RefHeading___Toc210168_2884651453) defines the threshold pressure from EQLNUM1 to EQLNUM2 and from EQLNUM2 to EQLNUM1.                                                                                                                                                                                                                | > 1\*     |
|                                                                                                                                     |                                                  |                                                                                                                                                                                                                                                                                                                                                     |           |
|                                                                                                                                     |                                                  | > The default value of 1\* sets the threshold pressure to a value that initially prevents flow between the two equilibration regions. Any subsequent production or injection in either of the two equilibration regions will therefore result in flow between the two regions. Thus, this default initially isolates the two equilibration regions. |           |
|                                                                                                                                     |                                                  |                                                                                                                                                                                                                                                                                                                                                     |           |
|                                                                                                                                     |                                                  | > If a equilibration region number pair has not been explicitly defined by this keyword the [THPRES](#__RefHeading___Toc210168_2884651453) is set to zero, for no threshold pressure.                                                                                                                                                               |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > psia                                                                                                                              | > barsa                                          | > atma                                                                                                                                                                                                                                                                                                                                              |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                            |                                                  |                                                                                                                                                                                                                                                                                                                                                     |           |
|                                                                                                                                     |                                                  |                                                                                                                                                                                                                                                                                                                                                     |           |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword is terminated by a "/".   |                                                  |                                                                                                                                                                                                                                                                                                                                                     |           |
+-------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 10.60: THPRES Keyword Description

See also the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that uses the transmissibility between the [MULTNUM](#__RefHeading___Toc61329_2752266063), [FLUXNUM](#__RefHeading___Toc45781_719036256) or [OPERNUM](#__RefHeading___Toc67857_718313858) region arrays to control the flow between various regions within the model.

#### Examples

Given NTEQUL is equal to six on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section,

\--

\-- EQLNUM EQLNUM THPRES

\-- FROM TO VALUE

THPRES

1 2 0.588031 / REGN 1 TO REGN 2

2 1 0.588031 / REGN 2 TO REGN 1

1 3 0.787619 / REGN 1 TO REGN 3

3 1 0.787619 / REGN 3 TO REGN 1

1 4 7.000830 / REGN 1 TO REGN 4

4 1 7.000830 / REGN 4 TO REGN 1

/

The above example defines the threshold pressures between equilibration regions one and two, one and three and one and four. As the threshold pressures between regions one and five and one and six (as well as other combinations), have not been explicitly set in the example, the threshold pressures for these combinations are set to zero.

However, as the irreversible option, as defined by IRREVER variable on [EQLOPTS](#__RefHeading___Toc131554_398689501) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, is not supported, then example can be simplified to:

\--

\-- EQLNUM EQLNUM THPRES

\-- FROM TO VALUE

THPRES

1 2 0.588031 / REGN 1 AND REGN 2

1 3 0.787619 / REGN 1 AND REGN 3

1 4 7.000830 / REGN 1 AND REGN 4

/

Again, as the threshold pressures between regions one and five and one and six (as well as other combinations), have not been explicitly set in the example, the threshold pressures for these combinations are set to zero.
