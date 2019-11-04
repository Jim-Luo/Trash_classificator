# Development Log

### Sep 22nd
- Constructing Framework
- Constructing Template

memo:

The webpage layout is very tricky when using Bootstrap, try more to use __Grid__ and __margin__ to solve these problems. What's more, don't forget the __Button__ component in __Navbar__ component.

todo:
- To figure out how to insert default image in back-end
- To solve Front-end images capture problem
- To learn how to do back-end routing 

### Sep 23rd

- Installing MySQL
- Deploying MySQL in the project
- Fixing the problem: the default image can be shown in the website correctly

memo:

The Django framework has been modified in 2 places. 

One is in __Trash_Classificator\venv\Lib\site-packages\django\db\backends\mysql\base.py(line: 35-36)__, the version checking function has been commented:

```python
if version < (0, 3, 0):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

The other is in __Trash_Classificator\venv\Lib\site-packages\django\db\backends\mysql\operations.py(line: 146-147)__, the string decoding function has been commented:
```python
query = query.decode(errors='replace')
```

### Sep 29th

- Creating the first table(model) in the project
- Creating a superuser for the website

memo:

The table has 4 waords : id (automatically created), content, timestamp, result. The data can be edited through superuser(admin/password).

todo:

- To finish the front- and back- end interaction 
- To finish the result-showing page and history page

### Sep 30th

- Creating the reactive mechanism in the homepage and the uploaded image can be shown in the page properly
- Creating a History page, which is used to store inquery history

memo:

Static files (e.g. JS, CSS, IMG) must be stored in a specific directory and this directory must be declared in __settings.py__ . When visited, static files' address must contain the __appName__ it belongs to. And, a special tag `{% load static %}` must be set before the reference.

```djangotemplate
{% load static %}
<script src="{% static "js/main.js" %}"></script>
``` 

todo:

- To finish the result-showing mechanism
- __To deploy the server__

### Oct 7th

- fullfiling the front- and back-end interaction part(result-showing machanism)

memo:

The process was excruciating. At the begin, I tried to use AJAX in JQuery but the current JQuery package did not support AJAX object. If I changed this package, Bootstrap would not work properly. Then I chose raw AJAX object but it did not support DJango CSRF check. I tried to figure it out but found nothing about raw AJAX resources online. As a result, I made a concession and closed the CSRF checking machanism. When it worked, the back-end could not accept the data from the front-end. So, I consulted Stackoverflow and made the following changes.


*main.js*
```javascript
// The AJAX part
var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/process", true);
        xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            document.querySelector("#result").textContent =
            this.responseText;
        }
        };
        xhttp.send(
            // tip : the transfering data must be stringfied
            JSON.stringify({
                content : reader.result
            })
        );
``` 

*views.py*
```python
#exempt csrf checking
@csrf_exempt
def process(request):
    #tip : the data should be accessed through request.body object and json.loads function 
    content = json.loads(request.body)['content']
    models.Trash.objects.create(content=content, result=0)
    return
```

todo :

- to amend front-end pages and to design the support page
- __To deploy the server__

>something might to do:
>- to excute more elegant queries
>- to implement CSRF checking
>- to implement cookies & detailed history inquery 
>- to support polyglotism


### Oct 9th

- Completing support page
- modifying result showing bar layout

todo :

- to add Keras description in support page
-  __To deploy the server__

>something might to do:
>- to excute more elegant queries
>- to implement CSRF checking
>- to implement cookies & detailed history inquery 
>- to support polyglotism
>- to unify homepage and other pages layout
>- to solve HCI problem in result bar
>- to design a icon

### Oct 27th

__SERVER DEPLOYED!__

- The Settings.py has changed, be careful when next time reboot the server.
- The password to the database has changed for the sake of security problems.

memo:
```shell script
# start the server (DEBUG MODE)
nohup python3 manage.py runserver ip:port >log.out 2>&1 &
```

todo:

- to complete support page
- to add the machine learning algorithm

>something might to do:
>- to excute more elegant queries
>- to implement CSRF checking
>- to implement cookies & detailed history inquery 
>- to support polyglotism
>- to unify homepage and other pages layout
>- to solve HCI problem in result bar
>- to design a icon
>- to change the application to a production mode (using NGINX)

