# Flask REST API with MongoDB
Simple Book Shelf API with Flask and Mongo DB (Flask PyMongo).

Pseudo Code:

1. Import Libraries
2. Read YAML configuration file for database credentials.
3. Add Mongo URI to app configuration.
4. Get an instance of Mongo DB.
5. Define endpoints.

Endpoints:
  1. 'GET'    : "/Books"                 ->  Get all books
  2. 'GET'    : "/Books/<book name>"     ->  Get books by name
  3. 'GET'    : "/Author/<author name>"  ->  Get books by author name
  4. 'POST'   : "/Books"                 ->  Send a JSON Body to add new books (can be done by Postman, swagger, etc.)
  5. 'PUT'    : "/Books/<book name>      ->  Update books by name with a JSON Body (again, can be done by Postman, swagger, etc.)
  6. 'DELETE' : "/Books/<book name>      ->  Delete books by name
