### UDTDIMS -- Define the Dimensions of the User Defined Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions of the User Defined Tables ("UDT") used by OPM Flow that can be used as lookup tables when assigning values to User Defined Quantities (\"UDQ\") using the UDQ keyword in the SCHEDULE section. UDTs are defined by the UDT keyword in the SCHEDULE section.

| 1 | MXUDT | MXUDT is a positive integer that defines the maximum number of User Defined Tables | 0 |
| --- | --- | --- | --- |
| 2 | NUDT | NUDT is a positive integer that defines the maximum number of rows in any given User Defined Table. | 0 |
| 3 | MXINTP | MXINTP is a positive integer that defines the maximum number of interpolation points allowed in any given dimension. | 0 |
| 4 | MXDIMS | MXDIMS is a positive integer that defines the maximum number of dimensions in any given User Defined Table.<br>Only one dimensional tables are currently supported by OPM Flow. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.53: UDTDIMS Keyword Description

#### Example

\--

\-- USER DEFINED TABLE DIMENSIONS

\--

\-- MAX MAX MAX MAX

\-- TABLES ROWS INTPOL DIMS

UDTDIMS

3 20 3 2 /

In the above example the maximum number of UDT tables is set to three and the maximum number of rows for each table is 20, the maximum number of interpolation points in any given dimension is set to three and the maximum number of dimensions is defined as two.
