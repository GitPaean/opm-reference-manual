### INSPEC -- Activate the INSPEC File Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the writing of the INIT Index file that specifies and defines the format and data type written to the \*.INIT data file. The \*.INIT data file contains the static data specified in the GRID, PROPS and REGIONS sections. For example, the PORO, PERM and NTG arrays from the GRID section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The INIT Index file can either be written out in formatted form as ASCII i.e. text files, if the FMTOUT keyword has been activated (\*.FINSPEC), or binary format (\*.INSPEC) if the FMTOUT keyword has not been activated. If the INIT keyword in the GRID section has been used to switch on the writing of the \*. INIT data file then a binary INIT Index file is automatically written out as well, unless the NOINSPEC keyword in the RUNSPEC section has been used to switch off the writing of the INIT Index file.

Note that most post-processing software require the \*.INSPEC file to load the \*.INIT data set, although OPM ResInsight does not require this file to be able to load the \*.INIT data file.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE WRITING THE INIT INDEX FILE FOR POST-PROCESSING

\--

INSPEC

The above example switches on the writing of the INIT Index file for post-processing in ResInsight.
