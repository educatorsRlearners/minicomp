sudo apt-get update

git clone https://github.com/ADGEfficiency/minicomp-rossman
#kaggle competitions download -c data-science-bowl-2019
cd minicomp-rossman
python data.py
cd data
mkdir $HOME/minicomp
mv *.zip $HOME/minicomp
sudo apt-get install unzip
unzip $HOME/minicomp/*.zip -d $HOME/minicomp/raw-data