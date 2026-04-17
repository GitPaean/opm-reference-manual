### SKPRPOLY -- Polymer Molecular Weight Model Polymer Injection Skin Table

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, SKPRPOLY, describes the relationship of a water injection well\'s injected polymer skin pressure as a function of polymer throughput and water velocity, for the simulator\'s Polymer Molecular Weight Transport option. The table is a two dimensional table that relates the polymer throughput values and water velocity values to derive the resulting wellbore skin pressure of the injected polymer, which is then used to calculate the total wellbore skin pressure based on the polymer concentration.

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.

| 1-1 | SKPRPNUM | A positive integer value greater than zero and less than or equal to the NTSKPOLY variable, as defined on the PINTDIMS keyword in the RUNSPEC section, that defines the SKPRPOLY Polymer Molecular Weight Model polymer injection skin pressure table number. | None |
| --- | --- | --- | --- |
| 1-2 | POLCON | A real positive value that the defines the reference polymer concentration for the table. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 2-1 | THRUPUT | A real positive monotonically increasing vector, that defines the polymer throughput values. The first entry should be zero to define a no throughput data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet^3^/feet^2^ | m^3^/m^2^ | cm^3^/cm^2^ |  |
| 3-1 | VELOCITY | A real positive monotonically increasing vector, that defines the polymer velocity values. The first entry should be zero to define a no velocity data set, and each vector record should be on a separate line terminated by a "/". | None |
| feet/day | m/day | cm/hour |  |
| 4-1 | PRESS | A series of real positive vectors representing the wellbore skin pressure, for the given reference polymer concentration (POLCON), for all combinations of the polymer throughput values (THRUPUT) and velocity values (VELOCITY), organized as a series of vectors PRESS(THRUPUT, VELOCITY).<br>Thus, the first vector represents the wellbore skin pressure of the first THRUPUT value and each entry in the vector is the corresponding wellbore skin pressure of the associated VELOCITY vector. Each vector should be on a separate line and should be terminated by a "/".<br>Thus, if THRUPUT has three entries and VELOCITY has four, then there should be three vectors, with each vector containing four elements representing wellbore skin pressure values, as a function of THRUPUT and VELOCITY. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword should be terminated by a "/", but may be repeated up to NTSKPOLY times, as per the PINTDIMS keyword in the RUNSPEC section, to allow for the input of multiple tables. |  |  |  |

Table 8.156: SKPRPOLY Keyword Description

Unlike other PROPS section table keywords, that enable multiple tables following the keyword to be entered, the SKPRPOLY keyword requires that the keyword itself must be repeated for each table, as is shown in the example on the following page.

The WSKPTAB keyword in the SCHEDULE section may be used to assign the SKPRPOLY and SKPRWAT tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

See also the SKPRWAT, PLYMWINJ, and PLYVMH keywords, in the PROPS section, that are the additional property keywords required for the Polymer Molecular Weight Transport option. In addition, see also the WPMITAB keyword in the SCHEDULE section, that assigns the PLYMWINJ tables to the water injection wells.

Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.

#### Example

Given NTSKPOLY equals two on the PINTDIMS keyword in the RUNSPEC section, then two SKPRPOLY tables are required to be entered:

\--

\-- POLYMER MOLECULAR WEIGHT MODEL POLYMER INJECTION SKIN TABLE

\-- (OPM FLOW PROPS KEYWORD)

\--

SKPRPOLY

\-- TABLE POLYMER REF

\-- NO. CONCENTRATION

1 2.00 /

\--

\-- THROUGHPUT VALUES

\--

0.0 200.0 400.0 /

\--

\-- VELOCITY VALUES

\--

0.0 50.0 80.0 100.0 /

\--

\-- PRESS SKIN VALUES

\--

0.0 10.0 20.0 40.0 / PRESS(THRUPUT=1, VELOCITY=1 TO N)

0.0 50.0 100.0 200.0 / PRESS(THRUPUT=2, VELOCITY=1 TO N)

0.0 100.0 200.0 400.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)

/

SKPRPOLY

\-- TABLE POLYMER REF

\-- NO. CONCENTRATION

2 2.0 /

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

0.0 10.0 20.0 40.0 / PRESS(THRUPUT=1, VELOCITY=1 TO N)

0.0 50.0 100.0 200.0 / PRESS(THRUPUT=2, VELOCITY=1 TO N)

0.0 100.0 200.0 400.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)

/

As mentioned previously, the SKPRPOLY keyword requires that the keyword itself must be repeated for each table, as is shown in the above example.
