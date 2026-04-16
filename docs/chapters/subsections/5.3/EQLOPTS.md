### EQLOPTS -- Activate the Equilibration Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [EQLOPTS](#__RefHeading___Toc131554_398689501) keyword defines the equilibration options by stating the character command to activate an option to be used for initializing the model. Multiple commands may be utilized to activate several equilibration options following the keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MOBILE | A character string that activates the mobile fluid critical saturation end point correction.<br>If the MOBILE command is stated then this option is activated.<br>This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| 2 | QUIESC | A character string that activates the initial quiescence option that modifies the equilibrium calculated phase pressures to ensure that a steady state solution is obtained. This options ensures that there is no flow potential between the grid blocks in a given region, which is the normal case when block-centered equilibration is used by setting BOINIT on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword to zero in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.<br>If the QUIESC command is stated then this option is activated.<br>This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| 3 | THPRES | A character string that activates the inter-region equilibration flow option. This option allows for a threshold pressure variable entered via the [THPRES](#__RefHeading___Toc210168_2884651453) keyword to define a pressure which prevents flow between regions until the [THPRES](#__RefHeading___Toc210168_2884651453) value between regions is exceeded.<br>If the [THPRES](#__RefHeading___Toc210168_2884651453) command is stated then this option is activated. | None |
| 4 | IRREVERS | A character string that activates the irreversible inter-region equilibration flow option. This option can only be invoked if the [THPRES](#__RefHeading___Toc210168_2884651453) command has been stated. The option allows for different [THPRES](#__RefHeading___Toc210168_2884651453) values for different directions.<br>If the IRREVERS command is stated then this option is activated.<br>This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.3.37.1: EQLOPTS Keyword Description

#### Example

\--

\-- ACTIVATE EQUILIBRATION OPTIONS

\-- MOBILE END-POINT(MOBILE) STEADY STATE(QUIESC) THRESHOLD(THPRES)

\-- IRREVERSIBLE THRESHOLD(IRREVERS)

EQLOPTS

\'THPRES\' \'IRREVERS\' /

The above example activates the threshold pressure option with different threshold pressure for different directions.
