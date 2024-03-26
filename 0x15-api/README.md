# Project Name.
**0x15. API**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   You must use `get` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary).
*   Your code should not be executed when imported (by using if` __name__ == "__main__":`).


## Project Description.
Learn what Bash scripting should not be used for. What is an API, a REST API, microservices. What is the CSV format and the JSON format.
Pythonic Package and module name style. Pythonic Class name style.
Pythonic Variable name style. Pythonic Function name style.
Pythonic Constant name style. Significance of CapWords or CamelCase in Python.


* **0. Gather data from an API** - Write a Python script that, using this REST API[(https://jsonplaceholder.typicode.com/)], for a given employee ID, returns information about his/her TODO list progress. - `0-gather_data_from_an_API.py`.

  Requirements:

  * You must use `urllib` or `requests` module.
  * The script must accept an integer as a parameter, which is the employee ID.
  * The script must display on the standard output the employee TODO list progress in this exact format:
    * First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
      * `EMPLOYEE_NAME`: name of the employee.
      * `NUMBER_OF_DONE_TASKS`: number of completed tasks.
      * `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks.
    * Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`).

  Example:
  ```
  sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
  Employee Ervin Howell is done with tasks(8/20):
      distinctio vitae autem nihil ut molestias quo
      voluptas quo tenetur perspiciatis explicabo natus
      aliquam aut quasi
      veritatis pariatur delectus
      nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
      repellendus veritatis molestias dicta incidunt
      excepturi deleniti adipisci voluptatem et neque optio illum ad
      totam atque quo nesciunt
  sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
  Employee Patricia Lebsack is done with tasks(6/20):
      odit optio omnis qui sunt
      doloremque aut dolores quidem fuga qui nulla
      sint amet quia totam corporis qui exercitationem commodi
      sequi dolorem sed
      eum ipsa maxime ut
      tempore molestias dolores rerum sequi voluptates ipsum consequatur
  sylvain@ubuntu$
  sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
  EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
  TSoditSoptioSomnisSquiSsunt
  TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
  TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
  TSsequiSdoloremSsed
  TSeumSipsaSmaximeSut
  TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
  sylvain@ubuntu$
  ```
---

* **1. Export to CSV** - Using what you did in the task #0, extend your Python script to export data in the CSV format. - `1-export_to_CSV.py`.

  Requirements:

  * Records all tasks that are owned by this employee.
  * Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`.
  * File name must be: `USER_ID.csv`.

  Example:
  ```
  sylvain@ubuntu$ python3 1-export_to_CSV.py 2
  sylvain@ubuntu$ cat 2.csv
  "2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
  "2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
  "2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
  "2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
  "2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
  "2","Antonette","True","aliquam aut quasi"
  "2","Antonette","True","veritatis pariatur delectus"
  "2","Antonette","False","nesciunt totam sit blanditiis sit"
  "2","Antonette","False","laborum aut in quam"
  "2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
  "2","Antonette","False","repudiandae totam in est sint facere fuga"
  "2","Antonette","False","earum doloribus ea doloremque quis"
  "2","Antonette","False","sint sit aut vero"
  "2","Antonette","False","porro aut necessitatibus eaque distinctio"
  "2","Antonette","True","repellendus veritatis molestias dicta incidunt"
  "2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
  "2","Antonette","False","sunt cum tempora"
  "2","Antonette","False","totam quia non"
  "2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
  "2","Antonette","True","totam atque quo nesciunt"
  sylvain@ubuntu$
  ```
---

* **2. Export to JSON** - Using what you did in the task #0, extend your Python script to export data in the JSON format. - `2-export_to_JSON.py`.

  Requirements:

  * Records all tasks that are owned by this employee.
  * ormat must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`.
  * File name must be: `USER_ID.json`.

  Example:
  ```
  sylvain@ubuntu$ python3 2-export_to_JSON.py 2
  sylvain@ubuntu$ cat 2.json
  {"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$
  ```
---

* **3. Dictionary of list of dictionaries** - Using what you did in the task #0, extend your Python script to export data in the JSON format. - `3-dictionary_of_list_of_dictionaries.py`.

  Requirements:

  * Records all tasks from all employees.
  * ormat must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`.
  * File name must be: `todo_all_employees.json`.

  Example:
  ```
  sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
  sylvain@ubuntu$ cat todo_all_employees.json
  {"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false}, {"username": "Bret", "task": "fugiat veniam minus", "completed": false}, {"username": "Bret", "task": "et porro tempora", "completed": true}, {"username": "Bret", "task": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false}, {"username": "Bret", "task": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false}, {"username": "Bret", "task": "illo expedita consequatur quia in", "completed": false}, {"username": "Bret", "task": "quo adipisci enim quam ut ab", "completed": true}, {"username": "Bret", "task": "molestiae perspiciatis ipsa", "completed": false}, {"username": "Bret", "task": "illo est ratione doloremque quia maiores aut", "completed": true}, {"username": "Bret", "task": "vero rerum temporibus dolor", "completed": true}, {"username": "Bret", "task": "ipsa repellendus fugit nisi", "completed": true}, {"username": "Bret", "task": "et doloremque nulla", "completed": false}, {"username": "Bret", "task": "repellendus sunt dolores architecto voluptatum", "completed": true}, {"username": "Bret", "task": "ab voluptatum amet voluptas", "completed": true}, {"username": "Bret", "task": "accusamus eos facilis sint et aut voluptatem", "completed": true}, {"username": "Bret", "task": "quo laboriosam deleniti aut qui", "completed": true}, {"username": "Bret", "task": "dolorum est consequatur ea mollitia in culpa", "completed": false}, {"username": "Bret", "task": "molestiae ipsa aut voluptatibus pariatur dolor nihil", "completed": true}, {"username": "Bret", "task": "ullam nobis libero sapiente ad optio sint", "completed": true}], "2": [{"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false}, {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": true}, {"username": "Antonette", "task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false}, {"username": "Antonette", "task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false}, {"username": "Antonette", "task"
  ....
  ETC
  ```
---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
