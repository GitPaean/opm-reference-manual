### WSEGDIMS -- Define Multi-Segment Well Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSEGSDIMS keyword defines the multi-segment well dimensions for the multi-segment well model and the keyword is obligatory if multi-segment wells are being employed in the model.

| 1 | MXWELS | A positive integer defining the maximum number of multi-segment wells for this model. | 0 |
| --- | --- | --- | --- |
| 2 | MXSEGS | A positive integer defining the maximum number of segments per well for this model. | 1 |
| 3 | MXBRAN | A positive integer defining the maximum number of branches per multi-segment well, including the main branch groups for this model. | 1 |
| 4 | MXLINKS | A positive integer defining the maximum number of segment links per multi-segment well.<br>The simulator does not currently support multi-segment chord links, and therefore this parameter is ignored. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.59: WSEGDIMS Keyword Description

#### Example

\--

\-- WELL WELL BRANCH SEGMENT

\-- MXWELS MXSEGS MXBRAN MXLINKS

WSEGDIMS

5 100 10 10 /

The above example defines the maximum number of multi-segment wells to be five with up to 100 segments per multi-segment well, a maximum number of 10 branches per multi-segment well, and up to 10 segment links per multi-segment well.
