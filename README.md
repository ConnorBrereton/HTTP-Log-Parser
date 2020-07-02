# HTTP Log File Parser
## 🚀 Sample Invoking
```
> python3 log_parser.py

Start time (HH:MM:SS):07:25:00

End time (HH:MM:SS):07:26:00

Want to add file for analysis? (y/n):y

File name: log_sample.txt

Between time 07:25:00 and time 07:26:00:
vimeo.com returned 11.76% 5xx errors
player.vimeo.com returned 23.53% 5xx errors
api.vimeo.com returned 0.00% 5xx errors
```


## 📑 Dependencies
- You must have Python3 installed. To install Python3 please see this tutorial [here](https://realpython.com/installing-python/).

- You must have `sys` and `time` modules imported to be used in coupling with Python3.


## 🤔 Assumptions
There are a few things we need to consider given that we were told in the instructions that we have a `10GB` file even though our sample file is only `4KB`.

* Because I used `readlines()` the entirety of the file read will be loaded into local memory (RAM). Most machines these days come with at least 8GB of RAM with most being 16GB of RAM. We would not be bounded by memory in this case but it will be slow to load all of this data, especially a huge file like 10GB with only one processor. This is the best implementation because Pyhton will automatically figure out the optimal buffer size to read *n-chunks* of data in at a time for us rather than creating a buffer ourselves.

* I used `readlines()` because *(a)* I knew that I had enough RAM to handle any edge cases and *(b)* I knew that a small 4KB file will not cause any processor or RAM bottlenecks.

* One solution if we didn't have enough RAM to process the entire file would be to use `external merge sort` to buffer our file into smaller files and process them all at once and merge together in order at the end. To see an excellent impelementation of external merge sort please check [this](https://github.com/melvilgit/external-Merge-Sort) out.