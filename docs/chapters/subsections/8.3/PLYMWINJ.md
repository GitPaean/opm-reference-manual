### PLYMWINJ -- Polymer Molecular Weight Model Throughput and Velocity Table

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [PLYMWINJ](#__RefHeading___Toc473331_2124352571), describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity. The table is a two dimensional table that relates the polymer throughput values and velocity values to derive the resulting molecular weight of the injected polymer, which is then used via the PLYVHM keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, to derive the polymer molecular weight scaled viscosity.

This keyword should only be used if the [POLYMER](#__RefHeading___Toc38609_2267116897) and [POLYMW](#__RefHeading___Toc38609_22671168971) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section are also activated.

| 1-1 | PLYMWNUM | A positive integer value greater than zero and less than or equal to the NTPMWINJ variable, as defined on the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) Polymer Molecular Weight Model throughput and velocity table number. | None |
| --- | --- | --- | --- |
| 2-1 | THRUPUT | A real positive monotonically increasing vector, that defines the polymer throughput values. The first entry should be zero to define a no throughput data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet^3^/feet^2^ | m^3^/m^2^ | cm^3^/cm^2^ |  |
| 3-1 | VELOCITY | A real positive monotonically increasing vector, that defines the polymer velocity values. The first entry should be zero to define a no velocity data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet/day | m/day | cm/hour |  |
| 4-1 | [POLYMW](#__RefHeading___Toc38609_22671168971) | A series of real positive vectors representing the polymer molecular weights for all combinations of the polymer throughput values (THRUPUT) and velocity values (VELOCITY), organized as a series of vectors [POLYMW](#__RefHeading___Toc38609_22671168971)(THRUPUT, VELOCITY).<br>Thus, the first vector represents the molecular weights of the first THRUPUT value and each entry in the vector is the corresponding molecular weight of the associated VELOCITY vector. Each vector should be on a separate line and should be terminated by a "/".<br>Thus, if THRUPUT has three entries and VELOCITY has four, then there should be three vectors, with each vector containing four elements representing molecular weight values, as a function of THRUPUT and VELOCITY. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| Notes:<br>1)  The keyword should be terminated by a "/", but may be repeated up to NTPMWINJ times, as per the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, to allow for the input of multiple tables. |  |  |  |

Table 8.104: PLYMWINJ Keyword Description

Unlike other [PROPS](#__RefHeading___Toc39329_784232322) section table keywords, that enable multiple tables following the keyword to be entered, the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) keyword requires that the keyword itself must be repeated for each table, as is shown in the example on the following page.

See also the [WPMITAB](#__RefHeading___Toc121649_24125861601) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that assigns the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) tables to the water injection wells, as well as the [SKPRWAT](#__RefHeading___Toc473331_212435257111), [SKPRPOLY](#__RefHeading___Toc473331_21243525711), and [PLYVMH](#__RefHeading___Toc473331_21243525712) keywords, in the [PROPS](#__RefHeading___Toc39329_784232322) section, that are the additional property keywords required for the Polymer Molecular Weight Transport option.

The [WSKPTAB](#__RefHeading___Toc121649_241258616011) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section may be used to assign the [SKPRPOLY](#__RefHeading___Toc473331_21243525711) and [SKPRWAT](#__RefHeading___Toc473331_212435257111) tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

Note that the standard polymer property data keywords: [PLYROCK](#__RefHeading___Toc110216_2939291539), [PLYADS](#__RefHeading___Toc121087_57619843), [PLYMAX](#__RefHeading___Toc110214_2939291539), etc., are still required to fully describe the polymer fluid.

#### Example

Given NTPMWINJ equals two on the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then two PLYWINJ tables are required to be entered:

\--

\-- POLYMER MOLECULAR WEIGHT MODEL THROUGHPUT AND VELOCITY TABLE

\-- (OPM FLOW PROPS KEYWORD)

\--

PLYMWINJ

1 / TABLE NUMBER

\--

\-- THROUGHPUT VALUES

\--

0.0 200.0 400.0 /

\--

\-- VELOCITY VALUES

\--

0.0 50.0 80.0 100.0 /

\--

\-- POLYMW VALUES

\--

20.0 19.0 18.0 16.0 / POLYMW(OUTPUT=1, VELOCITY=1 TO N)

20.0 16.0 14.0 12.0 / POLYMW(OUTPUT=2, VELOCITY=1 TO N)

20.0 12.0 8.0 4.0 / POLYMW(OUTPUT=3, VELOCITY=1 TO N)

/

PLYMWINJ

2 / TABLE NUMBER

\--

\-- THROUGHPUT VALUES

\--

0.0 200.0 400.0 /

\--

\-- VELOCITY VALUES

\--

0.0 50.0 70.0 100.0 /

\--

\-- POLYMW VALUES

\--

20.0 19.0 18.0 16.0 / POLYMW(OUTPUT=1, VELOCITY=1 TO N)

20.0 16.0 14.0 12.0 / POLYMW(OUTPUT=2, VELOCITY=1 TO N)

20.0 12.0 8.0 4.0 / POLYMW(OUTPUT=3, VELOCITY=1 TO N)

/

As mentioned previously, the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) keyword requires that the keyword itself must be repeated for each table, as is shown in the above example.
