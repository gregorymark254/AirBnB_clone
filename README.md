0x00. AirBnB clone - The console

More Info
Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231207%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231207T052905Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=471bc0148a52202720d0788fd83e172cac54d7395c431e838080b22e108abe2b" alt="project">