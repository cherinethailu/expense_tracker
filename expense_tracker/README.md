**Setup Instructions:**

Clone the repository
Create a virtual environment(recommended) and install dependencies - ```pip install -r requirements.txt```
Run migrations - ```python manage.py makemigrations```, ```python manage.py migrate```
Start the development server - ```python manage.py runserver [port]```
Visit ```/swagger/``` for Swagger API documentation

Endpoints Summary:
POST ```/api/users/``` - Create a new user.
GET ```/api/expenses/``` - List all expenses.
POST ```/api/expenses/ ```- Create a new expense.
GET ```/api/expenses/<id>/``` - Retrieve expense details.
PUT ```/api/expenses/<id>/``` - Update an expense.
DELETE ```/api/expenses/<id>/``` - Delete an expense.
GET ```/api/expenses/by-date-range/``` - List expenses by date range.
GET ```/api/expenses/category-summary/``` - Get expense summary by category.