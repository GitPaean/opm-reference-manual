### REGDIMS -- Define the Maximum Number of Regions for a Region Array

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The REGDIMS keyword defines the maximum number of regions for various region arrays used in the model. Note that the maximum number of FIPNUM regions can be defined both on this keyword and the TABDIMS keyword, if it set in both locations the maximum value is used. The reason for this type of inconsistency is due to the commercial simulator evolving with time as new features were added, but at the same time having to maintain backward input deck compatibility.

| 1 | NTFIP | A positive integer defining the maximum number of regions in the FIPNUM region array. If additional sets of fluid in-place regions have been defined, as per the FIPxxxxx series of fluid in-place region keywords, then NTFIP should be set to the maximum number of regions in either the FIPNUM or FIPxxxxx associated arrays.<br>Thus, if the maximum number of regions in the FIPNUM array is 12, and the maximum value in the FIPxxxxx series of arrays is 20, then 20 should be entered for NTFIP.<br>Note that this parameter may also be set on the TABDIMS keyword as well. If NTFIP is set in both places, then the maximum value is used. | 1 |
| --- | --- | --- | --- |
| 2 | NMFIPR | A positive integer defining the total maximum number of fluid in-place regions.<br>The number of FIPNUM regions are defined by NTFIP. However, if additional sets of fluid in-place regions are required, as per the FIPxxxxx series of fluid in-place region keywords, then these are to be defined here by adding the number of FIPxxxxx arrays to the value NTFIP.<br>So for example, if NTFIP equals five and the number of distinct FIPxxxxx regions is three, then the value to enter for NMFIPR is eight. | 1 |
| 3 | NRFREG | A positive integer defining the maximum number of independent reservoir regions in the ISOLNUM region array. | 0 |
| 4 | MXNFLX | A positive integer defining the maximum number of flux regions in the FLUXNUM region array. MXNFLX can also be defined on the TABDIMS keywords as well. If MXNFLX is defined both here and on the TABDIMS keyword then the maximum value of the two is used. | 0 |
| 5 | NUSREG | A positive integer defining the maximum user defined regions in a commercial simulator's compositional model. This parameter is included for compatibility and should be defaulted as it is not used in OPM Flow. | 0 |
| 6 | NTCREG | A positive integer defining the maximum number of regions in the COALNUM region array. This parameter is included for compatibility and should be defaulted as it is not used in OPM Flow. | 1 |
| 7 | NOPREG | A positive integer defining the maximum number of regions in the OPERNUM region array. | 0 |
| 8 | NWKDREG | A positive integer defining the maximum number of real double-precision work arrays for use with the OPERATE and OPERATER keywords. This parameter is included for compatibility and should be defaulted as it is not used in OPM Flow. | 0 |
| 9 | NWKIREG | A positive integer defining the maximum number of integer work arrays for use with the OPERATE and OPERATER keywords. This parameter is included for compatibility and should be defaulted as it is not used in OPM Flow. | 0 |
| 10 | NPLMIX | A positive integer defining the maximum number of regions in the PLMIXNUM region array. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.37: REGDIMS Keyword Description

#### Example

\--

\-- MAX TOTAL INDEP FLUX TRACK CBM OPERN WORK WORK POLY

\-- FIPNUM REGNS REGNS REGNS REGNS REGNS REGNS REAL INTG REGNS

REGDIMS

9 12 1\* 1\* 1\* 1\* 1\* 1\* 1\* 1\* /

The above example defines the number of FIPNUM regions to be nine and the number of FIPxxx type of regions to be three (12 -- 9), the rest of the region sizes are set to the default values.
