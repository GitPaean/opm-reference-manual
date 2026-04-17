### FMTOUT -- Activate The Format Output File Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the Format Output Files option for all output files. Similar to the commercial simulator, OPM Flow has various options for reading various input files and writing the resulting OPM Flow output files as described in .

| Input | FMTIN | A character string that defines the input files to be formatted as ASCII i.e. text files, as oppose to binary files. The input deck file is always of this type.<br>The option relates to the OPM Flow derived files that used as input, for for example when restarting from another case.<br>If the keyword is omitted then the default is for binary file input. | \*.FEGRID<br>\*.FINSPEC<br>\*.FINIT<br>\*.FRSSPEC<br>\*.FUNRST<br>\*.FSMSPEC<br>\*.FUNSMRY |
| --- | --- | --- | --- |
| MULTIN | A character string that defines the input files to be non-unified multiple files, as opposed to unified files. In this case, one file is read in per reporting time step, as opposed to all time steps reports being read from one file.<br>I*f the keyword is omitted then the default is for *one file per reporting time step. | \*.RSSPEC<br>\*.X0001<br>\*.SMSPEC<br>\*.S0001 |  |
| UNIFIN | A character string that defines the input files to be unified files, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. For this option a single summary file and a single restart file will be read.<br>I*f the keyword is omitted then the default is for *one file per reporting time step*.* | \*.RSSPEC<br>\*.UNRST<br>\*.SMSPEC<br>\*.UNSMRY |  |
| Output | FMTOUT | A character string that sets all output files to be formatted as ASCII i.e. text files, as opposed to binary files. The \*.PRT, \*.LOG and \*.DBG files are always of this type.<br>The option relates to the OPM Flow output files only. In this case the files will be portable across operating systems, but will also be very large in terms of hard disk space. For this reason it is recommend that the default option is used so that binary files are outputted.<br>If the keyword is omitted then the default is for binary file input. | \*.FEGRID<br>\*.FINSPEC<br>\*.FINIT<br>\*.FRSSPEC<br>\*.FUNRST<br>\*.FSMSPEC<br>\*.FUNSMRY |
| MULTOUT | A character string that defines the output files to be non-unified multiple files, as opposed to unified files. In this case, one file is written for each reporting time step, as opposed to all time steps reports being written in one file.<br>I*f the keyword is omitted then the default is for *one file per reporting time step. | \*.RSSPEC<br>\*.X0001<br>\*.SMSPEC<br>\*.S0001 |  |
| UNIFOUT | A character string that defines the output files to be unified files, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single summary file and a single restart file will be generated, as opposed to one file per report time step.<br>I*f the keyword is omitted then the default is for *one file per reporting time step. | \*.RSSPEC<br>\*.UNRST<br>\*.SMSPEC<br>\*.UNSMRY |  |
| Notes:<br>1)  A binary file is computer-readable but not human-readable. All executable programs are stored in binary files, as are most numeric data files. In contrast, text files are stored in a form (usually ASCII) that is human-readable.<br>2)  For unified files if the run terminates unexpectedly, or there is sufficient disk space, then the last report output is not stored. Their main advantage is that if a number of simulations reside in one directory, their output is organized. There is no limit on the number of reporting steps that a unified file can store. |  |  |  |

Table 5.15: FMOUT Keyword Description

There is no data required for this keyword.

See also [OPM FLOW OUTPUT FILE FORMATS](#anchor-2) for a more detailed description of the various file types (ASCII or binary) and file structure formats (unified or non-unified formats).

#### Example

\--

\-- SWITCH ON THE FORMAT OUTPUT FILES OPTION

\--

FMTOUT

The above example switches on the format output file option.
