# postgresql_syntax_checker_magic

Introduces a %%postgresql_syntax_checker magic.


# Installing

-   Using pip install:
    pip install git+https://github.com/eyaltrabelsi/postgresql_syntax_checker

# Usage

    In [1]: %load_ext postgresql_syntax_checker
    In [2]: %%postgresql_syntax_checker
            select id from account;

![](https://github.com/eyaltrabelsi/postgresql_syntax_checker_magic/blob/master/bad_sql_syntax.jpg)
