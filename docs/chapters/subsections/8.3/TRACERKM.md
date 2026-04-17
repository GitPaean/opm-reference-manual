### TRACERKM -- Multi-Partitioned Tracer Option K(P) Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, TRACERKM, defines the Multi-Partitioned Tracer option K(P) tables, for when the Partitioned Tracer option has been activate with the PARTTRAC keyword in the RUNSPEC section, and the SOLPHASE parameter on the TRACER keyword in the PROPS section has been set to MULT to activate the Multi-Partitioned Tracer option. Multi-partitioned tracers can partition into any number of phases (oil, water, gas etc.) and have adsorption, decay and diffusion parameters specific to each phase; whereas the standard partitioned tracers only have a "free" and "solution" phases. For the TRACERKM keyword the K(P) tables relate the ratio of the reference phase to the other phases versus pressure. So for example, given a multi-partitioned tracer in oil, water and gas, with the water phase acting as the reference phase, then TRACERKM would consist of columnar vectors of:

Where:

= multi-partitioned oil-water K(P)

= multi-partitioned gas-water K(P)

= oil concentration

= gas concentration

= water concentration

See also the TRACERKP keyword in the PROPS section that provides similar data for standard partitioned tracers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
