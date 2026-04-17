### SDENSITY -- Define the Miscible or Solvent Surface Gas Density

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SDENSITY keyword defines density at surface conditions of either the miscible injection gas for when the MISCIBLE option has been invoked in the RUNSPEC section, or the solvent for when the SOLVENT option has been invoked in the RUNSPEC section. This keyword must be invoked if either the MISCIBLE or SOLVENT options have been activated in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SDENSITY | SDENSITY is a real positive number defining the density at surface conditions of either:<br>1)  the miscible injection gas for when the MISCIBLE option has been invoked in the RUNSPEC section, or,<br>2)  the solvent for when the SOLVENT option has been invoked in the RUNSPEC section. | None |
| lb/ft^3^ | kg/m^3^ | gm/cc |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.145: SDENSITY Keyword Description

In addition to this keyword, the surface density or gravity of the in-place natural gas must be entered using either the DENSITY or GRAVITY keywords.

#### Examples

The following shows the SDENSITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to one.

\--

\-- MIS-SOL

\-- DENSITY

\-- \-\-\-\-\-\--

SDENSITY

0.04520 / MIS-SOL DENSITY

The next example shows the SDENSITY keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.

\--

\-- MIS-SOL

\-- DENSITY

\-- \-\-\-\-\-\--

SDENSITY

0.04520 / MIS-SOL DENSITY 1

0.05520 / MIS-SOL DENSITY 2

0.06420 / MIS-SOL DENSITY 3

There is no terminating "/" for this keyword.
