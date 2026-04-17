### DATUMRX -- Define Datum Depths for the FIP Allocated Regions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DATUMRX keyword defines the datum depth for each fluid in-place family region defined by the FIP keyword. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth within a given FIP region. The FIP keyword in the REGIONS section allows one to define additional sets of fluid in-place regions to the standard FIPNUM keyword. For example, one could use FIPNUM to define the reservoir layers as fluid in-place regions and the FIP keyword to define the fluid in-place region for fault blocks.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | FIPNAME | A character string of up to five characters in length that defines the FIP family name for which the datum depth data is being defined.<br>The default value of 1\* will set DATUMR to the standard FIPNUM region numbers. | 1\* |
| 2 | DATUMR | DATUMR is a vector of positive values that defines the datum depth for each fluid in-place family region. There must be one entry for each region in the FIP family name.<br>A maximum of NTFIP values, as declared by the REGDIMS keyword in the RUNSPEC section, may be entered for each FIPNAME entry. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is followed any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 10.13: DATUMR Keyword Description

See also the FIP keyword in the REGIONS section to define FIP family regions, and the DATUM and DATUMR keywords in the SOLUTION section that also define the datum depth for the model.

#### Example

\--

\-- FIP DATUM

\-- NAME DEPTH

DATUMRX

\'FLTBL\' 5000.0 5000.0 5000.0 5000.0 / DATUM DEPTH FOR REPORTING

\'LICBL\' 5000.0 5050.0 / DATUM DEPTH FOR REPORTING

/

The above example defines the datum depth for two FIP families, FLTBL and LICBL, with the datum set to a constant 5000.0 psia for FLTBL family and different values for each of the regions in the LICBL family of regions.
