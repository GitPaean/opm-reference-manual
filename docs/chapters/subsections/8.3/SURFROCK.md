### SURFROCK -- Define Surfactant-Rock Properties

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SURFROCK keyword defines rock properties for when the Surfactant option has been activated by the SURFACTANT keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ADINDX | A positive integer of 1 or 2 that defines the surfactant desorption option.<br>1)  then surfactant desorption may occur by retracing the surfactant adsorption isotherm when the local surfactant concentration in the solution decreases.<br>2)  then no surfactant desorption may occur. | Defined |
| dimensionless<br>1 | dimensionless<br>1 | dimensionless<br>1 |  |
| 2 | DENSITY | A real value that defines the rock in-situ density, that is at reservoir conditions. | None |
| lb/rtb | kg/rm^3^ | gm/rcc |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section, for each surfactant flooding region. There should be only one row per table.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.182: SURFROCK Keyword Description

#### Example

\--

\-- SURFACTANT-ROCK PROPERTIES

\--

SURFROCK

\-- DESORP INSITU

\-- OPTN DENSITY

\-- \-\-\-\-\-- \-\-\-\-\-\--

1 1800.0 / TABLE NO. 01

2 1980.0 / TABLE NO. 02

1 2005.0 / TABLE NO. 03

The above example defines three surfactant-rock tables, based on the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section being equal to three.

There is no terminating "/" for this keyword.
