## Semester project for the Case Solving Seminar
<http://www.wi2.fau.de/teaching/master/master-courses/css/>

### Theme: Customer profiling using stylometric features

Paper to be available soon at: [https://dmpe.github.io/PapersAndArticles/](https://dmpe.github.io/PapersAndArticles/)

The final presentation can be found at: [http://www.slideshare.net/F789GH/customer-linguistic-profiling](http://www.slideshare.net/F789GH/customer-linguistic-profiling)

#### Notes:
* Original data are available for download to the public from <http://mypersonality.org/wiki/doku.php?id=wcpr13>

* Check different *Jupyter Notebook(s)* and */src/* folder, in order to (attempt to) reproduce our results:
    * **Statuses only** by using TF-IDF Vectorizer and Bag-of-words (n-grams). <https://github.com/dmpe/CaseSolvingSeminar/blob/github/R_scripts_and_notebooks/baseline_2_status_only.ipynb>
    
    * **Derived columns** from FB's statuses which **only use 13 stylometric features**. <https://github.com/dmpe/CaseSolvingSeminar/blob/github/src/derived_columns_only.ipynb>
    
    * **Combination** of both approaches above: use of statuses (n-grams) and 13 derived stylometric features. <https://github.com/dmpe/CaseSolvingSeminar/blob/github/src/derived_columns.ipynb>

**Team members are**:

* [@dmpe](https://github.com/dmpe)
* [@dustinwind](https://github.com/dustywind)
* Keekan

### Installation of Python libraries and other tools

You should use the script from here <https://gist.github.com/dmpe/3a8987e9197b86b636ba> for downloading all the libraries which we installed on our PC. 

So, basically, download the `list.txt` locally, and execute (on Ubuntu OS) `sudo pip3 install -r list.txt`
