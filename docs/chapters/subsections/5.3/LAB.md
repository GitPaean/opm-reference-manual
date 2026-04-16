### LAB -- Activate the Laboratory System of Units for the Model

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the LABORATORY system of units for the model.

OPM Flow has three sets of units, namely: [METRIC](#__RefHeading___Toc70639_2267116897), [FIELD](#__RefHeading___Toc71850_2267116897) and [LAB](#__RefHeading___Toc72458_2267116897) and one of these keyword should be invoked in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to avoid any ambiguity. Both the simulator input and output units are controlled by including one of the [METRIC](#__RefHeading___Toc70639_2267116897), [FIELD](#__RefHeading___Toc71850_2267116897) or [LAB](#__RefHeading___Toc72458_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section of the input file.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- SWITCH ON THE LABORATORY SYSTEM OF UNITS FOR BOTH INPUT AND OUTPUT

\--

LAB

The above example switches on the LABORATORY system of units for the model.
