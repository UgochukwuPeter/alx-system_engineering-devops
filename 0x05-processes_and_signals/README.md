0. What is my PID mandatory

Write a Bash script that displays its PID.

1. List your processes mandatory

Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display a user-oriented format
Show process hierarchy

2. Show your Bash PID mandatory

Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

3. Show your Bash PID made easy mandatory

Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash.

Requirements:

You cannot use ps

4. To infinity and beyond mandatory

Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

In between each iteration of the loop, add a sleep 2

5. Kill me now mandatory

We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You must use kill
Terminal #0

6. Kill me now made easy mandatory

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall
Terminal #0

7. Highlander mandatory

Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal #0

8. Beheaded process mandatory

Write a Bash script that kills the process 7-highlander.

