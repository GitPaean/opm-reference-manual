### WSURFACT -- Define Water Injection Well Surfactant Concentration

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WSURFACT defines a water injection well's surfactant concentration in the injection stream that is to be used when the Surfactant phase has been activated by either the SURFACT or SURFACTW keywords in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name of a gas injection well for which the solvent fraction data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | SURCON | A real positive value that defines the surfactant concentration of the well's injection stream. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.125: WSURFACT Keyword Description

Water injection wells that are not declared via this keyword have their surfactant concentrations set to zero.

See also the GCONINJE keyword to define a group's injection targets and constraints, and the WCONINJE keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the surfactant concentrations for three water injection wells for when the surfactant phase option has been activated by either the SURFACT or SURFACTW keywords in the RUNSPEC section. Here the surfactant concentration has been set to 0.200 for all three wells.

\--

\-- DEFINE WATER INJECTION WELL SURFACTANT CONCENTRATION

\--

\-- WELL SURFACT

\-- NAME SURCON

\-- \-\-\-\-\-\-\--

WSURFACT

WI01 0.2000 /

WI02 0.2000 /

WI03 0.2000 /

/
