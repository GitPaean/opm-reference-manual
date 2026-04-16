### PERMFACT -- Permeability Multiplication Factor as a Function of Porosity Change

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[PERMFACT](#__RefHeading___Toc712146_1466963378) defines the permeability multiplication factor due to a change in porosity. The keyword is used in conjunction with OPM Flow's Salt Precipitation model, in which the pore space is reduced due to salt precipitating in the pore space, causing a reduction in porosity and an associated reduction in permeability. This keyword is also used for the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and [MICP](#__RefHeading___Toc383375_111689907) model, where the pore space is reduced due to biofilm formation, and for the [MICP](#__RefHeading___Toc383375_111689907) model, also due to calcite precipitation.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                                                     | > Name          | > Description                                                                                                                                                                                                                                           | > Default |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                                                                   | > Metric        | > Laboratory                                                                                                                                                                                                                                            |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                                                       | > POROFAC       | > A real monotonically increasing positive columnar vector that defines the porosity () factor for the corresponding PERMFAC vector.                                                                                                                    | > None    |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
|                                                                                                                                                                                                                           |                 | > In the simulator's Salt Precipitation model, the maximum value of is , implying a maximum value of one for POROFAC.                                                                                                                                   |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                                                                                                           | > dimensionless | > dimensionless                                                                                                                                                                                                                                         |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                                                                                                       | > PERMFAC       | > A real positive monotonically increasing columnar vector that defines the permeability (k) multiplier associated with POROFAC and used to scale a grid block\'s permeability due to the reduction in pore volume caused by salt precipitation. Where: | > None    |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > dimensionless                                                                                                                                                                                                           | > dimensionless | > dimensionless                                                                                                                                                                                                                                         |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                                                                  |                 |                                                                                                                                                                                                                                                         |           |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
| 1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.                                      |                 |                                                                                                                                                                                                                                                         |           |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
| 2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.    |                 |                                                                                                                                                                                                                                                         |           |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
| 3)  There must be same number of entries for each column.                                                                                                                                                                 |                 |                                                                                                                                                                                                                                                         |           |
|                                                                                                                                                                                                                           |                 |                                                                                                                                                                                                                                                         |           |
| 4)  Each table is terminated by a single "/" and there is no "/" terminator for the keyword.                                                                                                                              |                 |                                                                                                                                                                                                                                                         |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 8.97: PERMFACT Keyword Description

The porosity reduction can be written as a function proportional to the initial porosity, e.g., considering the volume fraction of salt () precipitated out of the vaporized water phase, that is:

The porosity and associated permeability factor data can be calculated using a permeability-porosity relationship, for example:

Where:

k~o~ and = the initial permeability and porosity,

k and = the actual permeability and porosity that changes due to the model dynamics (e.g., precipitation or dissolution of salt, biofilm formation, calcite precipitation),

= the residual porosity at which permeability is zero, and

= a positive exponent.

See also Kozeny-Carment (extended)[^1], [^2] and [^3] and Verma-Pruess[^4] for additional functional forms that can be used to derive the tabulated data that can be entered via the [PERMFACT](#__RefHeading___Toc712146_1466963378) keyword.

#### Example

The example below defines two [PERMFACT](#__RefHeading___Toc712146_1466963378) tables assuming NTSFUN equals two and NSSFUN is greater than or equal to five on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- PERMEABILITY FACTOR AS A FUNCTION OF POROSITY REDUCTION

\-- (OPM FLOW KEYWORD)

\--

PERMFACT

\-- PORO PERM

\-- FACTOR FACTOR

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 0.0000

0.25 0.0625

0.50 0.2500

0.75 0.5625

1.00 1.0000 / TABLE NO. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 0.0000

0.25 0.0625

0.50 0.2500

0.75 0.5625

1.00 1.0000 / TABLE NO. 02

Both tables use equation with Φc equal to zero and ɣ equal to 2.0. Note that [PERMFACT](#__RefHeading___Toc712146_1466963378) changes the permeability in all three dimensions, that is the [PERMX](#__RefHeading___Toc45791_719036256), [PERMY](#__RefHeading___Toc45793_719036256) and [PERMZ](#__RefHeading___Toc45795_719036256) arrays are all modified.

[^1]: J. Kozeny, \"Ueber kapillare Leitung des Wassers im Boden.\" Sitzungsber Akad. Wiss., Wien, 136(2a): 271-306, 1927.

[^2]: P.C. Carman, \"Fluid flow through granular beds.\" Transactions, Institution of Chemical Engineers, London, 15: 150-166, 1937.

[^3]: P.C. Carman, \"Flow of gases through porous media.\" Butterworths, London, 1956.

[^4]: Verma, A., & Pruess, K. (1988). Thermohydrological conditions and silica redistribution near high-level nuclear wastes emplaced in saturated geological formations. Journal of Geophysical Research,93, 1159--1173.
