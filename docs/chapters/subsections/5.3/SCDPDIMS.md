### SCDPDIMS -- Define Scale Deposition and Damage Table Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SCDPDIMS keyword defines the number of tables used in the Scale Deposition option and the maximum number of entries for the various tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | NTSCDP | NTSCDP is a positive integer that defines the number of SCDPTAB scale deposition tables used in the Scale Deposition option. | 0 |
| --- | --- | --- | --- |
| 2 | NPSCDP | NPSCDP is a positive integer that defines the maximum number of entries (or rows) in any one SCDPTAB scale deposition table defined in the input deck. | 0 |
| 3 | NTSCDA | NTSCDA is a positive integer that defines the number of SCDATAB scale damage tables used in the Scale Deposition option. | 0 |
| 4 | NPSCDA | NPSCDA is a positive integer that defines the maximum number of entries (or rows) in any one SCDATAB scale damage table defined in the input deck. | 0 |
| 5 | Not Used |  | 1\* |
| 6 | Not Used |  | 1\* |
| 7 | NTSCDE | NTSCDE is a positive integer that defines the number of SCDETAB karst aquifer dissolution tables used in the Scale Deposition option. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.41: SCDPDIMS Keyword Description

#### Example

\--

\-- NO. MAX NO. MAX NOT NOT NO.

\-- NTSCDP NPSCDP NTSCDA NPSCDA USED USED NTSCDE

SCDPDIMS

5 10 4 10 1\* 1\* 3 /

The above example defines the number of SCDPTAB scale deposition tables to be five with a maximum number of rows for each table set to 10, the maximum number of SCDATAB scale damage tables to be four with a maximum number of 10 rows per table, and the maximum number of SCDETAB karst aquifer dissolution tables to be three.
