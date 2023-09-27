# Using Environment Variables in Flask

## The Problem

When developing programs, in this case web apps, we often have secret pieces of
information that we don't want to include on our public repositories.

A common way to handle this problem is to create `.env` files, which store these
secrets in "Environment Variables". The `.env` files are then added to a
`.gitignore` file, which prevents them from being pushed up to GitHub.

**Note**: I've left my `.env` file in this repository as an example. You will
most likely not want to push your own `.env` files to your repository.

Here's what a `.env` file might look like:

```bash
TEST=test
```

## Using os.eviron

Python allows us to access environment variables set for our application using
the `os` module.

We can import the `os` module in our code, use it to access a Python dictionary
storing all accessible environment variables by running `os.environ`.

Ex:

```Python
import os

print(os.environ)
# prints a Python dictionary containing the environment variables as key, value pairs

for key, value in os.environ.items():
    print(key, value)
# iterates over the Python dictionary and prints the corresponding key / values
```

If you run this commands on your own computer, you'll probably see A LOT of
values printing out. Those are all the different variables your Operating system
is using!

You can also just access a single environment variable by running
`os.environ.get('ENV_VARIABLE')` using Python's built in dictionary `.get()`
method. If this method does not find a variable with the specified name, it will
return `None`.

Ex:

```Python
import os

os.environ.get('TEST')
```

Note that `os.environ` won't immediately work with `.env` files. More on that
further down!

## Development vs. Production

Since we won't be adding `.env` files to our remote repositories, we also likely
won't be adding those files to our production environment - we'll usually take
care of that setup when configuring our production environment ourselves,
whether through a cloud provider or manually.

For example, here's the screen where you can set environment variables for the
Render hosting platform:

![image
(3)](https://github.com/Matt-Eva/using-environment-variables-in-flask/assets/89106805/80c8dfe5-7fff-4c11-a95d-a77ee9621593)

> Note: this was posted 2023-09-27 - if you are viewing this at a substantially
> later time, Render's layout may have changed.

That means `.env` files are mostly useful to us in development mode.

## python-dotenv

However, using the `os.environ.get()` method won't work with `.env` files right
out of the box. Instead, we can use a python package, `python-dotenv` to allow
us to use `.env` files in development mode.

This package is what's know as a "developer dependency" - our code only depends
on it in the development environment, not the production environment.

To install this package in our application using `pipenv`, you can run `pipenv
install python-dotenv`.

You can then import and use this package anywhere in your code:

```Python
from dotenv import load_dotenv
load_dotenv()
```

By invoking the `load_dotenv()` function, we give ourselves the ability to
access environment variables via `os.environ.get()` throughout our code when
working in a development environment.

## Keeping development and production separate

Because `python-dotenv` is likely going to be just a dev dependency, we don't
necessarily want to require it within our main application code that will be
launched in production - `app.py`, most likely, if you're working with `Flask`.

Instead, we can make a separate file - maybe called `dev.py` - in which we can
use `load_dotenv()` and import and invoke our `app`.

Here's an example of what that might look like:

```Python
# dev.py
from dotenv import load_dotenv
load_dotenv()
from app import app

if __name__ == "__main__":
    app.run()
```

To run our app in development mode, we could invoke this file by running
`python3 dev.py`.

Note that we're running the `load_dotenv()` function before we import `app`. We
do this so the `load_dotenv()` runs first before any code in app runs. This will
allow any code that uses `os.environ.get()` throughout our actual application to
successfully access environment variables.

## Conclusion

And that's that! You can check out the files in this repo as an example. Your
configuration may differ slightly depending on the file structure of your
project, but this is a quick and easy way to access environment variables
declared in `.env` files throughout your Flask application while working in
development mode.

Happy coding! Hope this was helpful!
