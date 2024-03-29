![enter image description here](https://i.imgur.com/a9oTpld.png)
# 0x17. Web stack debugging #3

-   Foundations - System engineering & DevOps ― Web stack debugging
-   By Sylvain Kalache, co-founder at Holberton School
-   Ongoing project - started 05-17-2021, must end by 05-20-2021 (in about 2 hours) - you're done with  100% of tasks.
-   Checker was released at 05-18-2021 10:48 PM
-   QA review fully automated.

## Concepts

_For this project, students are expected to look at these concepts:_

-   [Web Server](https://intranet.hbtn.io/concepts/17)
-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

## Background Context

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It  [actually powers 26% of the web](https://intranet.hbtn.io/rltoken/Ah9_LmUi191dqxT-Zx7uhg "actually powers 26% of the web"), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements

### General

-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   Your Puppet manifests must pass  `puppet-lint`  version 2.1.1 without any errors
-   Your Puppet manifests must run without error
-   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
-   Your Puppet manifests files must end with the extension  `.pp`
-   Files will be checked with Puppet v3.4

## More Info

### Install  `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
## Author
 
 - **Juan Carlos Hernández** : Twitter - [@luigi_jong](https://twitter.com/luigi_jong)
 
##  info

 - Date 19/05/2021
 - Holberton school Colombia 
 - Cohort #13 BOG0920