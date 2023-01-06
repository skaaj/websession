## websession, _a web browser session launcher_

Session in that context mostly refers to "collection of URLs related to an activity". For example, working on some project might involve navigating to its repository, some documentations, a CI tool and so on. `websession` is then a tool that allows one to open all of those websites in a single command instead of having to start them one by one.

### Usage
The project is still in an exploration phase and for the time being only basics commands are implemented. Also, only Firefox is implemented yet.

* `websession start <name>`  
Open a new window with all the tabs of session <name>

* `websession create`  
Interactive session creation.

* `websession create --from-bookmarks <profile_path> <bookmarks_path>`  
Create a session from a bookmarks folder.

All the commands also implement `--help` for more accurate reference.

### Dependencies
Features related to fetching data from Firefox involves connecting to a SQLite database. Therefore the tool is written in Python which is the only dependency.
* Python 3.7+

### Session model
A sample session is available [there](https://github.com/skaaj/ffsession/blob/main/data/vanilla/sample.json) for reference. It is formatted in JSON. At the moment the schema is very straightforward as it is just a collection of URLs. Nevertheless, the way those configurations files are organized is very important because the script depends on it.
* `/config/user`: sessions created directly (yes, you can!) or from `create`.
* `/config/bookmarks`: sessions created from the last sync with your bookmarks.
Last thing to note, the name of the file equals the name of the session.
