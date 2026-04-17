### FOAMROCK -- Define Foam Rock Properties

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FOAMROCK keyword defines the foam rock properties for when the Foam option has been activated by the FOAM keyword in the RUNSPEC section.

The keyword is recognized by the input deck parser and simulator support is available in the experimental \"ebos\" simulator.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ADINDX | A positive integer of 1 or 2 that defines foam desorption option, as per:<br>1)  then foam desorption may occur by retracing the foam adsorption isotherm when the local foam concentration in the solution decreases.<br>2)  then no foam desorption may occur.<br>Only the default value of 1 is supported by OPM Flow. | Defined |
| dimensionless<br>1 | dimensionless<br>1 | dimensionless<br>1 |  |
| 2 | DENSITY | A real value that defines the rock in situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm^3^ | gm/rcc |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain just one row and one row only.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.38: FOAMROCK Keyword Description

#### Example

\--

\-- FOAM-ROCK PROPERTIES

\--

FOAMROCK

\-- DESORP INSITU

\-- OPTN DENSITY

\-- \-\-\-\-\-- \-\-\-\-\-\--

1 1800.0 / TABLE NO. 01

2 1980.0 / TABLE NO. 02

1 2005.0 / TABLE NO. 03

The above example defines three foam-rock tables, based on the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section being equal to three.

There is no terminating "/" for this keyword.
