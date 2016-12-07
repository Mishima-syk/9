# Mishima syk #9

今回は64bit ubuntuでTensorFlowを動かしますので環境の設定は事前に済ませておくとよいです。
特に初回のvagrant up時にubuntuイメージをダウンロードするのでかなり待たされます。

## 事前準備

事前にvagrant環境を構築しておきます。

### VirtualBoxのインストール

[VirtuarlBox](https://www.virtualbox.org/)のサイトから自分の環境にあったパッケージをダウンロードしてインストールします。

### Vagrantのインストール

[Vagrant](https://www.vagrantup.com/)のサイトから自分の環境にあったパッケージをダウンロードしてインストールします。

### 仮想環境(Ubuntu)の構築

ターミナル画面からコマンドを打っていきます。    

    vagrant init ubuntu/trusty64
    vagrant up #　これに時間がかかります。

## Ubuntu環境の構築 (anacondaを使ったお手軽な方法)

もとネタは[こちら](https://iwatobipen.wordpress.com/2016/11/13/%E3%82%B1%E3%83%A2%E3%82%A4%E3%83%B3%E3%83%95%E3%82%A9%E3%81%AB%E4%BD%BF%E3%81%88%E3%81%9D%E3%81%86%E3%81%AA%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%82%92%E3%81%BE%E3%82%8B%E3%81%A3%E3%81%A8/)

### anacondaをインストールする

まずは仮想環境にログインします。

    vagrant ssh

続いてanacondaをインストールします

    wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
    bash ./Anaconda3-4.2.0-Linux-x86_64.sh
    vim ~/.bashrc

最終行に以下を追記

    export "PATH=/home/vagrant/anaconda3/bin:$PATH"

condaを利用してtensorflow,keras,rdkitをインストールします。

    conda install -c conda-forge tensorflow
    conda install -c conda-forge keras=1.0.7
    conda install -c rdkit rdkit=2016.03.4

### jupyterでのアクセスのための設定（エディタが苦手とか対話環境が欲しい場合）

一度仮想環境からでます。Ctrl-Dかlogout
仮想環境を停止します

    vagrant halt

Vagrantfileを編集します

    vi Vagrantfile

config.vm.network "private_network"という行を探してコメント(#)を外します。viの場合xを押すと削除されます

これでホストマシンからアクセスできるようになったので仮想環境を起動します

    vagrant up
    vagrant ssh


ipythonを起動してパスワードの設定をします。

    $ ipython
    Python 3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:53:06) 
    Type "copyright", "credits" or "license" for more information.
    
    IPython 5.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: from notebook.auth import passwd
    
    In [2]: passwd()
    Enter password: 
    Verify password: 
    Out[2]: 'sha1:6e413d4ae936:325643af79a370bdce884587f5a0ec6a15d01257'

設定ファイルを作るために一度jupyter notebookを起動します

    jupyter notebook

起動させたら終了します。設定ファイルを追記します

    vim .jupyter/jupyter_notebook_config.py

内容はこれです

    c = get_config()
    c.NotebookApp.ip = '*'
    c.NotebookApp.password = u'sha1:6e413d4ae936:325643af79a370bdce884587f5a0ec6a15d01257'
    c.NotebookApp.open_browser = False
    c.NotebookApp.port = 8888

これでjupyterを起動すればホストからブラウザでアクセスできるようになります。

### TensorFlowを使ったDeepLarning

データは[AstraZenecaのLogP](https://www.ebi.ac.uk/chembl/assay/inspect/CHEMBL3301363)を利用します。

## Ubuntu環境の構築 (古臭いやり方、正当なやり方ともいう)

常に新しいバージョンのtensorflowやRDKitを使いたい場合にはこちらのインストールのほうが良いです。

## 余裕があれば書きます

TODO:書けたら書く

## Error関連

### vagrant upでボックスがダウンロードできない

vagrant upが上手くいかない

    $ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Box 'hashicorp/precise32' could not be found. Attempting to find and install...
        default: Box Provider: virtualbox
        default: Box Version: >= 0
    The box 'hashicorp/precise32' could not be found or
    could not be accessed in the remote catalog. If this is a private
    box on HashiCorp's Atlas, please verify you're logged in via
    `vagrant login`. Also, please double-check the name. The expanded
    URL and error message are shown below:
    
    URL: ["https://atlas.hashicorp.com/hashicorp/precise32"]
    Error: 

このエラーのときは[curlが古い可能性](http://stackoverflow.com/questions/23874260/error-when-trying-vagrant-up#)があります。

    sudo rm -rf /opt/vagrant/embedded/bin/curl

で解決した

+### 自分のPCに↑の環境を作れない人→ Cloud9でどうぞ。
+↓にCloudサービスのCloud9上に、ハンズオン環境の構築手順を書きました。
+10分もあれば作れます。ただし、HDDが2GBなのでかつかつなため、ずっと使い続けるには無理がある。
+https://github.com/kochi0603/mishima9/blob/master/README.md
