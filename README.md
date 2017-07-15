# Steps to install the omoads Django project

## To Run Locally
* Make a separate folder named omoProject
```bash
mkdir omoProject
```

* Make a virtual environment for the installation of right versions of the tools used in this repo.
```bash
virtualenv omoenv
```

* Activate the created virtual environment
```bash
source omoenv/bin/activate
```

* Clone the repo under the folder omoProject
```bash
git clone https://github.com/shivangg/omoads.git
```

* change directory to omads
```bash
cd omoads
```

* Checkout the djangoAdd branch
```bash
git checkout djangoAdd
```

* Install the required dependencies
```bash
pip install -r requirements.txt
```

* Create the core database tables
```bash
python manage.py migrate
```

* Run the local webserver
```bash
python manage.py runserver
```
* Checkout the site at http://localhost:8000
