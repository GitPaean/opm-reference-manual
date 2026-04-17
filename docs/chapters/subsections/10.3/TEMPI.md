### TEMPI -- Define the Initial Temperature Values for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the initial reservoir temperature for each cell in the model. The keyword is used to explicitly define the initial reservoir temperature via the Enumeration Initialization method rather than defining a uniform initial temperature or defining temperature versus depth tables.

The initial reservoir temperature must be defined when OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil temperature model, and the THERMAL keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow's CO~2~ or H~2~ storage option has been activated by the CO2STORE or H2STORE keyword in the RUNSPEC section.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMPI | TEMPI is an array of real positive numbers assigning the initial temperature to each cell in the model.<br>Repeat counts may be used, for example 20\*100.0. | None |
| ^o^F | ^o^C | ^o^C |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.58: TEMPI Keyword Description

See also the RTEMP keyword in the PROPS section and the RTEMPVD keyword in the SOLUTION section for alternative ways to initialize the model's initial temperature.

#### Example

\--

\-- DEFINE GRID BLOCK TEMPERATURE FOR ALL CELLS

-- (BASED ON NX x NY x NZ = 300)

\--

TEMPI

100\*212.0 100\*215.0 100\*220.0 /

The above example defines the initial temperature to be 212.0, 215.0, and 220.0 oF for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword in the RUNSPEC section.
