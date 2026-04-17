### SALINITY -- Define the Reservoir Salinity for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALINITY keyword defines a uniform salinity for all cells in the model. The keyword should only be used with OPM Flow's CO~2~-Brine model which is activated via the CO2STORE keyword in the RUNSPEC section. This keyword is a compositional keyword in the commercial simulator but has been implemented in OPM Flow's black-oil CO~2~-Brine model.

| No. | Name | Description | Default |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Field | Metric | Laboratory | 0 |
| 1 | SALINITY | A real positive value that defines the salinity for all grid blocks in the model for when the CO~2~-Brine model has been activated.<br>Note that the units for salinity are molality, that is gm-M/Kg, and therefore the units are defined as given below with the 10^-3^ prefix. |  |  |  |
| 10^-3^ x lb-M/lb | 10^-3^ x kg-M/kg | 10^-3^ x gm-M/gm |  |  |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |  |  |

Table 8.140: SALINITY Keyword Description

See also the CO2STORE keyword in the RUNSPEC section.

#### Example

The example sets the salt salinity for all cells in the model to 0.001 lb-M/Ib.

\--

\-- SET SALINITY FOR ALL CELLS (OPM FLOW KEYWORD)

\--

SALINITY

1.0 /

Note that units for salinity are to the 10^-3^, that is a value of 0.001 lb-M/lb should be entered as 1.0 (10^-3^ x lb-M/lb), as per the example.
