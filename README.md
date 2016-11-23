# Mishima syk #9

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

#### error

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