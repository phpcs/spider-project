## 获取考试类型和分类蜘蛛命令:
scrapy crawl koolearn_tiku_cate
## 获取分类和章蜘蛛命令:
scrapy crawl koolearn_tiku_chpater
## 获取题目蜘蛛命令:
scrapy crawl koolearn_tiku_question




### 说明:例如获取题目可能数量较多,耗时久,可以暂停或者恢复爬虫
<pre>

要启用一个爬虫的持久化，运行以下命令:

scrapy crawl koolearn_tiku_cate -s JOBDIR=crawls/somespider-1
然后，你就能在任何时候安全地停止爬虫(按Ctrl-C或者发送一个信号)。恢复这个爬虫也是同样的命令:

scrapy crawl koolearn_tiku_cate -s JOBDIR=crawls/somespider-1

</pre>

<pre>
CREATE TABLE `koolearn_cate` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `exam_type` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '' COMMENT '考试方向',
  `cate` varchar(64) COLLATE utf8mb4_bin NOT NULL DEFAULT '' COMMENT '分类',
  `url` varchar(255) COLLATE utf8mb4_bin NOT NULL DEFAULT '' COMMENT 'url的path',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
</pre>


<pre>
CREATE TABLE `koolearn_chapter` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `exam_type` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '考试类型',
  `cate` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '分类',
  `second_cate` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '左侧二级分类',
  `chapter_name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '章名',
  `url` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '章详情url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3910 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
</pre>


<pre>
CREATE TABLE `koolearn_question` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `chapter_id` int(11) unsigned NOT NULL COMMENT '章关联id',
  `question_title` varchar(800) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '题目标题',
  `question_option` varchar(800) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '选项',
  `question_answer` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '题目答案',
  `question_type` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '题目类型',
  `question_analysis` varchar(900) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '题目解析',
  PRIMARY KEY (`id`),
  KEY `chapter_id` (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=167 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
</pre>