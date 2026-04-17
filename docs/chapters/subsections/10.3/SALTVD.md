### SALTVD -- Equilibration Salt Concentration versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALTVD keyword defines the initial salt concentration versus depth tables for each equilibration region for when the salt (brine) phase has been activated in the model via the BRINE keyword in the RUNSPEC section, and the EQLOPT1 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section. Secondly, the keyword should also be used to set the initial salt concentration versus depth if OPM Flow's PRECSALT keyword in the RUNSPEC section has been used to activate the simulators Salt Precipitation model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth for corresponding salt concentrations SALTCON. | None |
| feet | m | cm |  |
| 2 | SALTCON | A columnar vector of real monotonically increasing down the column values that defines the corresponding salt concentration within the water phase for the given depth. There should be one columnar vector for each type of salt.<br>For the standard Brine Model there is only one salt type and therefore there should be only one columnar vector of SALTCON.<br>However, if the BRINE keyword has been invoked with the ECLMC keyword in the RUNSPEC section, then there should one columnar SALTCON vector for each declared salt type.<br>It is recommended to provide initial salt concentrations less then or equal to values provided by SALTSOL keyword in the PROPS section. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUIL tables as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQlDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.40: SALTVD Keyword Description

#### Examples

The first example activates the standard Brine Tracking model using the BRINE keyword in the RUNSPEC section and sets the number of equilibrium regions to three (NTEQUIL set to 3 on the EQLDIMS keyword also in the RUNSPEC), that is:

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

Then in the SOLUTION section the SALTVD keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DEPTH SALT-1 SALT-2 SALT-3 SALT-4

\-- SALTCON SALTCON SALTCON SALTCON

\-- \-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- SALTVD

3000.0 1.200

8000.0 1.200 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.300

8000.0 1.300 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.400

8000.0 1.400 / EQUIL REGN 03

The next example shows how the SALTVD keyword is entered when both the ECLMC and BRINE keywords have activated the Multi-Component Brine model in the RUNSPEC section, that is:

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

\--

\-- ACTIVATE MULTI-COMPONENT BRINE MODEL

\--

ECLMC

\--

\-- DEFINE WATER PHASE MULTI-COMPONENT BRINE COMPONENTS

\--

\-- SALT1 SALT2 SALT3 SALT4 SALT5

BRINE

NACL CACL MGC03 /

The above example activates the Multi-Component Brine model with three different water salinities for three equilibrium regions. In this case the resulting SALTVD keyword would be of the form:

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

\--

\-- DEPTH SALT-01 SALT-02 SALT-03 SALT-04

\-- CONCENTR CONCENTR CONCENTR CONCENTR

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- SALTVD

3000.0 1.200 0.540 0.020

7000.0 1.200 0.640 0.040 / EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.300 0.440 0.020

8000.0 1.300 0.540 0.040 / EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

5000.0 1.400 0.640 0.002

8000.0 1.400 0.640 0.002 / EQUIL REGN 03

In this case there are three data sets, on one for each equilibrium region and three SALTCON columnar vectors, one for each salt type (NACL, CACL and MGC03) declared via the BRINE keyword in the RUNSPEC section.

Note that the Multi-Component Brine model is not available in OPM Flow.
