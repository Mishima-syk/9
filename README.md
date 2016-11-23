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
    export "PATH=/home/ubuntu/anaconda3/bin:$PATH"

condaを利用してtensorflow,keras,rdkitをインストールします。

    conda install -c conda-forge tensorflow
    conda install -c conda-forge keras=1.0.7
    conda install -c rdkit rdkit=2016.03.4


### TensorFlowを使ったDeepLarning

これで解析環境が整いました。

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