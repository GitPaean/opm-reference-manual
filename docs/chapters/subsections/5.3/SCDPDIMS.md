### SCDPDIMS -- Define Scale Deposition and Damage Table Dimensions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SCDPDIMS](#__RefHeading___Toc637730_516898843) keyword defines the number of tables used in the Scale Deposition option and the maximum number of entries for the various tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | NTSCDP | NTSCDP is a positive integer that defines the number of [SCDPTAB](#__RefHeading___Toc644093_516898843) scale deposition tables used in the Scale Deposition option. | 0 |
| --- | --- | --- | --- |
| 2 | NPSCDP | NPSCDP is a positive integer that defines the maximum number of entries (or rows) in any one [SCDPTAB](#__RefHeading___Toc644093_516898843) scale deposition table defined in the input deck. | 0 |
| 3 | NTSCDA | NTSCDA is a positive integer that defines the number of [SCDATAB](#__RefHeading___Toc618634_516898843) scale damage tables used in the Scale Deposition option. | 0 |
| 4 | NPSCDA | NPSCDA is a positive integer that defines the maximum number of entries (or rows) in any one [SCDATAB](#__RefHeading___Toc618634_516898843) scale damage table defined in the input deck. | 0 |
| 5 | Not Used |  | 1\* |
| 6 | Not Used |  | 1\* |
| 7 | NTSCDE | NTSCDE is a positive integer that defines the number of [SCDETAB](#__RefHeading___Toc624987_516898843) karst aquifer dissolution tables used in the Scale Deposition option. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.41: SCDPDIMS Keyword Description

#### Example

\--

\-- NO. MAX NO. MAX NOT NOT NO.

\-- NTSCDP NPSCDP NTSCDA NPSCDA USED USED NTSCDE

SCDPDIMS

5 10 4 10 1\* 1\* 3 /

The above example defines the number of [SCDPTAB](#__RefHeading___Toc644093_516898843) scale deposition tables to be five with a maximum number of rows for each table set to 10, the maximum number of [SCDATAB](#__RefHeading___Toc618634_516898843) scale damage tables to be four with a maximum number of 10 rows per table, and the maximum number of [SCDETAB](#__RefHeading___Toc624987_516898843) karst aquifer dissolution tables to be three.
