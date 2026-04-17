### SALTSOL -- Define the Salt Solubility Limit by Region

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SALTSOL defines a grid block\'s maximum salt solubility for each PVTNUM region. The keyword should only be used with OPM Flow's Salt Precipitation model which is activated via the PRECSALT keyword in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SALTSOL | A real positive value that defines the maximum salt solubility for all grid blocks in a PVTNUM region. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| ‍2<br>‍ | | SALTDEN<br>| | | SALTDEN is a real number defining the density of salt at surface conditions.<br>| | | Defined<br>| |
| lb/ft^3^<br>135.469 | kg/m^3^<br>2170 | gm/cc<br>2.170 |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.142: SALTSOL Keyword Description

See also the PRECSALT and VAPWAT keywords in the RUNSPEC section and the PVTGW and PVTGWO keywords in the PROPS section.

#### Example

The first example sets the maximum salt solubility for all cells in the model to 134.6 lb/stb, assuming that there is only one PVT region, that is NTPVT is equal to one on the TABDIMS keyword in the RUNSPEC section.

\--

\-- SET SALT SOLUBILITY LIMIT FOR EACH REGION (OPM FLOW KEYWORD)

\--

SALTSOL

\-- MAX SALT

\-- SALTSOL DENSITY

134.6 1\* /

The 134.6 lb/stb, (380 kg/sm3 or 0.384 gm/scc for metric and laboratory units, respectively) is based on the solubility of NACL at 212 ^o^F (100 ^o^C) and should be used with care.

The next example shows how to set the maximum salt solubility for when NTPVT is equal to three on the TABDIMS keyword in the RUNSPEC section.

\--

\-- SET SALT SOLUBILITY LIMIT FOR EACH REGION (OPM FLOW KEYWORD)

\--

SALTSOL

134.6 / PVT REGION NO. 1

124.0 / PVT REGION NO. 2

/ PVT REGION NO. 3

Here the last entry, which is for region number three, is defaulted, and results in region's three maximum salt solubility to take the previous value, in this case 124.0 lb/stb.
