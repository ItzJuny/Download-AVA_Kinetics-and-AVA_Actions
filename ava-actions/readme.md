# 下载AVA-Actions视频

1. 🐱‍🏍`trainval_url.txt` 和`test_url.txt`：加入官网aws数据源的可下载url文件。
   
2. 🐱‍🏍WIN系统使用迅雷，IDM批量下载；ubuntu下直接wget即可。

3. 🐱‍🏍`download.py`如果不采用上述方法下载，亦可用download.py下载。
    ```python
    python download.py --url_txt <urlfile> --output_dir <output_dir>
    ```
    例如：
    ```
    python download.py --url_txt test_url.txt --output_dir test/
    ```

> https://github.com/cvdfoundation/ava-dataset

