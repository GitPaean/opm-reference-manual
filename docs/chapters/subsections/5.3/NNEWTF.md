### NNEWTF -- Activate the Non-Newtonian Fluid Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the Non-Newtonian Fluid phase and model for when the polymer phase is present in the model, as indicated by the POLYMER keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | NTHRBL | A positive integer that defines the maximum number of Herschel-Bulkley versus polymer concentration tables to be used with the polymer model, as entered via the FHERCHBL keyword in the PROPS section.<br>The tables are allocated to different parts of the grid by the HBNUM keyword in the REGIONS section | NTPVT |
| --- | --- | --- | --- |
| 2 | NLNHBL | A positive integer that defines the maximum number of rows for each table entered by the FHERCHBL keyword in the PROPS section. | 2 |
| Notes:<br>1)  The exact number of NTHRBL tables are required to completed the data set. For example, if NTHRBL is set equal to three, then there must be three tables entered for the FHERCHBL keyword.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.27: NNEWTF Keyword Description

#### Example

\--

\-- MAX MAX

\-- NTHRBL NLNHBL

NNEWTF

3 5 /

The above example defines maximum number of Herschel-Bulkley tables to be three with a maximum number of rows for each table set to five.
