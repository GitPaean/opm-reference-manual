### SALTP -- Define the Initial Precipitated Salt Volume Fraction for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALTP keyword defines the initial equilibration precipitated salt volume fraction values for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if the salt (brine) phase has been activated in the model via the BRINE keyword, and the PRECSALT keyword to activate OPM Flow's Salt Precipitation Model. Both keywords are in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SALTP | SALTP is an array of real positive numbers that are greater than or equal to zero and less than or equal to one, that define the initial equilibration salt volume fraction values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.15. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.37: SALTP Keyword Description

See also the PBUB, PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

The example activates the standard Brine Tracking model using the BRINE keyword, OPM Flow's Salt Precipitation model using the PRECSALT keyword, and OPM Flow's vaporized water phase with the VAPWAT keyword; all three keywords are in the RUNSPEC section.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- MAX MAX RSVD TVDP TVDP

\-- EQLNUM DEPTH NODES TABLE NODES

EQLDIMS

3 1\* 20 1\* 1\* /

\--

\-- ACTIVATE STANDARD BRINE MODEL

\--

BRINE

\--

\-- ACTIVATE THE OPM FLOW SALT PRECIPITATION MODEL (OPM FLOW KEYWORD)

\--

PRECSALT

\--

\-- VAPORIZED WATER IN WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)

\--

VAPWAT

Then in the SOLUTION section the SALTP keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DEFINE INITIAL PRECIPITATED SALT VOLUME FRACTION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SALTP

1000\*0.0000 1000\*0.0000 1000\*0.100 /

Here the initial equilibration precipitated salt volume fraction values are set to 0.0000 for all the cells in the first and second layers and finally 0.1000 for all the cells in the third layer.
