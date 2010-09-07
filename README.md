# django-fabtastic

Deploying Django projects is not an inherently fun task. It's not an
extremely difficult process, however, there are plenty of tedious, repetitive 
tasks that take precious time and keystrokes.

Each person or company handles their deployments in a slightly different
manner. There are a near infinite number of ways to deploy, maintain, and
update Django projects, each with their own benefits and limitations.
django-fabtastic is [DUO Interactive](http://duointeractive.com)'s 
philosophy on deployment, and is what we use for our own projects. 

This Django app can be dropped into any project, providing you with a quick, 
easy, standardized deployment method.

## Notes and assumptions

django-fabtastic does not attempt to be a one-size-fits-all solution. It is
aimed at what we need for our deployments. As is such, if you need a feature
implemented, feel free to open an issue in the tracker, or better yet,
fork and send a pull request.

As far as assumptions we make for those wishing to use this app:

* You are running [Django](http://djangoproject.com) 1.1 or higher.
* We strongly recommend Python 2.6+, but not 3.x (yet). It very well may run
  just fine on earlier Python versions, but we have done no testing below
  Python 2.6.
* You are using or wanting to use [Fabric](http://fabfile.org).
* We currently only implement Postgres DB operations. We'd love patches for
  others, though.
* You are using [virtualenv](http://pypi.python.org/pypi/virtualenv) and 
  [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper).
  
## Philosophy

We like Django. We like Fabric. Fabric is [thankfully] not at all tied to
Django, which is great. However, we found ourselves juggling Django
settings and environment stuff way too often. We also found ourselves wishing
we could just run certain segments of the deployment process in-place on
an arbitrary server or staging or development machine without any thought.

Fabric *can* do this just fine, but we didn't like cluttering our
fabfile with all of the extra sub-sections of our deployment process. We also
realized that our deployment scripts being ran entirely from a client machine
meant that some really bad assumptions were being made:

* The values in all of our local settings.py (and deployment/staging settings)
  are always in sync with what's in production.
* No overridden (local_settings.py, anyone?) values exist in production.

These caused us some grief, as we tend to keep sensitive settings out of our
git repositories. The best way to overcome the aformentioned limitations and
correct our assumptions was to chunk the deployment process out into
manage.py commands and some includable Fabric scripts that call them as needed.

In this way, we find ourselves with a useful set of management and deployment
commands that are guaranteed to always have the correct settings and
Django environment on all of our machines: local, staging, or production.