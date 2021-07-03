# the_paper_scraper

A major issue with the opencvf [and nips/icml] website is that every paper's link is a separate hyperlink. Browsing through so many webpages on a single page becomes painful. 

Anyways, i went ahead and wrote a scraper which downloads all the papers off the website in lexicographic order from opencvf's website and generates a merged manuscript. This should work as a temporary collection of all the proceedings. 

None of the compiled papers here are my own work. I am just putting stuff att a single place so that i could go through it quickly to extract relevant ideas. Ok, enough about this. 

Here's how you must get it to work. 

1. Set `url` variable in `generate_combined_pdf.py`
2. Run script as:
`python generatte_combined_pdf.py`
3. Voila!! `mergedfilesoutput.pdf` should appear in the repos root. rename accordingly. 


Love, 
rajat