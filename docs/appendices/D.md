A.

B.  # PYTHON INTERFACE TO OPM FLOW

A.  1.  ## Introduction

Some of the C++ code in OPM Flow has been "wrapped" in Python which means that one can invoke the simulator's C++ code from one's own Python programs. At the moment the wrappers for the input layer and the code for working with the result files is quite complete and usable. For a python class documentation and for further documentation and examples, please refer to the [OPM Online Python Documentation](https://opm.github.io/opm-python-documentation/index.html). There is also the option to interact with running simulations from within Python using the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword.

The goal is for the Python code to be structured like a native Python API, but some design decisions are certainly influenced by the underlying C++ implementation, and to get a deeper understanding of what is possible and how to achieve specialized tasks one might need to consult the simulator's C++ code.

A.  1.  ## Working with the Input Deck

The reading of the input deck in OPM Flow is a two step process, first a data structure called a *"Deck"* is created - the* "Deck"* is essentially a collection of keywords where all elements have been converted to the correct type and default values have been injected into the keyword. The *"Deck"* is a quite low level data structure, and the actual simulation is based on higher level data structures where the origin in "keywords" from a \*.DATA file is no longer so apparent. The most notable high level objects are the *"EclipseState"* and *"Schedule"* classes. Large parts of this functionality is available from Python.

A.  1.  1.  ### The Parser Object

The initial building block in the parsing process is the *"Parser"* object which knows how to interpret the input keywords and create data structures. Virtually all scripts working with the input files will start with creating a Parser object:

#!/usr/bin/env python3

from opm.io.parser import Parser

\# Create a parser object which can be used to parse a string or input files

parser = Parser()

In most cases one will just create a default parser object and be done with it, but it is possible to both add your own keyword definitions to the parser and alternatively create a custom parser which only accepts a subset of keywords. These features will be demonstrated briefly in section [[Special Parsing](#anchor-4)](#4.2.4.Special Parsing|outline).

A.  1.  1.  ### Loading an Input Deck

The *"Deck" *data structure is essentially a list of keywords which have been loaded as *"DeckKeyword"* instances. The Deck can either be loaded from an input data file or from a string. The following example shows how to load two [SCHEDULE](#__RefHeading___Toc43945_784232322) section keywords: [WELSPECS](#__RefHeading___Toc268463_1366622701) and [COMPDAT](#__RefHeading___Toc97651_3261743917):

#!/usr/bin/env python3

from opm.io.parser import Parser

deck_string = \"\"\"

WELSPECS

\'W1\' \'G1\' 19 4 1\* WATER 1\* 1\* SHUT 1\* 1\* 1\* /

/

COMPDAT

\'W1\' 11 3 1 5 OPEN 1\* 1\* 0.216 1\* 0 1\* Z 1\* /

/

\"\"\"

parser = Parser()

deck = parser.parseString( deck_string )

After running this small script the deck variable will contain the two keywords [WELSPECS](#__RefHeading___Toc268463_1366622701) and [COMPDAT](#__RefHeading___Toc97651_3261743917). For these keywords the \'\*\' have been replaced with the correct default value and the items have been converted to the correct type. In addition, all numerical values have been converted to SI units, more about units can be found in section** **[*[Units](#anchor-6)*](#4.2.3.Units|outline). Alternatively you can use the Parser.parseFile() method to parse an entire input file. In this case [INCLUDE](#__RefHeading___Toc55749_2479612490) and [IMPORT](#__RefHeading___Toc539691_2135714711) keywords will be resolved and everything will be coalesced into one large *"Deck*Keyword" data structure:

#!/usr/bin/env python3

import os.path

import sys

from opm.io.parser import Parser

data_file = sys.argv\[1\]

print(f\"Loading deck from {data_file}\")

parser = Parser()

deck = parser.parseFile( data_file )

The code above loads a \*.DATA file given by calling the Python script. For example, if the name of the input deck, that may contain a complete input deck or just a selection of keywords, is called NORNE.DATA, and the name of the above script is LoadDeck.py, then:

python LoadDeck NORNE.DATA

would load the NORNE.DATA into the simulator.

A.  1.  1.  ### Units

Internally in OPM Flow all quantities are managed as SI units, whereas input decks use the unit systems [METRIC](#__RefHeading___Toc70639_2267116897), [FIELD](#__RefHeading___Toc71850_2267116897), or [LAB](#__RefHeading___Toc72458_2267116897) (laboratory). The [METRIC](#__RefHeading___Toc70639_2267116897) unit system is comparable to SI units, the most notable difference is that time is expressed in days instead of seconds, the [FIELD](#__RefHeading___Toc71850_2267116897) unit system is based on historical units like barrels of oil (stb) and feet for length.

The important point is that when you access the elements in the Deck the values you will get are in SI units, whereas the input you provided has been in one of other set of units. Consider the example:

#!/usr/bin/env python3

from opm.io.parser import Parser

deck_string = \"\"\"

WCONPROD

\'W1\' \'OPEN\' \'ORAT\' 86400 /

/

\"\"\"

parser = Parser()

deck = parser.parseString( deck_string )

kw = deck\[0\]

record0 = kw\[0\]

orat = record0\[\"ORAT\"\].value

well = record0\[\"WELL\"\].value

print(\"==\> The Oil rate in well:{} is {} m3/s\".format(orat, well))

When this script is run it will print:

==\> The Oil rate in well:W1 is 1.0 m3/s

because the input value of 86,400 m3/day is internally converted to 1.0 m3/second.

The default input unit system is [METRIC](#__RefHeading___Toc70639_2267116897), that means that if the input is to be interpreted in either [FIELD](#__RefHeading___Toc71850_2267116897) or [LAB](#__RefHeading___Toc72458_2267116897) units, then one needs to add a keyword to declare the units before entering the data. Thus, to interpret the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword's oil rate as stb/d in the previous example, the [FIELD](#__RefHeading___Toc71850_2267116897) keyword needs to be added to the example, that is:

#!/usr/bin/env python3

from opm.io.parser import Parser

deck_string = \"\"\"

[FIELD](#__RefHeading___Toc71850_2267116897)

[WCONPROD](#__RefHeading___Toc146754_4203985108)

\'W1\' \'OPEN\' \'ORAT\' 86400 /

/

\"\"\"

A.  1.  1.  ### Accessing the Input Deck

After you have loaded a Deck you can query it with normal Python functions:

\# Check if deck has keyword:

if \"GRID\" in deck:

print(\"Deck contains \'GRID\' keyword\")

else

print(\"Deck does not have \'GRID\' keyword\")

\# Loop through all the keywords:

for kw in deck:

print(\"kw: {}\".format(kw.name)

To get a keyword from the deck you can access it with index, name, or a combination of name and occurrence index:

\# Get keyword 10

kw10 = deck\[10\]

\# Get the last DATES keyword

last_dates = deck\[\"DATES\"\]

\# Get the third WELSPECS keyword

welspecs3 = deck\[(\"WELSPECS\", 3)\]

A deck keyword is composed of *"records"*, which are again composed of *"items"*. The example below shows how one can iterate through the wells in a [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword:

kw = deck\[\"WELSPECS\"\]

print(f\"Keyword has {len(kw)} records\")

for record in kw:

well = record\[\"WELL\"\].get_str()

group = record\[1\].get_str()

print(f\"Well {num}: {well} is part of group{group})

A.  1.  1.  ### Special Parsing

The keywords that OPM Flow recognizes are configured via JSON files which are embedded in the source distribution. The JSON keywords for the simulator are in the following public GitHub repository:

[*https://github.com/OPM/opm-common/tree/master/opm/input/eclipse/share/keywords*](https://github.com/OPM/opm-common/tree/master/opm/input/eclipse/share/keywords)

By default the Parser class will recognize all the keywords which are known to OPM Flow, but one can create your own custom parser with only a subset of keywords:

from opm.io.parser import Builtin

\# Create a special parser which only recognizes the corner point grid \# keywords

parser = Parser(add_default = False)

builtin = Builtin()

parser.add_keyword( builtin.COORD )

parser.add_keyword( builtin.ZCORN )

parser.add_keyword( builtin.ACTNUM )

The opposite is also possible, here is how one can add a special keyword GCLOSE which could be used to close all the wells in the group:

\# Create a fictitious home mode keyword GCLOSE:

GCLOSE = {\"name\" : \"GCLOSE\",

\"sections\" : \[\"SCHEDULE\"\],

\"items\" : \[

{\"name\" : \"GROUP\", \"value_type\" : \"STRING\"}

\]}

parser = Parser()

\# Add the keyword description via a JSON string

parser.add_keyword(json.dumps(GCLOSE))

By default the parser used in OPM Flow is quite strict - a tad stricter than the one used by the commercial simulator. However, one can configure how the parser should react to certain error conditions. By default the parser will fail with an exception if an [INCLUDE](#__RefHeading___Toc55749_2479612490) file is not found, but one can for instance change this behavior to ignore that error condition, for example:

parse_context = ParseContext(\[(\'PARSE_MISSING_INCLUDE\',

opm.io.action.ignore)\])

parser = Parser()

deck = parser.parseFile(self.norne_fname, parse_context)

A.  1.  1.  ### Creating EclipseState and Grid Objects

The *"Deck"* is a quite raw structure and not very user friendly. Before actually used in the simulator the properties from the *"Deck"* are coalesced to a form more easily usable format. Consider, for example the [PORO](#__RefHeading___Toc45797_719036256) array configured below where the configuration is given in three steps:

\-- GRID Dimensions 10 x 10 x 3

DIMENS

10 10 3 /

\--

\-- Set A Global Value 0.10 For All Of The Grid

\--

PORO

300\*0.10 /

\--

\-- Set A Value Of 0.15 For All The Cells In The Middle Layer

\--

BOX

1 10 1 10 2 2 /

PORO

100\*0.15 /

ENDBOX

\--

\-- Scale The Bottom Layer By A Factor OF Two

\--

MULTIPLY

PORO 2 1 10 1 10 3 3 /

/

In the deck representation this will be a collection of five different keywords: {\"PORO\", \"BOX\", \"PORO\", \"ENDBOX\", \"MULTIPLY\"}, whereas in the *"EclipseState"* this will be one property \"PORO\" where all the modifications have been completed. In addition to the grid properties like \"PERMX\" and \"PORO\" the *"EclipseState"* object contains numerous other objects like the fault properties, PVT tables, and more.

#!/usr/bin/env python3

import syshe

form opm.io.parser import Parser

from opm.io.ecl_state import EclipseState

parser = Parser()

data_file = sys.argv\[1\]

deck = parser.parseFile( data_file )

es = EclipseState( deck )

\#

\# Get the FieldPropsManager from the EclipseState. The FieldPropsManager

\# is then used to query and look up grid properties like PERMX and PORO.

\# Observe that the properties you get from the FieldPropsManager only have

\# the active cells only.

\#

fp = es.field_props()

poro = fp\[\"PORO\"\]

satnum = fp\[\"SATNUM\"\]

\#

\# Get the input grid from the EclipseState:

\#

grid = es.grid()

\# Get a manager for all the tables

tables = es.tables()

A.  1.  1.  ### Creating a Schedule

The Schedule object contains all the dynamic information in the model, in particular that includes all information about wells and groups. The Schedule object is constructed from the *"Deck"* and the "*EclipseState"* objects.:

#!/usr/bin/env python3

import sys

from opm.io.parser import Parser

from opm.io.ecl_state import EclipseState

parser = Parser()

data_file = sys.argv\[1\]

deck = parser.parseFile( data_file )

es = EclipseState( deck )

schedule = Schedule(deck, es)

print(f\"Schedule file has {len(schedule)} report steps\")\'

print(\"List of wells\")

for well in schedule.well_names():

print(well)

The example above prints the number of report time steps and all the well names in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

A.  1.  ## Working with the Result Files

In addition to the functionality to load and inspect the input deck, OPM Flow also has a Python interface to load and inspect the various result files, [SUMMARY](#__RefHeading___Toc43949_784232322) and [RESTART](#__RefHeading___Toc135629_1317547213) files. There is also some functionality to create files with the correct formatting.

A.  1.  1.  ### Loading a Grid File

Using the class *"EclipseGrid"* one can load a grid representation from a \*.EGRID file on disk:

#!/usr/bin/env python3

import sys

from opm.io.ecl import EGrid

grid_file = sys.argv\[1\]

grid = EGrid(grid_file)

The return value from *"EclipseState.ecl_grid()*" is also of this type.

A.  1.  1.  ### Loading a Summary Case of Results

Using the class *"ESMry"* one can load the Extended [SUMMARY](#__RefHeading___Toc43949_784232322) file for a simulations that contains all the [SUMMARY](#__RefHeading___Toc43949_784232322) vectors.

#!/usr/bin/env python3

import sys

from opm.io.ecl import ESMry

case = sys.argv\[1\]

summary = Esmry(case)

A.  1.  1.  ### Loading a Restart File

Finally, one load the solution arrays stored in the \*.RESTART file using the Erst class, as shown below.

#!/usr/bin/env python

import sys

from opm.io.ecl import ERst

rst_file = sys.argv\[1\]

rst = Erst(rst_file)

Note that a restart file can be large, so care must be taken on how these type of files are loaded into Python.
