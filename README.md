# dirCleaner
## Quick script to delete large amount of files with specific starting/ending name also with option to specify the oldness of the files you want to delete. (must be in the same directory with the files)
<br/>

```
  -h, --help     show this help message and exit
  -s , --start   Specify the starting of the files name
  -e , --end     Specify the ending of the files (mp3, pdf, html, txt, etc...)
  -d , --days    Specify how old the files should be to get cleaned (by days)
  
  Examples: 
    python dirCleaner.py -e .pdf -d 7
    python dirCleaner.py -d 30 -s img -e jpg
```
