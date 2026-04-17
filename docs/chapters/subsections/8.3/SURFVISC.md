### SURFVISC -- Surfactant Solution Viscosity versus Concentration

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SURFSVISC defines the surfactant viscosity relationship of solution water viscosity with respect to increasing surfactant concentration within a grid block. The surfactant option must be activated by the SURFACT keyword in the RUNSPEC section in order to use this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SURFCON | A columnar vector of real monotonically increasing down the column values that defines the surfactant concentration in the solution surrounding the rock.<br>The first entry should be zero to define a no surfactant concentration. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2 | SURFVISC | A columnar vector of real positive values that defines the solution water viscosity of the solution for the given SURFCON entry at the reference pressure value, PRES, entered on the PVTW keyword in the PROPS section. | None |
| cP | cP | cP |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.183: SURFVISC Keyword Description

#### Example

\--

\-- SURFACTANT SOLUTION WATER VISCOSITY TABLES

\--

SURFVISC

\-- SURF VISCOSITY

\-- SURFCON SURFVISC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\--

0.0000 0.3500

0.0100 0.3900

0.0200 0.4200

0.0300 0.4300 / TABLE NO. 01

\-- SURF VISCOSITY

\-- SURFCON VISFAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-\--

0.0000 1.000

0.0003 10.000

0.0005 20.000

0.0007 40.000

0.0009 45.000

0.0011 55.000 / TABLE NO. 02

The example defines two surfactant viscosity scaling factor tables, based on the NTPVT variable on the TABDIMS keyword in the RUNSPEC section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.
