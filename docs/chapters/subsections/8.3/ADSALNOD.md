### ADSALNOD -- Salt Concentration Based on SATNUM Array

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ADSALNOD defines the salt concentration value based on a cells SATNUM number. The ADSALNOD property is used in the calculation of a polymer viscosity when the polymer and the salt options has been activated by the POLYMER and BRINE keywords in the RUNSPEC section. In the RUNSPEC section the number of SATNUM functions is declared by the NTSFUN variable on the TABDIMS keyword and allocated to individual cells by the SATNUM property array in the REGIONS section. NSSFUN on the TABDIMS keyword in the RUNSPEC section defines the maximum number of rows (or saturation values) in the relative permeability saturation tables and also sets the maximum number of entries for each ADSALNOD data set. The number of values for each data set must correspond to the number of polymer solution adsorption entries on the PLYADSS keyword. For example, if there are three sets of relative permeability tables and four values on the PLYADSS keyword, then three ADSALNOD data sets with four values of salt concentrations need to be entered.

The salt concentrations within each data set should be positive and monotonically increasing and each ADSALNOD data set is delimited by "/" including the last data set.

| No. | Name | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
| 1 | SALTCON | Field | Metric | Laboratory | None |
| A real positive columnar vector that sets the salt concentrations for the given relative permeability saturation tables. |  |  |  |  |  |
| lb/stb | kg/sm3 | gm/scc |  |  |  |
| Notes:<br>1)  Each data set must be terminated by a "/" including the last data set. |  |  |  |  |  |

Table 8.17: ADSALNOD Keyword Description

An alternative manner of entering the salt concentrations is by utilizing the PVTNUM region array by using the SALTNODE* *keyword in the PROPS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

Given three sets of relative permeability tables and four values on the PLYADSS keyword, then the data salt concentration should be entered as follows:

\--

\-- SETS SALT CONCENTRATION FOR POLYMER SOLUTION ADSORPTION

\-- VIA SATNUM ARRAY ALLOCATION

\--

\-- SALT

\--

ADSALNOD

1.0

5.0

10.5

25.0 / SATNUM TABLE NO. 01

1.0

3.0

7.5

15.0 / SATNUM TABLE NO. 02

1.0

7.5

20.5

35.0 / SATNUM TABLE NO. 03

See also the SALTNODE* *keyword.
