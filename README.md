# Krammer Map CMS
Krammer Map is an anonymous and collaborative online journal to share feelings. The project has two dependencies: [Webview](https://github.com/rice-krammer/map-webview) and [CMS](https://github.com/rice-krammer/map-cms). CMS (Content Management System) is built with [Django Framework](https://www.djangoproject.com). All installation instructions assume you already have [Homebrew](http://brew.sh) installed. If you are not running on MacOS or a Linux distribution, see the hyperlinks for dependencies.

# Dependencies
* [Python](https://www.python.org/) (≥ 3.7)
* [PIP](https://github.com/pypa/pip) (≥ 19.0.0)
```bash
brew install python3
```

# Installation
Verify you have Python ≥ 3.7 installed:  
```bash
python --version
python3 --version
```

Now we can install the repository. Run the following commands line by line:

```bash
git clone https://github.com/rice-krammer/map-cms
cd map-cms/
pip3 install -r requirements/dev.txt
```

After all the modules in requirements are installed, run the migration script:

```bash
python3 manage.py migrate
```
Now, create a super user. Run the following command and then proceed with the instructions:

```bash
python3 manage.py createsuperuser
```

Finally, start the server:

```bash
python3 manage.py runserver
```