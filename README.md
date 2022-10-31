# pytorch-vsumm-reinforce
This repo contains the Pytorch implementation of the AAAI'18 paper - [Deep Reinforcement Learning for Unsupervised Video Summarization with Diversity-Representativeness Reward](https://arxiv.org/abs/1801.00054). The original Theano implementation can be found [here](https://github.com/KaiyangZhou/vsumm-reinforce).

This repo is forked from (https://github.com/KaiyangZhou/pytorch-vsumm-reinforce).

## 用法

要求环境： python=2.7 torch==0.4.0 cuda=9.1

(由于实际运行有些问题，所以我在`main.py`中 23 行加入 `torch.backends.cudnn.enabled = False`)

1. 克隆代码仓库，下载数据集

```shell
git clone git@github.com:1099255210/pytorch-vsumm-reinforce.git
```

数据集：[百度网盘](链接：https://pan.baidu.com/s/1so9yMGs-oy_QBWeUZb9K6w?pwd=joau)

在代码仓库中创建 `dataset` 文件夹，将数据集解压到该文件夹下

分割数据：

```shell
python create_split.py -d datasets/eccv16_dataset_summe_google_pool5.h5 --save-dir datasets --save-name summe_splits  --num-splits 5
```

这样数据被分成五份

2. 如何训练

```shell
python main.py -d datasets/eccv16_dataset_summe_google_pool5.h5 -s datasets/summe_splits.json -m summe --gpu 0 --save-dir log/summe-split0 --split-id 0 --verbose
```

训练之后的模型默认保存在 `./log/summe-split0` 中（上面的代码只选取了split0中的数据训练）

3. 如何测试

```shell
python main.py -d datasets/eccv16_dataset_summe_google_pool5.h5 -s datasets/summe_splits.json -m summe --gpu 0 --save-dir log/summe-split0 --split-id 0 --evaluate --resume path_to_your_model.pth.tar --verbose --save-results
```

这样就在 log 文件夹中得到了结果 `result.h5`

可视化 score-vs-gtscore:

```
python visualize_results.py -p path_to/result.h5
```

4. 可视化摘要

运行 `summary2video.py` 可以生成摘要视频。

代码作者给出的数据集是提取特征后的，原视频数据在：(https://data.vision.ee.ethz.ch/cvl/SumMe/SumMe.zip)

首先需要找到 `result.h5` 的结果中有哪些视频，可以使用 `readh5data.py` 检查一下里面视频的编号，然后在数据集中找到对应的原视频。

然后需要将原视频每一帧提取出来，全部保存到一个文件夹内，命名方法是 {%6d.jpg}，从 `000001.jpg` 开始。

这一步骤可以使用 ffmpeg 实现：

```shell
ffmpeg -i video.mp4 %6d.jpg
```

然后运行：

```shell
python summary2video.py -p path_to/result.h5 -d path_to/video_frames -i 0 --fps 30 --save-dir log --save-name summary.mp4
```

即可在 `./log` 文件夹中得到摘要过后的视频

如果需要查看别的视频的摘要，修改命令行中 -i 后的数字即可