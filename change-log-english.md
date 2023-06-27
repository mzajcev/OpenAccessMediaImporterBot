# Changelog:
## General changes and notes:
Update to Python 3 for the entire code.
In order for the functions of the bot, starting with download-metadata, to work, we had to first modify the test files dummy.py and pmc_doi.
dummy.py
For dummy.py, we tried different download files and fixed minor errors.
Added the links as a variable to the function, modifying the code to actually download the files instead of just yielding them. This may have worked in Python 2.
pmc_doi.py
Made several small adjustments to the relations between the functions in the files, adding arguments and often hiding optional parameters and arguments.
Adjusted the download structure, similar to the issue with dummy.py, where the content was only printed instead of being saved.
Added download statements using Carlin (external programming from WikiData).
Often, only the content was printed instead of being stored.
# File: oa-cache
1. Change type: Removed import statements
What?

- The following modules were removed: gobject, pygst, gst.
- Functions and classes that are no longer used were removed: setup_all, create_all.
2. Change type: Updated/Added import statements
What?

- make_datestring from helpers was imported instead of importing the entire helpers module. Functions and classes were updated to import from the corresponding modules.

- sqlalchemy was added to create and link the database with SQLite.

3. Change type: Prints
What?

- stderr.write was replaced with print.
4. Change type: 'convert-media'
What?

-materials were changed (no filter --> All).
- path was removed (added os.path in some places).
- Relative paths were added.
- Lines 167-186 were added to perform file conversion using ffmpeg instead of gobject.
- Link ffmpeg conversion to .ogg format with previous code.
5. Change type: 'find-media'
What?

- The first part of the code was commented out because the Elixir tool no longer works with Python 3. Therefore, all variables related to these functions had to be temporarily deactivated.
- skip was commented out as this function no longer worked with the existing code. This may be due to either Python 3 or Elixir.
- journal and article.get_by were removed, and contrib_authors was added as a separate variable.
- get_by is an Elixir variable and is deprecated.
- The code for category was initially removed because it caused problems with dependencies in the pipeline of the find-media function. Instead, the results are printed.

# File: oa-get
1. Change type: Added/Modified import statements
What?

- sqlalchemy, model, urllib3, filetype, importlib, requests
2. Change type: Added a database engine and a session
What?

- A database engine and a session were added, as well as database tables.
- SQLite is used via SQLAlchemy to store metadata according to the format in the dummy file.
3. Change type: Added the source path / Changed try-except
What?

- Relative paths that were temporarily changed to absolute paths as each one tried to solve file problems individually.
4. Change type: Updated a function check_mime_types
What?

- Rewriting the function to fix issues in the pipeline.
5. Change type: 'update-mimetypes'
What?

- The beginning of the if-else statement loops was deleted.
- .all() was placed inside the parentheses.
- Added a for-loop to check the file path.
6. Change type: 'download-media'
What?

- materials were added to the session and then printed to check if content is being added.

- The download-media function works when a PMC DOI is added to the pmc_doi.py file and also works with a list.

# -File: model.py
1. Change type: Added/Modified import statements
What?

- sqlalchemy, importlib, sys
2. Change type: Redefining the 'set_source' function
What?

- Instead of using SQLite, importlib is used to define the source_module.
3. Change type: Defining new variables
What?

- engine --> to declare the SQL environment.
- Session --> to define a session in the bot workflow.
4. Change type: Changes in the 'Journal' class
What?

- The object was changed to Base instead of Entity due to issues with calling the variable before the change.
- Adding tablename because the data was not stored in the correct format in the SQLite server.
- Therefore, the variables in the class also need to be changed. Instead of using Field() for the title, Column() is used as an update from Python 2.
- Relations of the fields and keys were assigned for articles.
5. Change type: Adding the variable 'article_category'
What?

- This is where an association table is defined with the name 'article_category'.
- This allows articles and categories to be connected through the linking table.
- A function in oa-get or oa-cache asked for this table even though it didn't exist before. When switching to Python 3, some variables may have been lost, and then they had to be manually added through trial and error by examining 
- the error messages for the functions download-media, download-metadata, find-media, and convert-media.
6. Change type: Changes in the 'Category', 'Article', & 'SupplementaryMaterial' classes
What?

- Again, instead of Entity, Base is used as an adjustment to a new import.
# File: config.py
Update to Python 3

1. Change type: Path change
What?

- The original path did not work on personal laptops, so each person had to manually change it.
- Later, a change with relative paths was added.
- Adjustment of the User Config and expansion with specific local variables.
2. Change type: Added to the 'database_path' function
What?

- SQLite is required for database_path so that the respective command can create the individual databases.

# General Changes and Notes:
In order for the functions of the bot, starting with download-metadata, to work, we had to first modify the test files dummy.py and pmc_doi.
### dummy.py
For dummy.py, we tried different download files and fixed minor errors.
We added the links as a variable to the function and modified the code so that it actually downloads the files instead of just yielding them. This may have worked in Python 2.
### pmc_doi.py
There were many small adjustments to the relationships between the functions in the files. Arguments were added, and optional parameters and arguments were often hidden.
The download structure was adjusted, similar to the problem with dummy.py, where the content was only being yielded instead of being stored.
Download statements were added using Carlin (external programming of WikiData).
Often, only the content was printed instead of being saved.