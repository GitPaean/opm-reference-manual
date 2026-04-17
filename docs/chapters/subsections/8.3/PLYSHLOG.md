### PLYSHLOG -- Activate and Define the Polymer Shearing Logarithmic Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates and defines the parameters for the logarithm-based polymer shear thinning/thickening option.

| 1-1 | POLCON | A real positive value that defines the reference polymer concentration for the VELOCITY and VISFAC data for this keyword. | None |
| --- | --- | --- | --- |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 1-2 | SALTCON | A real positive value that defines the reference salt concentration for the VELOCITY and VISFAC data for this keyword.<br>Note that If the BRINE option has not been activated by the BRINE keyword in the RUNSPEC section, then this variable is ignored.<br>This variable is ignored as the BRINE option is not implemented in OPM Flow. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 1-3 | TEMP | A real positive value defines the reference polymer temperature for the VELOCITY and VISFAC data for this keyword.<br>Note that If the TEMP option has not been activated by the TEMP keyword in the RUNSPEC section, then this variable is ignored.<br>This variable is ignored as the TEMP and POLYMER options combination is not implemented in OPM Flow. | None |
| ^o^F | ^o^C | ^o^C |  |
| 1-4 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | VELOCITY | A columnar vector of real monotonically increasing down the column values that defines the water-polymer flow velocity for the reference conditions of POLCON, SALTCON and TEMP.<br>The VELOCITY value for the first row in the table should be a very small value that is greater than zero and less than 1 x 10-6. | None |
| feet/day | m/day | cm/hour |  |
| 2-2 | VISFAC | A columnar vector of real positive values that define the dimensionless shear effect multiplier for the given VELOCITY entry for the reference conditions of POLCON, SALTCON and TEMP.<br>Normally VISFAC value for the first row in the table should be one. | None |
| dimensionless | dimensionless | dimensionless |  |
| 1-4 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must be entered with two records, with entries 1-1, 1-2, 1-3 and 1-4 representing record number one and 2-1, 2-2 and 2-3 representing record number two in the "No." column in this table.<br>3)  Each of the records are terminated by a "/" and is explicitly shown in the above rows.<br>4)  For record number two a minimum of two rows and a maximum of NPPVT rows, as declared on the TABDIMS keyword in the RUNSPEC section, are required.<br>5)  There is no "/" terminator for the keyword. |  |  |  |

Table 8.107: PLYSHLOG Keyword Description

See the PLYSHEAR keyword for the alternative polymer shear thinning/thickening option that is also implemented in OPM Flow.

#### Example

The following example show how to enter two PLYSHLOG tables given that the NTPVT variable on the TABDIMS keyword in the RUNSPEC section is set equal to two.

\--

\-- POLYMER SHEARING LOGARITHMIC PARAMETERS

\--

PLYSHLOG

\-- REF REF REF

\-- POLCON SALTCON TEMP

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\--

0.5

/

\--

\-- VELOCITY VISFAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.0000001 1.00

0.000001 1.10

0.0001 1.30

0.001 1.47

0.01 1.67

0.1 2.00

1.0 2.20

10.0 2.30

100.0 2.40

1000.0 2.40

/ TABLE NO. 01

\-- REF REF REF

\-- POLCON SALTCON TEMP

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\--

0.5

/

\--

\-- VELOCITY VISFAC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

0.0000001 1.00

0.000001 1.10

0.0001 1.35

0.001 1.57

0.01 1.87

0.1 2.20

1.0 2.40

10.0 2.60

100.0 2.65

1000.0 2.65

/ TABLE NO. 02

The example activates the polymer logarithmic shear thinning-thickening option and defines two polymer shear thinning-thickening tables, based on the NTPVT variable on the TABDIMS keyword in the RUNSPEC section being equal to two and NPPVT variable on the same keyword being greater than or equal to ten.
