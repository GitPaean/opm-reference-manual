### GMWSET -- Export Well Status Vectors by Group to File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword is similar to the ALL keyword in the SUMMARY section, in that it results in a group of summary variables to be written out to the SUMMARY file. In this case the keyword activates the writing out of a set of data vectors that give the production and injections status of all the wells in the named groups, as well as the number of wells in the drilling queue and the number of workover events occurring within a time step for the requested groups. Both instantaneous and cumulative well counts and events for the groups are written out as tabulated in .

Note that GMWSET should be followed by a list of group names enclosed in quotes and therefore a terminating "/" is required to end the list of groups. A blank list requests output for all groups.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| Number of abandoned injection wells | MWIA | FMWIA | GMWIA |  |
| --- | --- | --- | --- | --- |
| Number of abandoned production wells | MWPA | FMWPA | GMWPA |  |
| Number of drilling events in total | MWDT | FMWDT | GMWDT |  |
| Number of drilling events this timestep | MWDR | FMWDR | GMWDR |  |
| Number of injection wells currently flowing | MWIN | FMWIN | GMWIN |  |
| Number of injectors on group control | MWIG | FMWIG | GMWIG |  |
| Number of injectors on own reservoir volume rate limit control | MWIV | FMWIV | GMWIV |  |
| Number of injectors on own surface rate limit control | MWIS | FMWIS | GMWIS |  |
| Number of injectors on pressure control | MWIP | FMWIP | GMWIP |  |
| Number of producers controlled by own oil rate limit | MWPO | FMWPO | GMWPO |  |
| Number of producers on group control | MWPG | FMWPG | GMWPG |  |
| Number of producers on own reservoir volume rate limit control | MWPV | FMWPV | GMWPV |  |
| Number of producers on own surface rate limit control | MWPS | FMWPS | GMWPS |  |
| Number of producers on pressure control | MWPP | FMWPP | GMWPP |  |
| Number of producers using artificial lift (with ALQ \> 0.0) | MWPL | FMWPL | GMWPL |  |
| Number of production wells currently flowing | MWPR | FMWPR | GMWPR |  |
| Number of unused injection wells | MWIU | FMWIU | GMWIU |  |
| Number of unused production wells | MWPU | FMWPU | GMWPU |  |
| Number of workover events in total | MWWT | FMWWT | GMWWT |  |
| Number of workover events this time step. | MWWO | FMWWO | GMWWO |  |
| Total number of injection wells | MWIT | FMWIT | GMWIT |  |
| Total number of production wells | MWPT | FMWPT | GMWPT |  |
| Notes:<br>3)  Cells colored in gray with a mnemonic indicate that the summary variable is not available in OPM Flow.<br>4)  Cells colored in gray with no mnemonic indicate that the summary variable is not available for this combination.<br>5)  Cells colored orange show combinations that are not available in OPM Flow because the underlying feature is not available. |  |  |  |  |

Table 11.29: GMWSET - Standard Field and Group Well Status Summary Variables

See also the FMWSET keyword in the SUMMARY schedule that has similar functionality but at the field level.

#### Examples

The first example below exports all the group standard well status variables to the SUMMARY file.

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT WELL STATUS VECTORS FOR NAMED GROUPS TO FILE

\--

GMWSET

/

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE

The second example exports all the group standard well status variables for just the PLAT1 and PLT2 groups only to the SUMMARY file.

\--

\-- EXPORT WELL STATUS VECTORS FOR NAMED GROUPS TO FILE

\--

GMWSET

'PLAT1' 'PLAT2'

/

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE
