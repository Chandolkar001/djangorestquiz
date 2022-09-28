"# djangorestquiz" 

Main URL: https://djangorestquiz.herokuapp.com/

| Method | API endpoints | parameters |usecase    |
|--------|---------------|------------|-----------|
|  get   | /users        | - | gets all the users registered to the portal |
|  post  | /users        | username, password | accepts username, password and registers a user | 
|  post | /create_question | title, description, correct_ans | Accepts the parameters and registers a question only if the user is an Admin|
| post | /create_quiz | quiz_title, question_id, quiz_start, quiz_end | Accepts the parameter and registers a quiz only if the user is an Admin |
| get | /quiz | - | Responds with a list of availabe quizes for the user |
| post | /submit_quiz | quiz_id, answer | Submits the quiz with the parameters |
| get | /account_detail | - | Gets the account details of the logged in user with score, username,etc |
