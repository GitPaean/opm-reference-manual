### SALTNODE -- Salt Concentration Based PVTNUM Array

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SALTNODE defines the salt concentration value based on a cells PVTNUM number. The SALTNODE property is used in the calculation of a polymer viscosity when the polymer and the salt options has been activated by the POLYMER and BRINE keywords in the RUNSPEC section. In the RUNSPEC section the number of PVTNUM functions is declared by NTPVT variable on the TABDIMS keyword and allocated to individual cells by the PVTNUM property array in the REGIONS section. NPPVT on the TABDIMS keyword in the RUNSPEC section defines the maximum number of rows (or pressure values) in the PVT tables and also sets the maximum number of entries for each SALNODE data set. The number of values for each data set must correspond to the number of polymer solution adsorption entries on the PLYADSS keyword. For example if there are three sets of PVT tables and four values on the PLYADSS keyword, then three SALTNODE data sets with four values of salt concentrations need to be entered.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Field | Metric | Laboratory |  |
| 1 | SALTNODE | A real monotonically increasing positive columnar vector defining the salt concentration for a given PVTNUM table. | None |  |  |
| lb/stb | kg/sm3 | gm/scc |  |  |  |
| Notes:<br>1)  Each table is terminated by a "/" including the last table; however, there is no "/" terminator for the keyword. |  |  |  |  |  |

Table 8.141: SALTNODE Keyword Description

An alternative manner of entering the salt concentrations is by utilizing the PVTNUM region array by using the ADSALNOD keyword in the PROPS section.

#### Example

Given three sets of relative permeability tables and four values on the PLYADSS keyword and two SALNODE data sets with four values of salt concentrations then the data should be entered as follows:

\--

\-- SETS SALT CONCENTRATION FOR POLYMER SOLUTION ADSORPTION

\-- VIA PVTNUM ARRAY ALLOCATION

\--

\-- SALT

\--

SALTNODE

1.0

5.0

10.5

25.0 / PVTNUM TABLE NO. 01

1.0

3.0

7.5

15.0 / PVTNUM TABLE NO. 02

See also the ADSALNOD keyword.
