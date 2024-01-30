from db import employeeCollection

class LoginController:
   @staticmethod
   def fetchEmployee(username: str, password: str):
      data = employeeCollection.find_one({'username': f"{username}", 'password': f'{password}'}, {'_id': 0})
      return data
