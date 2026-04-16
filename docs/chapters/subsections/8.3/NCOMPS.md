### NCOMPS -- Confirm Number of Compositional Components

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword confirms the maximum number of compositional components in the model, as such it should have the same number of components as that declared via the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword and either the [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) or the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, have also be activated for the gas-water two component model.

+-------------------------------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name                                                        | > Description                                                                                                                                                                                                                                                                                  | > Default |
+-------------------------------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > [NCOMPS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1) | > A positive integer defining the maximum number of compositional components in the model. Secondly the number of components must be the same as that enter via the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | > 2       |
|                                           |                                                               |                                                                                                                                                                                                                                                                                                |           |
|                                           |                                                               | > Only the default value of two is currently supported by OPM Flow.                                                                                                                                                                                                                            |           |
+-------------------------------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                                               |                                                                                                                                                                                                                                                                                                |           |
|                                           |                                                               |                                                                                                                                                                                                                                                                                                |           |
| 1)  The keyword is terminated by a "/".   |                                                               |                                                                                                                                                                                                                                                                                                |           |
+-------------------------------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 8.90: NCOMPS Keyword Description

#### Example

The following example defines how to confirm a two component formulation to be used with the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) options.

\--

\-- CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)

\--

NCOMPS

2 /
