# Live-Poller

## Author

Weidi Zhang

## License

[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](LICENSE.md)

## Description

Live Poller is a platform created with Flask that allows for quick and efficient polling, designed specifically for use in a live setting where many people are gathered together at one place. 

## Features

* Management panel for all polls: create, delete, close, share, and view results
* Specify which IP addresses can manage polls; by default this is set to localhost (127.0.0.1)
* Highly customizable: poll question/text, add an unlimited number of possible responses, choose the closing time of the poll
* Share a poll with a page that displays a QR code that can be quickly scanned by mobile users
* Simplicity in voting - no extra bloat on any page
* Session checking to avoid repeat voters on a poll
* Visual results for all poll results, with all information (e.g. number of votes, percentage) placed on top of the result bars
* Results page automatically updates - no need for manual refresh

## Screenshots

* [Manage Page](doc/images/screenshot-manage.png)
* [Manage Page: Poll Creation](doc/images/screenshot-manage-create.png)
* [Share Page](doc/images/screenshot-share.png)
* [Vote Page](doc/images/screenshot-vote.png)
* [Results Page](doc/images/screenshot-results.png)
* [Results Page (2)](doc/images/screenshot-results-2.png)

## Libraries/Packages Used
* [Bootstrap](https://getbootstrap.com/)
* [Flask](http://flask.pocoo.org/)
* [Flask-QRCode](https://marcoagner.github.io/Flask-QRcode/)
* [flatpickr](https://flatpickr.js.org/)
* [jQuery](https://jquery.com/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)

## Requirements
* Python 3.6+

## Installing Required Python Packages
```
pip install Flask
pip install flask-qrcode
```

## Running Live-Poller

1. Edit ```config.py``` as needed.
2. Use the provided ```run.bat``` (Windows) or ```run.sh``` (Mac / Linux) scripts.
