### HEATCRT -- Define Reservoir Rock Heat Capacity Temperature Dependence for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HEATCRT keyword defines the reservoir rock volumetric heat capacity temperature dependence for all cells for when OPM Flow's thermal calculation is activated by the THERMAL keywords in the RUNSPEC section.

This keyword can only be used if OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | HEATCRT | HEATCRT is an array of real positive numbers that define reservoir rock volumetric heat capacity temperature dependence of a grid block.<br>Repeat counts may be used, for example 3000\*0.05 | None |
| Btu/ft3/°R2 | kJ/m3/K2 | J/cm3/K2 |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

*Table 6.44: HEATCRT Keyword Description*
Note this keyword is incompatible with SPECROCK keyword in the PROPS section.

The data for this keyword and the HEATCR keyword are used to calculate the reservoir rock volumetric heat capacity temperature dependence using the following relationship:

#### Example

\--

\-- DEFINE RESERVOIR ROCK HEAT CAPACITY TEMPERATURE DEPENDENCE

\-- FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\-- KEYWORD IS INCOMPATIBLE WITH THE SPECROCK KEYWORD

\-- (OPM FLOW THERMAL OPTION ONLY)

\--

HEATCRT

300\*0.05 /

The above example defines the reservoir rock volumetric heat capacity temperature dependence of 0.05 for each cell in the 300 grid block model.
