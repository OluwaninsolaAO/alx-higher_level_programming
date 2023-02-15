# 0x0E SQL More Queries

__Project Descriptor:__ SQL multi users managements (including USER
CREATION, GRANTS and PERMISSIONS) multi table operations, usage of
table contraints and many more were all explored in this section.
SQL Style Guide were also considered for all the sql queries within
this directory following recommended common practices.

```
-- This is a comment.

SELECT first_name AS fn, last_name AS ln, staff_id AS sid
 WHERE sid BETWEEN 100 AND 250
 ORDER BY last_name ASC;
```

> _NB: all python scripts/files ```*.py``` are checked to be Pycodestyle_
> _compliant. The choice Style Guide for Python Code._
