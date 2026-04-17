### RSCONST -- Define Constant GOR (Rs) for All Dead Oil PVT Fluids

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

RSCONST defines a constant Gas-Oil Ratio ("GOR"), for all dead oil[^1] PVT fluids. If the oil has a constant and uniform dissolved gas concentration, GOR, and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the GAS and DISGAS keywords from the RUNSPEC section, treating the oil as a dead oil, and defining a constant Rs (GOR) value with keywords RSCONST or RSCONSTT in the PROPS section. This results in the model being run as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | RS | A real positive value that defines the dead oil GOR for all oil PVT tables in the model | None |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |
| 2 | PRESS | A real positive value that defines that saturation pressure (bubble point pressure) for all the oil PVT tables in the model. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.133: RSCONST Keyword Description

See also the RSCONSTT keyword to define a different constant Rs to the various dead oil PVT tables and the PVDO and PVCDO keywords to enter the dead oil properties. All of the aforementioned keywords are in the PROPS section.

#### Example

The example sets the dead oil GOR to 5 scf/stb and the bubble point pressure to 14.7 psia.

\--

\-- DEAD OIL PVT CONSTANT GOR AND SATURATION PRESSURE

\--

RSCONST

\-- RS PSAT

\-- MSCF/STB PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\--

0.0050 14.7 /

[^1]: "Dead" oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.
