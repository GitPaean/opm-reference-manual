### APIVD -- Equilibration Oil API Gravity versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The APIVD keyword defines the oil API gravity versus depth tables for each equilibration region when API Tracking as been activated by the API keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding API gravity values, API. | None |
| feet | m | cm |  |
| 2 | API | A columnar vector of real values that defines the API gravity at the corresponding DEPTH.<br>The American Petroleum Institute ("API") classifies oils based on an API gravity (γ~API~), or degrees API (^o^API), the relationship between relative density (γ~o~) of oil and API gravity (γ~API~) is given by: | None |
| ^o^API | ^o^API | ^o^API |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.5: APIVD Keyword Description

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the bubble-point versus depth functions.

\--

\-- DEPTH API

\-- GRAVITY

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

APIVD

3000.0 41.10

8000.0 41.10 / API VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 41.10

8000.0 38.50 / API VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 41.10

8000.0 38.50 / API VS DEPTH EQUIL REGN 03

Here three tables are entered; the first table has a constant API gravity versus depth relationship for equilibration region number one and the other two equilibration regions have the API gravity varying with depth.
