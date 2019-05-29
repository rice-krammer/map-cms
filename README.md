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

# API Endpoints
Map CMS provides a number of API endpoints that allow clients to add/alter/remove data to/from the database. Other repositories such as [Webview](https://github.com/rice-krammer/map-webview) and [Sentiment Analysis](https://github.com/rice-krammer/sentiment-analysis) use these API endpoints to make meaning of the stored data.

### `GET /api/entries/<id>`
Lists all the entries, ordering by the id DESC. If `<id>` is provided, then shows a single entry of the given id.
```
[
    {
        "id": 2,
        "entry": "Such an amazing day!",
        "pub_datetime": "2019-05-29T12:16:11.818381-05:00",
        "pub_recently": true,
        "pub_location": "0.020001, 0.010001"
    },
    {
        "id": 1,
        "entry": "I was feeling down today, but it is getting better!",
        "pub_datetime": "2019-05-24T11:06:27-05:00",
        "pub_recently": false,
        "pub_location": "29.725062, -95.389317"
    }
]
```

### `POST /api/entries/`
Posts a new entry to the journal. The request IP should be whitelisted to allow posts from authorized clients.
```
{
    "entry": "This is an example entry.",
    "pub_loc_long": "0.000000",
    "pub_loc_lat": "0.000000"
}
```