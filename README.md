# PyChooseU (multiple choice question tester)

* Reads multiple csv files with question data
* Displays each question with four answers
* Checks and displays correct choice after answer entered
* Allows user to choose number of questions to display
* Displays score (%), number of correct/incorrect answers, and completion time at the end
* Can write all output to a text file for review once complete

## Usage 
1. Create or use folder (`csvdata/` by default) for question data  
*(If using new directory, update `questions_dir` variable)*
2. Add `csv` files with question data (**pipe `|` separated**) in the form:  
`question | option A | option B | option C | option D | answer (a-d)`
3. Run `pychooseu.py`
4. Choose how many questions you want to display (hit `enter` to display all)
5. Enter `a-d` to answer or `q` to quit
6. (Optional) View results output file in `output` directory

### Docker Usage
1. Do a docker build with the Dockerfile  
`docker build -t pychooseu .`
2. Run the container interactively  
`docker run -i --name pychooseu pychooseu`
3. (Optional) To save the results, view the container logs and pipe output to a file  
`docker logs pychooseu > results.txt`
