### THCONSF -- Define Gas Saturation Dependent Thermal Conductivity Scaling Factor for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The THCONSF keyword defines a gas saturation dependent scaling factor to the fluid and reservoir rock thermal conductivities entered via the THCONR keyword in the GRID section, for when the thermal calculation is activated by the THERMAL keyword in the RUNSPEC.

This keyword can only be used if the thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | THCONSF | THCONSF is an array of real positive numbers, greater than zero and less than or equal to one, that define the gas saturation dependent scaling factor that is applied to the THCONR data, entered via the THCONR keyword, to adjust the thermal conductivity of the reservoir cells in each grid block.<br>Repeat counts may be used, for example 3000\*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

*Table 6.125: THCROCK Keyword Description*
Note that there two ways to define the rock and in situ fluids thermal conductivity:

3)  1)  1)  Either by using the THCONR keyword to define the combined rock and fluid conductivity, and optionally the THCONSF keyword in the GRID section, or

        2)  by specifying the rock and fluid conductivities individually using the THCROCK, THCOIL, THCGAS, and THCWATER keywords in the GRID section.

Hence, the THCROCK and THCONR keywords are mutually exclusive.

Here, the THCONSF keyword defines a scaling factor which is a function of the gas saturation that scales a cells total thermal conductivity (reservoir fluids plus reservoir rock) entered via the THCONR keyword in the GRID section. This combination of keywords, THCONSF and THCONR implies that the oil and water phase thermal conductivities are saturation independent with respect to the liquid phase, and that only the gas saturation influences a cell's thermal conductivity as entered via the THCONR keyword.

Thus, THCONSF scales the THCONR values via a multiplier Ω, by:

See also the THCGAS, THCOIL, THCWATER and THROCK keywords in the GRID section, for an alternative way to enter the thermal conductivity properties. However, the THCONSF keyword cannot be used with the THCGAS, THCOIL, THCWATER and THCROCK keywords. Secondly, the commercial compositional simulator\'s THCSOLID keyword is not supported or required by OPM Flow.

#### Example

\--

\-- DEFINE GRID SGAS DEPENDENT SCALING FACTOR FOR THE THCONR ARRAY \-- FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\-- (OPM FLOW THERMAL OPTION ONLY)

\--

THCONSF

300\*0.12 /

The above example defines the gas saturation thermal conductivity scaling factor to be applied to the THCONR to be 0.12 for all 300 cells in the model, as defined by the DIMENS keyword in the RUNSPEC section.
