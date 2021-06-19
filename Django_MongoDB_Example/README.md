# Django MongoDB Example
## Note : 
```bash
    Djongo

    Djongo is a Django-MongoDB connector made by Nesdis. This connector is very easy to use because it supports all django contrib libraries. Using Djongo, all we need to do is setting up and changing the models base import, no need to worry about changing serializers, views, and all other modules. To use Djongo, make sure you have Python 3.6 or higher and MongoDB 3.4 or higher installed (if we need to use nested queries, then we need MongoDB 3.6 or higher) and start to make our projects.
```
### Requirements
```bash
    python3 -m venv myenv
    source myenv/bin/activate
    pip3 install --upgrade pip
    pip3 install django
    pip3 install djangorestframework
    # MongoDB tie into Django Package
    pip install djongo
```
3. Install MongoDB
```bash
sudo apt-get install mongodb
```
4. supported command
```bash
python3 manage.py startapp cards apps/cards
```


## Checked mongoDB in Linux
```bash
    mongodb
```

[MongoDB With Django](https://pypi.org/project/djongo/)