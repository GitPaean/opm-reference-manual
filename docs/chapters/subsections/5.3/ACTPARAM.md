### ACTPARAM -- Define Action Facility Target and Tolerance Parameters

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ACTPARAM keyword defines the maximum target percent value for the ACTION series of keywords and the fractional equality tolerance for determining if two numbers are numerically equal when comparing values using the ACTION series of keywords. The ACTION keyword allows the user to enter computational logic and calculations to the simulation run based on the how the simulation run is proceeding.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | MXTOLS | A positive real value that defines the maximum target percent number for the ACTION series of keywords.<br>The default value of 100 means the target is not applied. | Defined |
| percent<br>100.0 | percent<br>100.0 | percent<br>100.0 |  |
| 2 | MXEQLS | MXEQLS a real positive number greater than zero and less than one that defines the tolerance used to determine if two real values are equal for comparing values in the ACTION series of keywords.<br>Floating-point numbers (as implemented in computers) are never exact, one cannot compare floating point numbers for exact equality. Thus, MXEQLS defines a tolerance. For example, the default value of 1 x 10-4 means that if the difference between two real values is less than 1 x 10-4 then the values are considered equal. | Defined |
| fraction<br>1 x 10-4 | fraction<br>1 x 10-4 | fraction<br>1 x 10-4 |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.4: ACTPARAM Keyword Description

Although this keyword is read by OPM Flow, the ACTION and UDQ computational logic and calculations have not been fully implemented and therefore this keyword should not be used as it may result in OPM Flow terminating.

#### Example

\--

\-- ACTION ACTION

\-- MXTOLS MXEQLS

ACTPARAM

5.0 1.0E-4 /

The above example defines the maximum tolerance to be 5% and the equality tolerance to be the default value of 1.0 x 10-4.
