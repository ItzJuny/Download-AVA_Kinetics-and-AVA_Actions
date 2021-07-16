# AVA 时空检测数据集

https://research.google.com/ava/download.html#ava_actions_download

```
.
├── source
├── ava-actions
├── ava-kinetics
├── readme.md
```

- `souce`：存放官网下载文件。

- `ava-kinetics`，`ava-actions`：下载数据集视频的脚本。

## AVA-Actions(v2.2)

包含 430 个视频，其中235 个用于训练、64 个用于验证和 131 个用于测试。每个视频有 15 分钟的注释，间隔为 1 秒。

[AVA-Actions(v2.2)数据集下载](https://research.google.com/ava/download/ava_v2.2.zip)，同时我也存放在[source](/AVA-Actions2/source/)文件夹下，下载后会有以下文件：

`行为类别文件`：

- ava_action_list_v2.2_for_activitynet_2019.pbtxt：60类行为，Evaluate时使用。

- ava_action_list_v2.2.pbtxt：80类行为。

`行为标签文件`：

- ava_train_v2.2.csv、ava_val_v2.2.csv、ava_test_v2.2.txt。

`其他文件`：

- 每个视频要检测的位置，即第902到1798秒。
  - ava_included_timestamps_v2.2.txt
- 不需要进行检测的timestamp，即 train/val/test 数据集中每个视频不需要进行检测的timestamp。
  - ava_test_excluded_timestamps_v2.2.csv
  - ava_train_excluded_timestamps_v2.2.csv
  - ava_val_excluded_timestamps_v2.2.csv

## AVA-Kinetics(v1.0)

包含来自 AVA v2.2 的原始 430 个视频，以及来自[Kinetics-700 数据集的](https://deepmind.com/research/open-source/kinetics)的238k个视频 。

[AVA-Kinetics(v1.0)数据集下载](https://storage.googleapis.com/deepmind-media/Datasets/ava_kinetics_v1_0.tar.gz))，同时我也存放在[source](/AVA-Actions2/source/)文件夹下，下载后会得到以下文件。

`行为类别文件`：

- ava_action_list_v2.2.pbtxt：80类行为。

- ava_action_list_v2.2_for_activitynet.pbtxt：60类行为，Evaluate时使用。

`行为标签文件`：

- AVA数据集：ava_test_v2.2.csv，ava_train_v2.2.csv，ava_val_v2.2.csv。

- kinetics数据集：kinetics_test_v1.0.csv，kinetics_train_v1.0.csv，kinetics_val_v1.0.csv。

# 视频下载

由于AVA官方版本，只提供注释，类别等文件，不提供视频下载。

## 下载AVA-Actions视频

`cd ava-actions`

```
.
├── download.py
├── trainval_src.txt
├── test_src.txt
├── readme.md
```

- `trainval_url.txt`，`test_url.txt`：训练集验证集、测试集可以直接下载的url文件，在win下可以直接使用迅雷，IDM批量下载；ubuntu下直接wget即可。
- `download.py`：如果不采用上述方法下载，亦可用download.py下载。
  
    ```
    python download.py --url_txt <urlfile> --output_dir <output_dir>
    ```

> https://github.com/cvdfoundation/ava-dataset

## 下载AVA-Kinetics视频

`cd ava-kinetics`

```
.
├── download.py
├── all.csv
├── test.csv
├── test.csv
├── train.csv
├── readme.md
```

- `all.csv`，`train.csv`，`test.csv`，`val.csv`：训练集、验证集、测试集、所有数据集的Youtube ID，包括起止时间。

- `download.py`：download.py下载。

  ```
  python download.py  --input_csv <csvfile> --output_dir <output_dir>
  ```

> https://github.com/gurkirt/kinetics-download-prep

# 视频处理

## MMAction2

待续

## PySlowFast

待续

