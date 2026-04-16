### COMPS -- Activate Compositional Modeling Formulation

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword activates the Compositional Modeling Formulation, and declares the number of components active in the model.

OPM Flow does not currently support the general compositional modeling formulation.

+-------------------------------------------+---------+-------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name  | > Description                                                                             | > Default |
+-------------------------------------------+---------+-------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > COMPS | > A positive integer defining the number of compositional components active in the model. | > 2       |
|                                           |         |                                                                                           |           |
|                                           |         | > Only the default value of two is currently supported by OPM Flow.                       |           |
+-------------------------------------------+---------+-------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |         |                                                                                           |           |
|                                           |         |                                                                                           |           |
| 1)  The keyword is terminated by a "/".   |         |                                                                                           |           |
+-------------------------------------------+---------+-------------------------------------------------------------------------------------------+-----------+

Table 5.7: COMPS Keyword Description

#### Example

The following example shows how to request a two component compositional modeling formulation to be used with the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) options.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)

\--

CO2STORE

\--

\-- ACTIVATE COMPOSITIONAL MODELING FORMULATION (OPM FLOW KEYWORD)

\--

COMPS

2 /

\--

\-- ACTIVATE GAS-WATER THE MODEL (OPM FLOW KEYWORD)

\--

GASWAT
