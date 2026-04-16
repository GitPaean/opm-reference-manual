### API -- Activate API Tracking

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on API tracking so that the various "oil types" are tracked in the model.

In many reservoirs the initial API gravity of oil varies with depth due to the heavy viscous fractions occupying the deepest part of the reservoir whilst the lighter more mobile fractions will occupy the upper part of the reservoir. As a reservoir is depleted the API gravity of oil in a cell will gradually change as the different fluids mix.

In OPM Flow it is possible to define different PVT regions in a reservoir, as in all finite difference formulated simulators, oil moving from one region to another will suddenly assume the properties of that region it has moved to. The fluid type tracking option allows the smooth change of PVT properties in a cell to be simulated by correlating PVT properties against the API gravity of oil.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE THE API TRACKING OPTION

\--

API

The above example switches on the API tracking facility.
