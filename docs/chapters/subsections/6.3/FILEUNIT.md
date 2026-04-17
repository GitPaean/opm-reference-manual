### FILEUNIT -- Activate Unit Consistency Checking

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FILEUNIT keyword defines the units of the data set, and is used to verify that the units in the input deck and any associated include files are consistent. The keyword does not provide for the conversion between different sets of units.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FILEUNIT | A character string that defines the units of the data set, and should be set to:<br>1)  FIELD for field units,<br>2)  METRIC for metric units, or<br>3)  LAB for laboratory units | None |
| Notes:<br>1)  No unit conversion is performed.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.38: FILEUNIT Keyword Description

OPM Flow\'s behavior is controllable through the \"UNIT_SYSTEM_MISMATCH\" environment variable. The default behavior if the check fails (i.e., if one of the INCLUDE files has a unit system different from the main run specification) is to terminate the simulation with an error.

#### Example

\--

\-- ACTIVATE UNIT CONSISTENCY CHECKING

\--

FILEUNIT

FIELD /

The above example defines the data set units to be FIELD units.
