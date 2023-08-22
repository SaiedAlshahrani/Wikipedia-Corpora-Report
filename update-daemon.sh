pip3 install --quiet selenium==3.141.0 geckodriver-autoinstaller==0.1.0 python-dateutil

python update-metadata.py

# git lfs install
git clone https://huggingface.co/datasets/SaiedAlshahrani/test
cd Wikipedia-Corpora-Report/

head -n1 ../English--Wikipedia--Metadata.csv > Wikipedia-Corpora-Report.csv
sed -i '' 1d ../*--Wikipedia--Metadata.csv
cat ../*--Wikipedia--Metadata.csv >> Wikipedia-Corpora-Report.csv
# cp -r ../all-metadata .

git add .
git status
git commit -m "Update Wikipedia-Corpora-Report.csv"
git push

rm ../*--Wikipedia--Metadata.csv
cp Wikipedia-Corpora-Report.csv ..
cd ..

