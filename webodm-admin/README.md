# WebODM Tutorial notes

We are running a workshop / tutorial session which includes a day on getting started with WebODM.

* [WebODM Admin API reference](https://docs.webodm.org/reference/admin/)

## Configuration 

`.env` contains the base URL of the WebODM installation

## Command-line WebODM admin

Log in, this will save an access token that will last for 6 hours:

`webodm-admin login [username]`

Create new 4 users, numbered sequentially

`webodm-admin create 4`

Set a password either with the `--password` switch or by adding `BASEPWD=[password]` into the file named `.env`

By default the users are named `workshop` 1, 2, etc

`webodm-admin create 2 --prefix tutorial --password MemorablePassword` gives you 2 new users called "tutorial1" and "tutorial2" with passwords "MemorablePassword1" and "MemorablePassword2"










## Get started 

Create a python virtual environment with `uv`

`uv venv`

Install our package and dependencies

`uv pip install -e .`

