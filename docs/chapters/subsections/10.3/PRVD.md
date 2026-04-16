### PRVD -- Define the Initial Equilibration Pressures versus Depth

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PRVD](#__RefHeading___Toc288806_501926209) keyword defines the initial reservoir pressure versus depth and should be used in conjunction with the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords etc., to fully describe the initial state of the model. [PRVD](#__RefHeading___Toc288806_501926209) is an alternative to the [PRESSURE](#__RefHeading___Toc135627_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, that defines the initial equilibration pressures for all grid cells in the model

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section. This is the non-standard formulation to initialize the model and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#__RefHeading___Toc58139_3701168388) | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding reservoir oil pressures values, [PRESSURE](#__RefHeading___Toc135627_1317547213). | None |
| feet | m | cm |  |
| 2 | [PRESSURE](#__RefHeading___Toc135627_1317547213) | A columnar vector of real values that defines the initial equilibration oil pressure values at the corresponding [DEPTH](#__RefHeading___Toc58139_3701168388). | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.24: PRVD Keyword Description

See also the [PBUB](#__RefHeading___Toc135619_1317547213), [PDEW](#__RefHeading___Toc135623_1317547213), [RS](#__RefHeading___Toc137361_1317547213), [RV](#__RefHeading___Toc137365_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords to fully define the initial state of the model.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to five on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the following example defines the initial oil reservoir pressure versus depth

\--

\-- DEPTH INIT

\-- PRESS

\-- \-\-\-\-\-- \-\-\-\-\--

PRVD

3000.0 3000.0

4000.0 3345.0

5000.0 3690.0

7000.0 4700.0

7200.0 4769.0 / POIL VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 3100.0

4000.0 3445.0

5000.0 3790.0

7000.0 4700.0

7200.0 4769.0 / POIL VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 3150.0

4000.0 3495.0

5000.0 3840.0

7000.0 4700.0

7200.0 4769.0 / POIL VS DEPTH EQUIL REGN 03

Here three tables are entered and each table is terminated by a "/" and there is no keyword terminating "/".
