### SALTP -- Define the Initial Precipitated Salt Volume Fraction for All Grid Blocks

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SALTP](#__RefHeading___Toc486358_4287353749) keyword defines the initial equilibration precipitated salt volume fraction values for all grid cells in the model and should be used in conjunction with the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the salt (brine) phase has been activated in the model via the [BRINE](#__RefHeading___Toc162083_289573908) keyword, and the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword to activate OPM Flow's Salt Precipitation Model. Both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SALTP](#__RefHeading___Toc486358_4287353749) | [SALTP](#__RefHeading___Toc486358_4287353749) is an array of real positive numbers that are greater than or equal to zero and less than or equal to one, that define the initial equilibration salt volume fraction values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.15. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, unless the [BOX](#__RefHeading___Toc42110_3671211675) keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the [BOX](#__RefHeading___Toc42110_3671211675) statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.37: SALTP Keyword Description

See also the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [PRESSURE](#__RefHeading___Toc135627_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords to fully define the initial state of the model.

#### Example

The example activates the standard Brine Tracking model using the [BRINE](#__RefHeading___Toc162083_289573908) keyword, OPM Flow's Salt Precipitation model using the [PRECSALT](#__RefHeading___Toc332782_3149455253) keyword, and OPM Flow's vaporized water phase with the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword; all three keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

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

Then in the [SOLUTION](#__RefHeading___Toc43947_784232322) section the [SALTP](#__RefHeading___Toc486358_4287353749) keyword would be of the form:

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
