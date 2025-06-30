People!
======

_Django Social Media App - Social Networking called "People", built to learn the framework_


### What is it

Is a simple, non production ready, Social Media Web Application use for learning and meant to be used as an example. 

Quick Start
-----------

* Make sure you have Python3.12 installed else please install via --> https://www.python.org/downloads/
* Install MySQL, preferably `MySQL 8`, should work in lower version but I developed using version 8 so can't guarantee it works for older ones.

```bash
git clone git@github.com:Koubae/people.git
cd people
# create Python environment 
python -m venv env 
# Activate (linux)
source env/bin/activate
# Activate (windows)
env/Scripts/activate.bat

# Install 
python -m pip install requirements.txt
# (Optional) Install development dependencies
python -m pip install dev_requirements.txt
# Go Inside MySQL
mysql -u<user> -p<password
# create database 'people'
mysql> CREATE DATABASE people;
mysql> USE people;
mysql> SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| people     |
+------------+
# exit mysql 
mysql> exit

# Cool now, let's create migration to intialize the database
python manage.py makemigrations
python manage.py migrate

# run Django 
python manage.py runserver

# Now go to
localhost:8000
```

### Login

Now use can use the demo user to login

* **Email:** `awesome.guy@demo.com`
* **Password:** `awesome`
* **Username:** `peoplePerson`
* **First Name:** `Guy`
* **Last Name:** `Awesome`


#### Stack

* Python3.12
* Django 5
* Django Template _intentionally avoiding using any 'big' javascript framework in order to use Django Templating system_
* MySQL 8

### Specifications 

* [Model Structure](./model_structure.md)
* User password for testings: `xPwVOJ-L0vVY3ERaLKgWOg`

Projects
---------------

### Plugin - Django Library and cool Projects

* [Datta Able Django](https://github.com/app-generator/django-datta-able)
* [Django Material Dashboard](https://github.com/app-generator/django-material-dashboard)

* [django-cities](https://github.com/coderholic/django-cities)
* [django-smart-selects](https://github.com/jazzband/django-smart-selects)


### Other Django Examples

_Here a list of some example I found in github and online_

* [django-realworld-example-app](https://github.com/gothinkster/django-realworld-example-app/tree/master)
* [My django project](https://github.com/mach1el/my-django)
* [E-Commerce Project For Baby Tools](https://github.com/MET-DEV/Django-E-Commerce)
* [example.django.mi_aplicacion](https://github.com/macagua/example.django.mi_aplicacion)
* [django-blog-example](https://github.com/rgab1508/django-blog-example)
* [simple-django-page](https://github.com/90x-Development/simple-django-page)
* [Simple Django Signals](https://github.com/BaseMax/SimpleDjangoSignals)
* [django-tutorial-step-by-step](https://github.com/consideratecode/django-tutorial-step-by-step)


Troubleshooting
---------------

To keep things more organize, rather than have the application in root of the repository, I moved it inside [app](./app) folder.
PyCharm by default starts and expect Django application to be developed at root level, so in order to make it work see the below article

In general simply do

1. Go to Settings --> Languages & Frameworks --> Django --> 
2. Modify `Django Project Root` and make it pointing to `app` 

Additionally you may want to change Run configuration of PyCharm, set `Working Directory` also to `app` folder


* [Getting Pycharm to run Django tests after moving the entire django source to a subfolder](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000622670-Getting-Pycharm-to-run-Django-tests-after-moving-the-entire-django-source-to-a-subfolder)


### PyCharm complaining about 'templates' folder

* [PyCharm code inspection complains template file not found, how to fix?](https://stackoverflow.com/questions/20873625/pycharm-code-inspection-complains-template-file-not-found-how-to-fix)


Further Reading
---------------

* [Organize django apps inside](https://stackoverflow.com/questions/73354083/organize-django-apps-inside)
* [When to create a new app (with startapp) in Django?](https://stackoverflow.com/questions/64237/when-to-create-a-new-app-with-startapp-in-django)
* [How to execute external script in the Django environment](https://stackoverflow.com/questions/41825037/how-to-execute-external-script-in-the-django-environment)
* [How to define default data for Django Models?](https://stackoverflow.com/questions/39739439/how-to-define-default-data-for-django-models/39742847#39742847)
* [Django - Working with many-to-many intermediary models](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#working-with-many-to-many-intermediary-models)
* [Ordering admin.ModelAdmin objects in Django Admin](https://stackoverflow.com/questions/398163/ordering-admin-modeladmin-objects-in-django-admin)
* [how to have "city" fields depending on "country" field in Django models, without creating their tables](https://stackoverflow.com/questions/39806588/how-to-have-city-fields-depending-on-country-field-in-django-models-without)
* https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

#### Social Media Related stuff

* [What is Facebook's architecture?](https://www.quora.com/What-is-Facebooks-architecture-6)
* [Facebook shares some secrets on making MySQL scale](https://ahmadrais.blogspot.com/2011/12/facebook-shares-some-secrets-on-making.html)
* [Database normalization](https://en.wikipedia.org/wiki/Database_normalization)
* [Falsehoods Programmers Believe About Names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)

* [Design a friends table for a social networking site](https://stackoverflow.com/questions/36998526/design-a-friends-table-for-a-social-networking-site)
* [MySQL Structure for a social network](https://stackoverflow.com/questions/9930940/mysql-structure-for-a-social-network)
* [Database schema for a social network website? MySql?](https://stackoverflow.com/questions/66652245/database-schema-for-a-social-network-website-mysql)
* [Social web application database design: how can I improve this schema?](https://stackoverflow.com/questions/3844477/social-web-application-database-design-how-can-i-improve-this-schema)
* [Table structure for social media content](https://stackoverflow.com/questions/36648479/table-structure-for-social-media-content)
* [Guide To Design Database For Social Network System In MySQL](https://mysql.tutorials24x7.com/blog/guide-to-design-database-for-social-network-system-in-mysql)
* [MySQL Social Network Database](https://github.com/j84guo/mysql-social-network)
* [Analyzing Social Media Data with SQL](https://learnsql.com/blog/sql-social-media-analysis/)
* [Going against the grain — Why we chose MySQL for building Social Graph](https://medium.com/gameskraft-engineering/why-we-chose-mysql-for-social-graph-service-332bc40ffcc9)
* [SQL database for a social network](https://codereview.stackexchange.com/questions/153710/sql-database-for-a-social-network)
* [Database 101: How social media “likes” are stored in a database](https://dev.to/danielhe4rt/database-101-how-social-media-likes-are-stored-in-a-database-3oii)
* [In a MySQL social network database, should likes of posts and comments be in the same or separate tables?](https://www.quora.com/In-a-MySQL-social-network-database-should-likes-of-posts-and-comments-be-in-the-same-or-separate-tables)
* [Database Design for Facebook: A Social Network Database Example](https://www.youtube.com/watch?v=sougyTO_Wjw)
* ['schema' design for a social network](https://stackoverflow.com/questions/2839725/schema-design-for-a-social-network?rq=4)
* [social networking website database management](https://stackoverflow.com/questions/3013103/social-networking-website-database-management?rq=4)
* [Database scheme design social networking sites](https://stackoverflow.com/questions/2489739/database-scheme-design-social-networking-sites?rq=4)
* [How to model database tables for implementing Friend relationship? [closed]](https://stackoverflow.com/questions/379236/how-to-model-database-tables-for-implementing-friend-relationship)
* [How to store bidirectional relationships in a RDBMS like MySQL?](https://stackoverflow.com/questions/10807900/how-to-store-bidirectional-relationships-in-a-rdbms-like-mysql)
* [What is the best way to implement Polymorphic Association in SQL Server?](https://stackoverflow.com/questions/7000283/what-is-the-best-way-to-implement-polymorphic-association-in-sql-server)

* FOAF (FOAF Friend of a Friend)-format. <-- What is it? | ref : https://stackoverflow.com/a/379301/13903942
  * http://www.foaf-project.org
  * https://en.wikipedia.org/wiki/FOAF
  * https://www.amazon.com/dp/0123735564

* What is **Boyce-Codd Normal Form (BCNF)** --> https://github.com/j84guo/mysql-social-network/tree/master?tab=readme-ov-file#mysql-schema
