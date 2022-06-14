# Flask REST API with MongoDB
Simple Book Shelf API with Flask and Mongo DB (Flask PyMongo).

Instructions:
  1. Install Mongo DB
  2. Start Mongo server in task manager > service (windows) or `sudo systemctl start mongod` (ubuntu)
  3. Type `mongo` or `mongo --port 27017` in terminal/cmd.
  4. Create a database called *BookShelf* with `use BookShelf`.
  5. Create a collection called *Books* with `db.createCollection("Books")`.
  6. Insert sample documents with
  ```
  db.Books.insertMany([
    {_id:NumberInt(1), title:"Deniz Kurdu", author:"Jack London", page:NumberInt(376)},
    {_id:NumberInt(2), title:"İki Şehrin Hikayesi", author:"Charles Dickens", page:NumberInt(508)},
    {_id:NumberInt(3), title:"Araba Sevdası", author:"Recaizade Mahmut Ekrem", page:NumberInt(320)},
    {_id:NumberInt(4), title:"Çalıkuşu", author:"Reşat Nuri Güntekin", page:NumberInt(541)},
    {_id:NumberInt(5), title:"Titan'ın Laneti", author:"Rick Riordan", page:NumberInt(282)},
    {_id:NumberInt(6), title:"Şimşek Hırsızı", author:"Rick Riordan", page:NumberInt(363)},
    {_id:NumberInt(7), title:"Gohor: Cam Kent", author:"Aşkın Güngör", page:NumberInt(200)},
    {_id:NumberInt(8), title:"Kurtlar Yolu", author:"Aşkın Güngör", page:NumberInt(176)},
    {_id:NumberInt(9), title:"Özgürlük Uğruna", author:"Barış Müstecaplıoğlu", page:NumberInt(280)},
    {_id:NumberInt(10), title:"Marslı", author:"Andy Weir", page:NumberInt(416)},
    {_id:NumberInt(11), title:"Beyaz Diş", author:"Jack London", page:NumberInt(258)},
    {_id:NumberInt(12), title:"Çile", author:"Necip Fazıl Kısakürek", page:NumberInt(512)},
    {_id:NumberInt(13), title:"İlahi Komedya", author:"Dante", page:NumberInt(838)},
    {_id:NumberInt(14), title:"1984", author:"George Orwell", page:NumberInt(352)},
    {_id:NumberInt(15), title:"Sefiller", author:"Victor Hugo", page:NumberInt(400)}
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
  2. 'GET' &nbsp; &nbsp; &nbsp; &nbsp;: "/Books/```<book id>```"     ->  Get books by id
  3. 'GET' &nbsp; &nbsp; &nbsp; &nbsp;: "/Author/```<author name>```"  ->  Get books by author name
  4. 'POST' &nbsp; &nbsp; &nbsp;: "/Books"                 ->  Send JSON Body to add new books (can do with Postman, swagger, etc.)
  5. 'PUT' &nbsp; &nbsp; &nbsp; &nbsp;: "/Books/```<book id>```"      ->  Update books by id with a JSON Body
  6. 'DELETE' : "/Books/```<book id>```"      ->  Delete books by id
