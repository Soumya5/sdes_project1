source/15307r001.pdf: source/Phase_plot.png source/Plot_of_states.png source/15307r001.tex source/15307r001.bbl source/15307r001.blg source/15307r001.html
	cd source && pdflatex 15307r001.tex
	cd source && pdflatex 15307r001.tex
	mv source/15307r001.pdf output/15307r001.pdf
	cd source && rm -f *.aux *.log *.blg *.bbl *.png *.toc *.pyc

source/15307r001.html: source/15307r001.ipynb
	cd source && ipython nbconvert 15307r001.ipynb
	if [ ! -d ./output ]; then mkdir output; fi
	mv source/15307r001.html output/15307r001.html
	
source/Phase_plot.png source/Plot_of_states.png: source/vanderpol_oscc.py
	cd source && python vanderpol_oscc.py
	cd source && rm -f *.pyc

source/15307r001.bbl source/15307r001.blg: source/15307r001.bib
	cd source && pdflatex 15307r001.tex
	cd source && bibtex 15307r001

test:
	cd source && python test_vanderpol_oscc.py

.PHONY: clean

clean:
	cd source && rm -f *.aux *.log *.blg *.bbl *.png *.toc  *.pyc *.html
	rm -rf output
