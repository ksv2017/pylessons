![python-image][python-image]

Python Lessons
==============


### Description

This repository contains Python lessons designed to provide a basic understanding of the language.

#### Contents

![Lesson][Lesson-image1] - Introduction to functions

![Lesson][Lesson-image2] - Reading json data from API

![Lesson][Lesson-image3] - Reading csv data from yahoo API

![Lesson][Lesson-image4] - Printing environmental variables based on the OS

![Lesson][Lesson-image5] - SSH connection to the remote server

#### Pylint

In order to run [pylint](https://docs.pylint.org/en/1.6.0/installation.html) it needs to be installed since it is external analyser tool for static code analyses.

```shell
python -m pip install pylint

python -m pylint module_or_folder_name

# you should see something similar:
C:\path_to_pylessons_folder>python -m pylint urok5_ssh_connection.py
No config file found, using default configuration
************* Module urok5_ssh_connection
W: 34, 8: Unused variable 'stdin' (unused-variable)
W: 34,23: Unused variable 'stderr' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 9.17/10, +0.00)
```

#### References

[Documentation](https://docs.python.org/3/) about Python - dynamically typed programming language.

[python-image]: http://www.computeracademy.com.hk/images/course_slider/python-programming_banner.jpg
[Lesson-image1]: https://img.shields.io/badge/Lesson-1-blue.svg?style=plastic
[Lesson-image2]: https://img.shields.io/badge/Lesson-2-blue.svg?style=plastic
[Lesson-image3]: https://img.shields.io/badge/Lesson-3-blue.svg?style=plastic
[Lesson-image4]: https://img.shields.io/badge/Lesson-4-blue.svg?style=plastic
[Lesson-image5]: https://img.shields.io/badge/Lesson-5-blue.svg?style=plastic
