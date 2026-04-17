### SALTPVD -- Initial Precipitated Salt Volume Fraction versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALTPVD keyword defines the initial precipitated salt volume fraction versus depth tables for each equilibration region for when OPM Flow's Salt Precipitation Model has been activated in the input deck via the PRECSALT keyword in the RUNSPEC section. The keyword defines the initial deposited salt as a volume fraction (Ss), that is solid salt saturation.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth for corresponding salt volume fraction SALTPSAT. | None |
| feet | m | cm |  |
| 2 | SALTPSAT | A columnar vector of real values that defines the corresponding volume fraction of precipitated salt for the given depth.<br>Note only the standard Brine Model is supported and therefore there should be only one columnar vector of SALTPSAT. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTEQUL tables as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQlDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.38: SALTPVD Keyword Description

Precipitated salt can be viewed in OPM ResInsight via the SALTP dynamic grid variable that represents the precipitated salt saturation.

#### Example

The example activates the standard Brine Tracking model using the BRINE keyword, OPM Flow's Salt Precipitation model using the PRECSALT keyword, and OPM Flow's vaporized water phase with the VAPWAT keyword; all three keywords are in the RUNSPEC section. The example also sets the number of equilibrium regions to three (NTEQUL set to three on the EQLDIMS keyword also in the RUNSPEC), that is:

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

Then in the SOLUTION section the SALTPVD keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- PRECIPITATED SALT VOLUME FRACTION VERSUS DEPTH (OPM FLOW KEYWORD)

\--

\-- DEPTH SALTPSAT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

SALTPVD

3000.0 0.000

8000.0 0.000 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.000

8000.0 0.000 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.000

8000.0 0.000 / EQUIL REGN 03

Here the initial precipitated salt volume fraction has been set to zero for all three equilibration regions.
