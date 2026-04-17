### SMRYDIMS -- Define Maximum Number of Summary Vectors to be Written

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SMRYDIMS keyword defines the maximum number of summary vectors to be written out to the SUMMARY file (\*.SUMMARY).

OPM Flow uses dynamic memory allocation and therefore the keyword has no effect and is ignored by the simulator, but is documented here for completeness.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NSUMMX | A positive integer that defines the maximum number of summary vectors to be written out to the SUMMARY file (\*.SUMMARY). | 10000 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.42: SMRYDIMS Keyword Description

#### Example

\--

\-- SET THE MAXIMUM NUMBER OF SUMMARY VECTORS THAT CAN BE WRITTEN OUT

\--

SMRYDIMS

10000 /

The above example sets maximum number of summary vectors that can be written out to the SUMMARY file to the default value of 10,000; however, this has no effect in OPM Flow input decks.
