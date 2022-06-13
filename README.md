# Flask REST API with MongoDB
Simple Book Shelf API with Flask and Mongo DB (Flask PyMongo).

Instructions:
  1. Install Mongo DB
  2. Start Mongo server in task manager > service (windows) or `sudo systemctl start mongod` (ubuntu)
  3. Type `mongo` or `mongo --port 27017` in terminal/cmd.
  4. Create a database called *BookShelf* with `use BookShelf`.
  5. Create a collection called *Books* with `db.createCollection("Books")`.
  6. Insert sample collections with
  ```
  db.Books.insertMany([
      {_id:1, title:"Deniz Kurdu", author:"Jack London"},
      {_id:2, title:"İki Şehrin Hikayesi", author:"Charles Dickens"},
      {_id:3, title:"Araba Sevdası", author:"Recaizade Mahmut Ekrem"},
      {_id:4, title:"Çalıkuşu", author:"Reşat Nuri Güntekin"},
      {_id:5, title:"Titan'ın Laneti", author:"Rick Riordan"},
      {_id:6, title:"Şimşek Hırsızı", author:"Rick Riordan"},
      {_id:7, title:"Gohor: Cam Kent", author:"Aşkın Güngör"},
      {_id:8, title:"Kurtlar Yolu", author:"Aşkın Güngör"},
      {_id:9, title:"Özgürlük Uğruna", author:"Barış Müstecaplıoğlu"},
      {_id:10, title:"Marslı", author:"Andy Weir"},
      {_id:11, title:"Beyaz Diş", author:"Jack London"},
      {_id:12, title:"Çile", author:"Necip Fazıl Kısakürek"},
      {_id:13, title:"İlahi Komedya", author:"Dante"},
      {_id:14, title:"1984", author:"George Orwell"},
      {_id:15, title:"Sefiller", author:"Victor Hugo"}
  ])
  ```

Pseudo Code:
  1. Import Libraries
  2. Read YAML configuration file for database credentials.
  3. Add Mongo URI to app configuration.
  4. Get an instance of Mongo DB.
  5. Define endpoints.

Endpoints:
  1. 'GET' &nbsp; &nbsp; &nbsp; &nbsp;: "/Books"                 ->  Get all books
  2. 'GET' &nbsp; &nbsp; &nbsp; &nbsp;: "/Books/```<book id>```"     ->  Get books by name
  3. 'GET' &nbsp; &nbsp; &nbsp; &nbsp;: "/Author/```<author name>```"  ->  Get books by author name
  4. 'POST' &nbsp; &nbsp; &nbsp;: "/Books"                 ->  Send a JSON Body to add new books (can be done by Postman, swagger, etc.)
  5. 'PUT' &nbsp; &nbsp; &nbsp; &nbsp;: "/Books/```<book id>```"      ->  Update books by name with a JSON Body
  6. 'DELETE' : "/Books/```<book id>```"      ->  Delete books by name
