"""Utility to use the WebODM API to create user accounts for workshop"""

import click
import os
from webodm_admin.api import WebODMAPI
from dotenv import load_dotenv

load_dotenv()


@click.group()
@click.pass_context
def webodm(ctx):
    ctx.obj = {"api": WebODMAPI(os.environ.get("BASEURL"))}


@webodm.command("login")
@click.pass_obj
@click.argument("username", type=str, required=True)
@click.password_option()
def login(obj, username, password):
    if not hasattr(obj['api'], 'baseurl') or obj['api'].baseurl is None:
        click.echo("Please set BASEURL of your webODM in environment")
    _ = obj["api"].auth_token(username, password)
    click.echo(f"logged in as {username}")


@webodm.command("users")
@click.pass_obj
@click.argument("number", type=int, required=True)
@click.option("--prefix", type=str, default="workshop")
@click.option("--password", type=str)
def users(obj, number, prefix, password):
    """Create a set of new users, option of prefix and password"""

    if not password:
        if os.environ.get("BASEPWD"):
            password = os.environ.get("BASEPWD")
        else:
            click.echo("Please either set a --password or put one as BASEPWD in .env")
            return
    for i in range(1, number + 1):
        username = f"{prefix}{i}"
        print(username)
        user_password = f"{password}{i}"

        response = obj["api"].create_user(username, user_password)
    click.echo(f"added {number} new users")


@webodm.command("getuser")
@click.pass_obj
@click.argument("userid", type=int, required=True)
def getuser(obj, userid):
    """Get info for a userid (numeric)"""

    response = obj["api"].get_user(userid)

    click.echo(response)


webodm.add_command(login)
webodm.add_command(users)
webodm.add_command(getuser)
