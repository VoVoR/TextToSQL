python evaluation.py --gold [gold file] --pred [predicted file] --etype [evaluation type] --db [database dir] --table [table file]

arguments:
  [gold file]        gold.sql file where each line is `a gold SQL \t db_id`
  [predicted file]   predicted sql file where each line is a predicted SQL
  [evaluation type]  "match" for exact set matching score, "exec" for execution score, and "all" for both
  [database dir]     directory which contains sub-directories where each SQLite3 database is stored
  [table file]       table.json file which includes foreign key info of each database