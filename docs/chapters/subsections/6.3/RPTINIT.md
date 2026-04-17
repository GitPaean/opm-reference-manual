### RPTINIT -- Define Output to the INIT File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the data in the GRID and EDIT sections that is to be written out to the INIT file (\*.INIT or \*.FINIT). The format consists of the keyword followed by a series of character strings that indicate the data to be written. In most cases the character string is the keyword used to load the data into the OPM Flow input deck, for example PORO for the porosity array in the GRID section. In addition, values either read or calculated by the simulator in the EDIT section can also be written to the INIT file. Again the keyword or property name is used as the mnemonic for the character string, for example the PORV, TRANX keywords etc. If the RPTINIT keyword is not used in the input deck then a default set of data array are written to the file, in this case the actual data written is dependent on the model's configuration and the options being used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
