### SCDPTRAC -- Allocate Sea Water Tracer for Scale Deposition

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SCDPTRAC keyword is used to allocate an existing passive water tracer defined by the TRACER keyword in the PROPS section, to represent the sea water flowing into a well connection as a fraction of the total water influx. The keyword is used together with the SCDPTAB keyword in the SCHEDULE section to calculated the volume of scale deposited around the well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NAME | A three letter character string defining the tracer's name that has previously been defined by the TRACER keyword in the PROPS section | None |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 12.63: SCDPTRAC Keyword Description

#### Example

In the PROPS section define a tracer in the water phase, for example:

\--

\-- DEFINE TRACER NAMES

\--

\-- TRACER TRACER

\-- NAME PHASE

\-- \-\-\-\-\-- \-\-\-\-\--

TRACER

\'SEA\' \'WAT\' / SEA WATER TRACER

/

Then in the SCHEDULE section allocate the previously defined water tracer as a sea water tracer to be used with the scale deposition facility, that is:

\--

\-- ALLOCATE SEA WATER TRACER FOR SCALE DEPOSITION

\--

\-- TRACER

\-- NAME

\-- \-\-\-\-\--

SCDPTRAC

\'SEA\' / SEA WATER TRACER

/
