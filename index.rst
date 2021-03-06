=====================================
Pythonな会社でchefしてる例の紹介
=====================================

.. s6:: styles

   'h1': {marginTop:'0.5em'},

おまえ、誰よ
=============
.. figure:: face.png

* `http://清水川.jp/ <http://清水川.jp/>`_
  `@shimizukawa <http://twitter.com/shimizukawa>`_
* 活動:
   * Sphinxメンテナ, Sphinx-users.jp会長
   * Python系, XP系, PyConJP 2012 副座長
* 言語:
   * C++/C/8086/**Python**/Rails/chef


.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'65%'},
    'div[0]': {width:'15%', position:'absolute', top:'1em'},

提供
=====

.. figure:: beproud.gif

.. s6:: effect slide

.. s6:: styles

   'h2': {fontSize:'120%', textAlign:'center'},
   'div[0]/img': {margin:'2em', marginTop:'1.5em', width:'80%'},
   'div/img': {border:'0.1em gray outset'},

最初はVagrant
==============

* VirtualBoxのコンソール出さずに使える便利
* chefっていうので環境設定できるらしい
* 見よう見まねで使ってみる -> **便利！！**

.. s6:: effect slide

会社のRedmineの管理が大変
==========================

* Pythonの会社なのでメンテナンスが大変
* Redmineにプラグイン入れてそのままリポジトリ管理
* 構築手順とか残っているような無いような・・
* よしchefを使おう

.. s6:: effect slide

Redmineはアプリ？ミドルウエア？
================================

* **ミドルウエアです**
* ミドルウエアなのでCapistranoは使いません
* ということでChefで突き進みます

.. s6:: effect slide

Redmineの構成
===============

.. figure:: django_skypehub.png

.. s6:: effect slide

.. s6:: styles

   'div[0]/a/img': {margin:'2em', marginTop:'1.5em', width:'80%'},

Redmineセットアップ出来た
==========================

* rvm入れてruby入れる
* redmine入れる
* redmineプラグイン入れる
* 記法をreSTにしてblockdiag対応させる
* DBサーバーとか設定する
* apache設定する

.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'80%'},

DBセットアップ出来た
=====================

* MySQL入れる
* GRANTする

.. s6:: effect slide

これからやる
===============

* Skypeプラグイン入れよう
* Mercurialリポジトリサーバー起動させる
* メール送信設定

.. s6:: effect slide

あきらめ
==========

* Skypeクライアントのインストール

  * xvfbにvncで接続してインストールウィザードをクリックする

.. s6:: effect slide

悩み1
=======

* 最初に使い始める人に簡単に使う方法を提供したい

  * VirtualBox + Vagrant + (Berkshelf | Librarian)
  * Rubyに明るくないのでgem周りでけっこうはまる

.. s6:: effect slide



社内での反応
=============

* 半年前は **chefなの？** という感じ
* 今はみんな「興味はある」
* 最初のハードル(Vagrant+chef)がクリアされると「よさそう」という反応

* とりあえず開発に使用し始めました！


.. s6:: effect slide

悩み2
=======

* RedmineのバージョンアップをChefでどうやって表現するの？

  * chefで環境つくればいいから、新しい環境作って切り換えかなあ

.. s6:: effect slide

はまり1
========

* attributesに ``default[:mycookbook][:key] = 'value'`` で初期設定
* recipesで ``node[:mycookbook][:key]`` で使う

  * Vagrantで ``chef.json = {:mycookbook => {:key => 'other'}}``
  * 動く

* Vagrantに設定せずrolesに移行

  * 動かない！！

.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'70%'},

はまり2
========

* ``recipe[nginx]``

  * nginxサーバー立ち上がった

* ``recipe[jenkins::proxy_nginx]``

   * nginxをソースから入れようとする
   * **nginxユーザーを作ろうとして失敗する><**


.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'80%'},

自作cookbook
=============

* 自分でいくつか作ったものを公開してます

  * https://github.com/shimizukawa?tab=repositories

* rvm-redmine : rvm環境にredmineをインストール
* bp-redmine : rvm-redmine上にBP社カスタマイズ
* python-build : Pythonの2.4-3.3までビルド
* download-make-install : CMMIです

.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'65%'},
