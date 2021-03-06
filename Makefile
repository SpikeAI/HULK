default: pdf html

diff:
	git diff  --color-words -r 00d0776b2c6d0c2192e9bed1326f7629f54ed0c6  hulk.tex | aha > 2019-09-06_diff.html

pdf:
	latexmk -pdf hulk.tex

html:
	jupyter nbconvert --to html_embed Annex.ipynb --output=index.html

tmp_database:
	mkdir -p /tmp/database/ && rsync -a "/Users/laurentperrinet/science/VB_These/Rapport d'avancement/database/Face_DataBase/Raw_DataBase" /tmp/database/

fetch_delete_frioul:
	rsync -av -u --delete --exclude .AppleDouble --exclude .git perrinet.l@frioul.int.univ-amu.fr:/hpc/invibe/perrinet.l/ICLR/HULK/cache_dir .

fetch_frioul:
	rsync -av -u --exclude .AppleDouble --exclude .git perrinet.l@frioul.int.univ-amu.fr:/hpc/invibe/perrinet.l/ICLR/HULK/cache_dir .
