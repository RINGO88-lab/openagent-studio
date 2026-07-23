# Git - 什么时候用什么指令

## 场景1：第一次开始写项目
git init                    # 创建仓库（一个项目只做一次）
git remote add origin 地址   # 关联 GitHub（一次）
# 以后就不用再做了

## 场景2：每天写代码结束
git status        # 看看改了什么
git add .         # 把所有修改加进来
git commit -m "Day X: 做了什么"  # 提交
git push          # 推到 GitHub

## 场景3：改错了想撤回
git diff                  # 看看改了啥
git restore 文件名         # 还没 add 之前，撤回修改
git restore --staged 文件名 # 已经 add 了，撤回暂存

## 场景4：想看看历史
git log --oneline     # 看所有提交
git log --oneline -5  # 只看最近5条

## 场景5：想试新功能，又怕搞坏
git branch dev        # 创建一个新分支
git switch dev        # 切换到新分支
# 在新分支上随便改，不影响 main
git switch main       # 切回主分支
git merge dev         # 确定没问题了，合并到 main

## 场景6：多人协作或换电脑
git pull              # 先拉取最新代码
# 改完代码后
git add . && git commit -m "xx" && git push  # 提交推送

## 场景7：下载别人的项目
git clone 地址   # 下载到本地
