### UDTDIMS -- Define the Dimensions of the User Defined Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the dimensions of the User Defined Tables ("UDT") used by OPM Flow that can be used as lookup tables when assigning values to User Defined Quantities (\"[UDQ](#__RefHeading___Toc161095_2932703077)\") using the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. UDTs are defined by the [UDT](#__RefHeading___Toc1674916_4250154414) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

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

In the above example the maximum number of [UDT](#__RefHeading___Toc1674916_4250154414) tables is set to three and the maximum number of rows for each table is 20, the maximum number of interpolation points in any given dimension is set to three and the maximum number of dimensions is defined as two.
