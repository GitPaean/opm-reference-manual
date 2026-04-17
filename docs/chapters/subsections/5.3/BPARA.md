### BPARA -- Activate Block Parallel License

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The BPARA keyword activates the block parallel license in the commercial simulator. There is no data required for this keyword; however the keyword should be followed by the PARALLEL keyword in the RUNSPEC section, as illustrated in the example below.

There is no data required for this keyword and there is no terminating "/" for this keyword.

OPM Flow is an open source project and therefore there is no license management of the various implemented options or the number of cores/threads that can be utilized; hence this keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to run OPM Flow in parallel mode.

#### Example

\--

\-- ACTIVATE BLOCK PARALLEL LICENSE

\--

BPARA

\--

\-- PARALLEL MULTI-CORE OPTIONS

\-- NDMAIN MACHINE TYPE

PARALLEL

8 DISTRIBUTED /

The above example sets the number of domains (or processors) to eight and for the simulation to run in block parallel mode. This has no effect in OPM Flow input decks.
