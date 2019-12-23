# NeteaseMusicPlaylistExportScript
基于NeteaseCloudMusicApi的简单导出个人歌单歌曲列表的脚本。

这个脚本简单导出某个用户创建的所有歌单信息为自定义的JSON。
感谢创造了[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)这个项目的人们，我一直在找一些方法导出自己的歌单信息备份，直到遇到了它。

#### how to use
1. 你需要配置并启动[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)的服务。
2. 登录网易云音乐网页版拿到你的UID。
3. 替换UID，运行。

#### 导出的JSON结构
```
[
  {
    "name": "歌单名",
    "description","歌单描述",
    "tags","歌单标签",
    "tracks":[
      {
        "name","歌曲名",
        "alias","歌曲别名",
        "artist","艺术家",
        "album",{
          "name","专辑名",
          "img_url","专辑封面图链接"
         },
        "duration","歌曲时长"
      }
    ]
  }
]
```
