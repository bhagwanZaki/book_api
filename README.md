# Floran Book Display Api  

Floran Book Display is an open Api created for <b><a href="https://youtube.com/playlist?list=PLOl8TbOSTlwAn8qUO-Q4lENzvk0pwpfte"> React.js workshop for beginner </a></b> to 
fetch latest and other book data along with posting new book data.

## API Information

<b>Each book object will look like this</b>
<br/>
<pre>
{
    "id": 3,
    "name": "Dummy Book 2",
    "author": "Elon Musk",
    "description": "Lorem Ipsum is simply dummy text of the printing and ….",
    "price": 500.0,
    "pages": 200,
    "cover": "https://res.cloudinary.com/floran-music/raw/upload/v1/media/default.jpg"
}
</pre>
<ol>
<li><div>
<b>To get the latest book data</b>

API: https://floran-book-api.herokuapp.com/latest/

This will return you list of 5 latest books only
</div>

<li> <div>
<b>To get other book data</b>

API: https://floran-book-api.herokuapp.com/

This will return you remaining book data other than the latest books
</div>

<li><div>
<b>To get specific book data for detail page</b>

API: https://floran-book-api.herokuapp.com/<book id>

This will return you specific book data
</div>

<li><div>
<b>To post new book data</b>
API: <a href="https://floran-book-api.herokuapp.com/">https://floran-book-api.herokuapp.com/</a>       [USE POST REQUEST]

The formdata  should contain exactly the same following key

<ul>
<li> <b>field: </b>name <b>type: </b>String
<li> <b>field: </b>author <b>type: </b>String
<li> <b>field: </b>description: <b>type: </b>String
<li> <b>field: </b>price: <b>type: </b>Float
<li> <b>field: </b>pages: <b>type: </b>Integer
<li> <b>field: </b>cover: <b>type: </b>Image File
</ul>
</div>
</ol>

## Requirement 
Python v.3.8+
## Setup

### Clone Repository

for windows, create virtual env using virtualenvwrapper-win
```bash
    pip install virtualenvwrapper-win
    mkvirtualenv reactdj
```
for linux & mac use this command
```bash
    apt-get install python3-venv  
    python3 -m venv reactdj
```

To activate environment in windows
```bash
    workon reactdj
```

To activate environment in linux & mac
```bash
    source reactdj/bin/activate
```

Copy Paste the following commands to clone the repo

```bash
    https://github.com/Floran-Github/Floran_POS.git
```

## To run backend django rest framework

Go inside the floran_pos_backend directory and install the module from requirements.txt

```bash
  cd floran_pos_backend
  pip install -r requirements.txt
 ```
 
 Then make the migrations and then migrate the database
 
 ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
  
  Create the superuser 
  
  ```bash
    python manage.py createsuperuser
  ```
  
  Now run the django server on your local network instead of localhost for react to communicate
  
  ```bash
    python manage.py runserver 0.0.0.0:8000
  ````
  
  <h2>Now you goto localhost:8000 to see the API</h2>
  
  ```bash
      http://127.0.0.1:8000/api/auth
  ```
