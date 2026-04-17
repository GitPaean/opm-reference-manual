### BDENSITY -- Define the Surface Brine Density for the Fluid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

BDENSITY defines the brine surface density for when the brine phase has been activated in the model by the BRINE keyword in the RUNSPEC section. The number of BDENSITY vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section. Each record consists of a maximum of NPPVT values, as declared on the TABDIMS keyword in the RUNSPEC section, with each value representing a brine surface density.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

The keyword is used in conjunction with the PVTWSALT keyword in the PROPS section, with each brine density value matching with the salt concentration values in column 1 of each table in the PVTWSALT keyword. Note that the BDENSITY keyword is optional, and if absent from the input file, then the brine surface densities will be set to the water density values declared via the DENSITY keyword in the PROPS section. In this case there is no variation in brine surface density with respect to salt concentration.

| No. | Name | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
| 1 | WATDEN | Field | Metric | Laboratory | None |
| WATDEN is a real monotonically increasing positive row vector that defines the brine density at surface conditions for the given salt concentrations on the corresponding PVTWSALT keyword in the PROPS section.<br>There should be one row element for each salt concentration columnar element (SALTCON) on the PVTWSALT keyword. |  |  |  |  |  |
| lb/ft^3^ | kg/m | gm/cc |  |  |  |
| Notes:<br>1)  Each row vector data set must be terminated by a "/" including the last data set. |  |  |  |  |  |

Table 8.24: BDENSITY Keyword Description

#### Example

The following shows the BDENSITY and PVTWSALT keywords for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set equal to two and NPPVT is set to greater than four on the TABDIMS keyword.

\--

\-- BRINE WATER DENSITY DATA FOR PVTWSALT KEYWORD

\--

\-- SALTCON SALTCON SALTCON SALTCON SALTCON \-- DENSITY DENSITY DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

BDENSITY

62.20 63.50 64.75 65.90 / FOR PVTWSALT TABLE 1

64.00 65.50 67.00 / FOR PVTWSALT TABLE 2 \--

\-- WATER SALT PVT TABLE

\--

PVTWSALT

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4500.0 0.000 / TABLE NO. REF. DATA

\--

\-- SALTCONC BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.020 2.7E-6 0.370 0.0

2.0 1.010 2.7E-6 0.370 0.0

4.0 1.000 2.7E-6 0.370 0.0

10.0 0.950 2.7E-6 0.370 0.0 / TABLE NO. 01 SALT DATA

\--

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4000.0 0.000 / TABLE NO. 02 REF. DATA

\--

\-- SALTCONC BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.005 2.5E-6 0.320 0.0

6.0 0.985 2.5E-6 0.320 0.0

12.0 0.930 2.5E-6 0.320 0.0 / TABLE NO. 02 SALT DATA
