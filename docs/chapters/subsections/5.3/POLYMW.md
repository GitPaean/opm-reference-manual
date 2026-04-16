### POLYMW -- Activate the Polymer Molecular Weight Transport Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates OPM Flow\'s Polymer Molecular Weight Transport option that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is also activated. The keyword will also invoke data input file checking to ensure that all the required polymer phase input parameters are defined in the input deck.

In the [PROPS](#__RefHeading___Toc39329_784232322) section the [PLYVMH](#__RefHeading___Toc473331_21243525712), [PLYMWINJ](#__RefHeading___Toc473331_2124352571), [SKPRWAT](#__RefHeading___Toc473331_212435257111) and [SKPRPOLY](#__RefHeading___Toc473331_21243525711) keywords are used to define the additional polymer and water properties for the model. And the [SPOLYMW](#__RefHeading___Toc428289_1116899071) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section may be used to set the initial molecular weight for each grid block in the model, in order to initialize the model. In the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, the [WPMITAB](#__RefHeading___Toc121649_24125861601) keyword should be used to associate a water injection well with the appropriate [PLYMWINJ](#__RefHeading___Toc473331_2124352571) table. Finally, the [WSKPTAB](#__RefHeading___Toc121649_241258616011) keyword, also in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, may be used to define the [SKPRPOLY](#__RefHeading___Toc473331_21243525711) and [SKPRWAT](#__RefHeading___Toc473331_212435257111) tables associated with the skin pressure for polymer and water injection. All the aforementioned keywords are OPM Flow specific keywords, that are not available in the commercial simulator.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE POLYMER PHASE IN THE MODEL

\--

POLYMER

\--

\-- ACTIVATE THE POLYMER MOLECULAR WEIGHT TRANSPORT OPTION

\--

POLYMW

The above example declares that the polymer phase is present, and that the simulator\'s Polymer Molecular Weight Transport option should be used instead of the standard polymer model.
