### NINEPOIN -- Activate the Nine-Point Discretization Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [NINEPOIN](#__RefHeading___Toc232496_718033703) keyword activates the Nine-Point Discretization formulation for the whole grid. If the keyword is absent from the run then the conventional standard five-point discretization formulation is used for the model. The nine-point scheme is based on adding additional non-neighbor connections between the diagonal neighbors in the areal plane, in order to reduce grid orientation effects[^1].

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

In none Local Grid Refinement runs the [NINENUM](#__RefHeading___Toc226526_718033703) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section may be use to optionally set parts of the grid to use nine-point discretization and the remaining regions to use the conventional standard five-point discretization formulation.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE NINE-POINT DISCRETIZATION OPTION

\--

NINEPOIN

The above example switches on the Nine-Point Discretization option for the whole grid.

[^1]: Yanosik, J. L. and McCracken, T. A. "A Nine-Point, Finite-Difference Reservoir Simulator for Realistic Prediction of Adverse Mobility Ratio Displacements," paper SPE 5734, Society of Petroleum Engineers Journal (1979) 19, No. 4, 253-262.
