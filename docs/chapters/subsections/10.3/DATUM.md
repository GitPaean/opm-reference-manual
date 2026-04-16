### DATUM -- Define the Datum Depth for the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [DATUM](#__RefHeading___Toc135613_1317547213) keyword defines the datum depth for the model. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DATUM](#__RefHeading___Toc135613_1317547213) | [DATUM](#__RefHeading___Toc135613_1317547213) is a single positive value that defines the datum depth for the model. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 10.11: DATUM Keyword Description

See also the [DATUMR](#__RefHeading___Toc135615_1317547213) and [DATUMRX](#__RefHeading___Toc298753_1539708736) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section that also define the datum depth for the model.

#### Example

\-- DATUM

\-- DEPTH

\-- \-\-\-\-\--

DATUM

5000.0 / DATUM DEPTH FOR REPORTING

The above example defines the datum for the model to be 5000.0
