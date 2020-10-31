# Regex parse and delete

Helping my friend to parse error files and delete using python and regex for his
drupal site.

To use

```{python}
./regx-delete.py [filename]
```

Currently only works with error log files and not standard input, so no piping

Testing code also still remains, and is yet to be removed.

As a test that the code works, git clone it into a fresh directory, run
./regx-delete.py or python3 regx-delete.py by itself. It will parse the error
log in ./testregex.txt, touch the files into the directory which it will show
you and then perform a delete.
