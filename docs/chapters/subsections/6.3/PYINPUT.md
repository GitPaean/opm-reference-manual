### PYINPUT -- Define the Start of a PYINPUT Section

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PYINPUT and PYEND keywords are a part of OPM Flow's Python scripting facility that processes standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck. The main purpose of the facility is to script the construction of the various keywords used by the simulator.

PYINPUT declares the start of a PYINPUT Definition Section on a single separate line, which is then followed by various standard Python commands, with one command per line. A PYINPUT Definition Section is terminated by a PYEND keyword on a separate single line.

There is no data required for this keyword and there is no terminating "/" for this keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the PYINPUT facility allows the user to implement complex functionality and the implementation is new for the 2020-04 release. Users should therefore use caution when using this facility.

| PYINPUT | PYINPUT declares the start of a PYINPUT Definition Section. This is then followed by any number Python commands. | Not Applicable |
| --- | --- | --- |
| 1-1 | PYTHON | A series of standard Python commands with one line per command. The active Parser objects are accessible as context.parser and the active Deck object is available as context.deck. |
| PYEND | PYEND declares the end of a PYINPUT Definition Section. The Python code between PYINPUT and PYEND is read and executed, and the simulator thenreturns to reading the normal simulation input deck. |  |
| Notes:<br>1)  There is no terminating "/" for this keyword, instead the PYEND keyword terminates the keyword. |  |  |

Table 6.113: PYINPUT Keyword Description

The PYINPUT/PYEND set of keywords is a result of combining two programming languages, the interactive Python interpreter and OPM Flow's source code language C++. When combining two languages one extends and embeds one into the other. When extending Python with C++ the functionality implemented in C++ is made available to Python applications, when embedding Python in C++ one can call Python functions from within C++. The PYINPUT/PYEND set of keywords is based on embedding a Python interpreter in the C++ OPM Flow simulator, but the Python code actually runs as part of the PYINPUT keyword is based on wrapping C++ objects in Python, that is extending Python.

The Python code in between the PYINPUT and PYEND keywords are imported during processing of the input deck and as such this implies that basic Python syntax checking is performed during reading the Python script.

See also the PYACTION keyword in the SCHEDULE section which is also part of OPM Flow's Python scripting facility, that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time.

#### Example

The example shows how to construct the DX variable in the GRID section and to add the resulting DX array as part of the input deck.

\--

\-- START OF PYINPUT SECTION

\--

PYINPUT

\#

\# Import Numpy Model

\#

import numpy as np

\#

\# Define DX and Get the Input Decks Unit Systems

\#

dx = np.array(\[100.0, 100.0, 100.0, 100.0\])

active_unit_system = context.deck.active_unit_system()

default_unit_system = context.deck.default_unit_system()

\#

\# Set DX in the Input Deck

\#

kw = context.DeckKeyword( context.parser\[\'DX\'\], dx, active_unit_system,

default_unit_system )

context.deck.add(kw)

PYEND

The active Parser objects is accessible as context.parser and the active Deck object is available as context.deck.
