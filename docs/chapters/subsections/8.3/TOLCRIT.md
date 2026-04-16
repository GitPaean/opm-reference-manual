### TOLCRIT -- Define The Critical Saturation Tolerance

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Critical fluid saturations are determined from the relative permeability tables, that is the last saturation in a relative permeability table where the relative permeability of a phase is set equal to zero. Since floating-point numbers (as implemented in computers) are never exact, one cannot compare floating point numbers for exact equality. Thus, this keyword defines a value below which is considered equivalent to zero in determining the critical saturation for a phase.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [TOLCRIT](#__RefHeading___Toc138557_1496523326) | [TOLCRIT](#__RefHeading___Toc138557_1496523326) is a real positive number greater than zero and less than one that defines the critical saturation tolerance used to determine the critical saturation of a fluid in the relative permeability tables.<br>The default value of 1 x 10-6 means that relative permeabilty values less than this value will be treated as being equal to zero. | 1 x 10^-6^ |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.193: TOLCRIT Keyword Description

See also section [[8.2.4](#anchor-2)](#8.2.2.Saturation Tables (Relative Permeability and Capillary Pressure Tables)|outline)[](#8.2.2.Saturation Tables (Relative Permeability and Capillary Pressure Tables)|outline)[[Saturation Tables (Relative Permeability and Capillary Pressure Tables)](#anchor-2)](#8.2.2.Saturation Tables (Relative Permeability and Capillary Pressure Tables)|outline) for a description of the relative permeability tables and the various end-point definitions, including oil, water and gas critical saturations.

#### Example

\-\--

\-- SET THE CRITICAL SATURATION TOLERANCE

\--

TOLCRIT

1.0E-6 /

The above example defines the critical saturation tolerance to be the default value of 1 x 10-6.
