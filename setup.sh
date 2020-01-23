sudo apt-get update
cd $HOME
git clone https://github.com/ADGEfficiency/minicomp-rossman
#kaggle competitions download -c data-science-bowl-2019
cd minicomp-rossman
python data.py
cd data
mkdir -p $HOME/minicomp
mv *.zip $HOME/minicomp
sudo apt-get install unzip
unzip $HOME/minicomp/*.zip -d $HOME/minicomp/raw-data