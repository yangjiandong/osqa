 学习django系列 - osqa
======================

# 2012.01.19

1. git

    git remote add origin git@github.com:yangjiandong/osqa.git
    git push -u origin master
    
2. setup

    http://www.zhimaq.com/ 芝麻问答
    code:https://bitbucket.org/felinx/zhimaq ,use django,tornado?
    same other: http://www.osqa.net/ ，http://svn.osqa.net/svnroot/osqa/trunk/ 

    install packages for osqa:
    easy_install django
    easy_install html5lib
    easy_install markdown
    easy_install python-openid
    easy_install south
    easy_install django-debug-toolbar
    easy_install mysql-python

    sudo ./bin/pip install -U html5lib markdown python-openid django-debug-toolbar mysql-python
  
    syncdb and migrate
    python manage.py syncdb --all
    python manage.py migrate forum --fake
    python manage.py migrate attachments
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

    other error:
    a. ImportError: cannot import name mark_safe 
    http://wiki.osqa.net/display/docs/Ubuntu+with+Apache+and+MySQL?focusedCommentId=3047880#comment-3047880 

    In /forum/utils/html.py
    replace
    from django.template import mark_safe
    with
    from django.utils.safestring import mark_safe

    leo

    b. django.core.exceptions.ImproperlyConfigured: App with label attachments could not be found --没影响

    c. copy settings_local.py.dist to settings_local.py

    set APP_URL = "http://...."

    d. add tornado server

    app.py
    run: python app.py

3. vim nedtree

    delete file
    Highlight the file you want to delete
    Press ‘m’
    Press ‘d’
    Press ‘y’

4. add docs

   --END    
