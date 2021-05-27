![enter image description here](https://i.imgur.com/qYlM1Hg.png)
# 0x1A. Application server

-   Foundations - System engineering & DevOps ― Web stack
-   By Sylvain Kalache, co-founder at Holberton School
-   Ongoing project - started 05-24-2021, must end by 05-28-2021 (in about 13 hours) - you're done with  0% of tasks.
-   Checker was released at 05-26-2021 02:24 PM
-   QA review fully automated.

## Concepts

_For this project, students are expected to look at these concepts:_

-   [Web Server](https://intranet.hbtn.io/concepts/17)
-   [Server](https://intranet.hbtn.io/concepts/67)
-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210527T154233Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=131a8218a1e1d7ad0d03951f6dcdbe281fdeb67305e0cc358771190266aac845)

## Background Context

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/2ea1058f813d42c61f48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210527%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210527T154233Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0be3ff9db91520f97691540503d4833ceea285cb8d10f6eb7798e5e36b6e53dc)](https://youtu.be/pSrKT7m4Ego)

Your web infrastructure is already serving web pages via  `Nginx`  that you installed in your  [first web stack project](https://intranet.hbtn.io/rltoken/RrbqMLWOJUyVaWdXsnpvXw "first web stack project"). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your  `Nginx`  and make is serve your Airbnb clone project.

## Resources

**Read or watch**:

-   [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw "Application server vs web server")
-   [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA "How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04")  (As mentioned in the video, do  **not**  install Gunicorn using  `virtualenv`, just install everything globally)
-   [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ "Running Gunicorn")
-   [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA "Be careful with the way Flask manages slash")  in  [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA "route")  -  `strict_slashes`
-   [Upstart documentation](https://intranet.hbtn.io/rltoken/oQPs-o5UUcZkxOw5sNIM0g "Upstart documentation")

## Requirements

### General

-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Everything Python-related must be done using  `python3`
-   All config files must have comments

### Bash Scripts

-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   All your Bash script files must be executable
-   Your Bash script must pass  `Shellcheck`  (version  `0.3.7-5~ubuntu16.04.1`  via  `apt-get`) without any error
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

## Authors
 
 - **Juan Carlos Hernández** : Twitter - [@luigi_jong](https://twitter.com/luigi_jong)
 
##  info

 - Date 27/05/2021
 - Holberton school Colombia 
 - Cohort #13 BOG0920