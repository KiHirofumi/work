# workリポジトリについて

## 背景

このリポジトリは
LINEbot、およびそのソースを管理するためのGitHubを学習するためのリポジトリです。

## line bot

まずはおうむ返し状態をCommitしてあります。
今後、育てていきます。

## 暫定目標

ユーザーからの質問に対して、とあるデータから問い合わせ結果を返してあげる

## ルール

- ブランチ名は「なにを開発してるか」わかるものに
- コミット単位はできるだけ小さく
- プルリクエストは完成前でも良い（レビューとして使用）
- 課題や今後開発したいことはissueに記載する

---

# GitHubの使用方

1. https://github.com/KiHirofumi/work にて、右上にあるForkボタンを押下(初回のみ)

   - 自分のGitHub（Gitのネットワーク上、リモートリポジトリ）に取得

2. コマンドでcloneする

   1. ForkしたGitHubページにある「Clone or download」ボタン押下して、自分のGitHubのページのアクセス情報をコピー
   2. 自分の開発ディレクトリに移動（例はICディレクトリ）
      > cd IC

   3. gitを開始する
      > git init

   4. 以下のアドレスは自分でcloneのアドレスコピーしたものを貼り付ける

      > git clone git@github.com:KiHirofumi/work.git

      とか

      > git clone https://github.com/KiHirofumi/work.git

   5. cloneしてきたディレクトリに移動

      > cd work

3. branch
   - なんの開発するか明確にする
     - 「main関数に呼び出し元を作成」とか
    1. 現在のbranchを確認(最初はmasterになっている)
        >git branch

    1. branchを作成し、そこで作業する
        > git branch main関数に呼び出し元を作成
        > git checkout main関数に呼び出し元を作成

## 開発

4. コードを追加
     - 開発をローカルの環境で実施

5. 変更をコミット
     - 開発をGit上に保存

6. リモートブランチ作成
     - 自分のGitHubに同名ブランチを作成
     - pushでGitHubに保存
        > git push origin ブランチ名

## 完了処理（レビュー）

7. Pull Requestを送る

test[20200705][tatehisa]
test[20200712][tatehisa]
test[20200820][tatehisa]