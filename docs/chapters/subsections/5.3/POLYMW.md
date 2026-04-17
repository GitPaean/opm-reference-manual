### POLYMW -- Activate the Polymer Molecular Weight Transport Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates OPM Flow\'s Polymer Molecular Weight Transport option that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the POLYMER keyword in the RUNSPEC section is also activated. The keyword will also invoke data input file checking to ensure that all the required polymer phase input parameters are defined in the input deck.

In the PROPS section the PLYVMH, PLYMWINJ, SKPRWAT and SKPRPOLY keywords are used to define the additional polymer and water properties for the model. And the SPOLYMW keyword in the SOLUTION section may be used to set the initial molecular weight for each grid block in the model, in order to initialize the model. In the SCHEDULE section, the WPMITAB keyword should be used to associate a water injection well with the appropriate PLYMWINJ table. Finally, the WSKPTAB keyword, also in the SCHEDULE section, may be used to define the SKPRPOLY and SKPRWAT tables associated with the skin pressure for polymer and water injection. All the aforementioned keywords are OPM Flow specific keywords, that are not available in the commercial simulator.

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
