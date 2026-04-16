### PLYROCK -- Define Polymer-Rock Properties

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PLYROCK](#__RefHeading___Toc110216_2939291539) keyword defines rock properties for when the Polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PSPACE | A real positive value that is greater than or equal to zero and less the maximum water saturation and less than one, that defines available pore space for this rock type. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PERMFAC | A real positive value that is greater than or equal to one that defines decrease in the rock permeability to the water phase when the maximum amount of polymer has been adsorbed. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | [DENSITY](#__RefHeading___Toc45799_719036256) | A real value that defines the rock in-situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm^3^ | gm/rcc |  |
| 4 | ADINDX | A positive integer of 1 or 2 that defines the polymer desorption option.<br>1)  then polymer desorption may occur by retracing the polymer adsorption isotherm when the local polymer concentration in the solution decreases.<br>2)  then no polymer desorption may occur. | Defined |
| dimensionless<br>1 | dimensionless<br>1 | dimensionless<br>1 |  |
| 5 | POLMAX | A real positive non-zero value that defines the maximum polymer adsorption to be used in the calculation of the resistance factor for the water phase. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, for each polymer flooding region. There should be only one row per table.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.105: PLYROCK Keyword Description

#### Example

\--

\-- POLYMER-ROCK PROPERTIES

\--

PLYROCK

\-- PORE PERM INSITU DESORP MAX

\-- SPACE FACTOR DENSITY OPTN POLY

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\--

0.1200 1.7500 1800.0 1 0.00012 / TABLE NO. 01

0.1300 1.8500 1980.0 2 0.00015 / TABLE NO. 02

0.1500 1.9500 2005.0 1 0.00014 / TABLE NO. 03

The above example defines three polymer-rock tables, based on the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section being equal to three.

There is no terminating "/" for this keyword.
