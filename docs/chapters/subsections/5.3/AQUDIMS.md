### AQUDIMS -- Define Aquifer Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The AQUDIMS keyword defines the dimensions of the various aquifer property data. The data is normally entered on a single line and is terminated by a "/".

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXNAQN | A positive integer value that defines the AQUNUM keyword maximum number of lines associated with this keyword, that is the maximum number of numerical aquifers | 1 |
| 2 | MXNAQC | A positive integer value that defines the AQUCON keyword maximum number of lines of connection data associated with this keyword, that is the maximum number of lines of connection data for numerical aquifers. | 1 |
| 3 | NIFTBL | A positive integer value that defines the AQUTAB keyword maximum number of Carter-Tracy aquifer tables associated with this keyword. | 1 |
| 4 | NRIFTB | A positive integer value that defines the AQUTAB keyword maximum number of rows in the Carter-Tracy aquifer tables associated with this keyword.<br>NRIFTB must not be less than 36 in order to accommodate the default infinite acting Carter-Tracy aquifer influence function. | 36 |
| 5 | NANAQ | A positive integer value that defines the AQUFETP, AQUFLUX and AQUCT maximum number of analytical aquifers defined by these three keywords. | 1 |
| 6 | NCAMAX | A positive integer value that defines the maximum number of cells connected to an *analytical aquifer.* | 1 |
| 7 | MXNALI | A positive integer value that defines the maximum number of aquifer lists. | 0 |
| 8 | MXAAQL | A positive integer value that defines the maximum number of *analytical aquifers* in any single aquifer list as defined by (7). | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.5: AQUDIMS Keyword Description

#### Example

\--

\-- AQF AQF AQF AQF AQF AQF AQF AQF

\-- MXAQN MXNAQC NIFTBL NRIFTB NANAQU NCAMAX MXNALI MXAAQL

AQUDIMS

1\* 1\* 1\* 1\* 1\* 1\* 1\* 1\* /

The above example defines the default values for the AQUDIMS keyword.
