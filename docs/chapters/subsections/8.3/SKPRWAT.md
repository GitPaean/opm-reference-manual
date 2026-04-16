### SKPRWAT -- Polymer Molecular Weight Model Water Injection Skin Table

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [SKPRWAT](#__RefHeading___Toc473331_212435257111), describes the relationship of a water injection well\'s injected water skin pressure as a function of water throughput and water velocity, for the simulator\'s Polymer Molecular Weight Transport option. The table is a two dimensional table that relates the water throughput values and water velocity values to derive the resulting wellbore skin pressure of the injected water, which is then used to calculate the total wellbore skin pressure based on the polymer concentration.

This keyword should only be used if the [POLYMER](#__RefHeading___Toc38609_2267116897) and [POLYMW](#__RefHeading___Toc38609_22671168971) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section are also activated.

| 1-1 | SKPRWNUM | A positive integer value greater than zero and less than or equal to the NTSKWAT variable, as defined on the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the [SKPRWAT](#__RefHeading___Toc473331_212435257111) Polymer Molecular Weight Model water injection skin pressure table number. | None |
| --- | --- | --- | --- |
| 2-1 | THRUPUT | A real positive monotonically increasing vector, that defines the water throughput values. The first entry should be zero to define a no throughput data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet^3^/feet^2^ | m^3^/m^2^ | cm^3^/cm^2^ |  |
| 3-1 | VELOCITY | A real positive monotonically increasing vector, that defines the water velocity values. The first entry should be zero to define a no velocity data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet/day | m/day | cm/hour |  |
| 4-1 | PRESS | A series of real positive vectors representing the wellbore skin pressure, for all combinations of the water throughput values (THRUPUT) and velocity values (VELOCITY), organized as a series of vectors PRESS(THRUPUT, VELOCITY).<br>Thus, the first vector represents the wellbore skin pressure of the first THRUPUT value and each entry in the vector is the corresponding wellbore skin pressure of the associated VELOCITY vector. Each vector should be on a separate line and should be terminated by a "/".<br>Thus, if THRUPUT has three entries and VELOCITY has four, then there should be three vectors, with each vector containing four elements representing wellbore skin pressure values, as a function of THRUPUT and VELOCITY. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword should be terminated by a "/", but may be repeated up to NTSKWAT times, as per the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, to allow for the input of multiple tables. |  |  |  |

Table 8.157: SKPRWAT Keyword Description

Unlike other [PROPS](#__RefHeading___Toc39329_784232322) section table keywords, that enable multiple tables following the keyword to be entered, the [SKPRWAT](#__RefHeading___Toc473331_212435257111) keyword requires that the keyword itself must be repeated for each table, as is shown in the example on the following page.

The [WSKPTAB](#__RefHeading___Toc121649_241258616011) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section may be used to assign the [SKPRPOLY](#__RefHeading___Toc473331_21243525711) and [SKPRWAT](#__RefHeading___Toc473331_212435257111) tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

See also the [SKPRPOLY](#__RefHeading___Toc473331_21243525711), [PLYMWINJ](#__RefHeading___Toc473331_2124352571), and [PLYVMH](#__RefHeading___Toc473331_21243525712) keywords, in the [PROPS](#__RefHeading___Toc39329_784232322) section, that are the additional property keywords required for the Polymer Molecular Weight Transport option. In addition, see also the [WPMITAB](#__RefHeading___Toc121649_24125861601) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that assigns the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) tables to the water injection wells.

Note that the standard polymer property data keywords: [PLYROCK](#__RefHeading___Toc110216_2939291539), [PLYADS](#__RefHeading___Toc121087_57619843), [PLYMAX](#__RefHeading___Toc110214_2939291539), etc., are still required to fully describe the polymer fluid.

#### Example

Given NTSKWAT equals two on the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then two [SKPRWAT](#__RefHeading___Toc473331_212435257111) tables are required to be entered:

\--

\-- POLYMER MOLECULAR WEIGHT MODEL WATER INJECTION SKIN TABLE

\-- (OPM FLOW PROPS KEYWORD)

\--

SKPRWAT

1 / TABLE NUMBER

\--

\-- THROUGHPUT VALUES

\--

0.0 200.0 400.0 /

\--

\-- VELOCITY VALUES

\--

0.0 50.0 70.0 100.0 /

\--

\-- PRESS SKIN VALUES

\--

0.0 2.0 4.0 8.0 / PRESS(THRUPUT=1, VELOCITY=1 TO N)

0.0 20.0 40.0 80.0 / PRESS(THRUPUT=2, VELOCITY=1 TO N)

0.0 50.0 100.0 200.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)

/

SKPRWAT

2 / TABLE NUMBER

\--

\-- THROUGHPUT VALUES

\--

0.0 200.0 400.0 /

\--

\-- VELOCITY VALUES

\--

0.0 30.0 50.0 100.0 /

\--

\-- PRESS SKIN VALUES

\--

0.0 2.0 4.0 8.0 / PRESS(THRUPUT=1, VELOCITY=1 TO N)

0.0 20.0 40.0 80.0 / PRESS(THRUPUT=2, VELOCITY=1 TO N)

0.0 50.0 100.0 200.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)

/

As mentioned previously, the [SKPRWAT](#__RefHeading___Toc473331_212435257111) keyword requires that the keyword itself must be repeated for each table, as is shown in the above example.
