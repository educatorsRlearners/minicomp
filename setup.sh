pip install -r requirements_final.txt
#sudo apt-get update
cd $HOME
git clone https://github.com/ADGEfficiency/minicomp-rossman
#kaggle competitions download -c data-science-bowl-2019
cd minicomp-rossman
python data.py
cd data
mkdir -p $HOME/minicomp/raw-data
#mv 'store.csv' -d $HOME/minicomp/raw-data
#mv 'train.csv' -d $HOME/minicomp/raw-data
mv 'train.csv' $HOME/minicomp/raw-data
mv 'store.csv' $HOME/minicomp/raw-data
#mv "file with spaces.txt" "new_place/file with spaces.txt"
#mv *.zip $HOME/minicomp
#sudo apt-get install unzip
#unzip $HOME/minicomp/*.zip -d $HOME/minicomp/raw-data
