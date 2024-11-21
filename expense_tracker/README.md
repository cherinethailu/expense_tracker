**Setup Instructions:**

Clone the repository <br/>
Create a virtual environment(recommended) and install dependencies - ```pip install -r requirements.txt``` <br/>
Run migrations - ```python manage.py makemigrations```, ```python manage.py migrate``` <br/>
Start the development server - ```python manage.py runserver [port]``` <br/>
Visit ```/swagger/``` for Swagger API documentation <br/>

Endpoints Summary:<br/>
POST ```/api/users/``` - Create a new user. <br/>
GET ```/api/expenses/``` - List all expenses. <br/>
POST ```/api/expenses/ ```- Create a new expense. <br/>
GET ```/api/expenses/<id>/``` - Retrieve expense details. <br/>
PUT ```/api/expenses/<id>/``` - Update an expense. <br/>
DELETE ```/api/expenses/<id>/``` - Delete an expense. <br/>
GET ```/api/expenses/by-date-range/``` - List expenses by date range. <br/>
GET ```/api/expenses/category-summary/``` - Get expense summary by category. <br/>
